import numpy as np
import yfinance as yf
from sklearn.ensemble import RandomForestRegressor
from sklearn.covariance import LedoitWolf
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.core.problem import ElementwiseProblem
from pymoo.optimize import minimize
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def get_historical_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    print(data)
    return data

def predict_expected_returns(prices):
    returns = prices.pct_change().dropna()
    features = returns.shift(1).dropna()
    targets = returns[1:]
    features = features.iloc[1:]
    targets = targets.iloc[:-1]
    predicted_returns = []
    for ticker in prices.columns:
        X = features[[ticker]]
        y = targets[ticker]
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)
        pred_return = model.predict(X.iloc[-1].values.reshape(1, -1))
        predicted_returns.append(pred_return[0])
    expected_returns = np.array(predicted_returns) * 250  # Annualize
    return expected_returns

def forecast_returns(prices, periods_ahead):
    forecasted_returns = []
    for ticker in prices.columns:
        # Calculate daily returns
        returns = prices[ticker].pct_change().dropna()
        # Fit ARIMA model (you can optimize the order)
        model = ARIMA(returns, order=(1, 0, 0))
        model_fit = model.fit()
        # Forecast future returns
        forecast = model_fit.forecast(steps=periods_ahead)
        # Calculate the cumulative return over the forecast period
        cumulative_return = np.prod(1 + forecast) - 1
        # Annualize the forecasted return
        annualized_return = cumulative_return * (250 / periods_ahead)
        forecasted_returns.append(annualized_return)
    return np.array(forecasted_returns)

def calculate_covariance_matrix(log_returns):
    lw = LedoitWolf()
    lw.fit(log_returns)
    covariance_matrix = lw.covariance_ * 250  # Annualize
    return covariance_matrix

class PortfolioOptimizationProblem(ElementwiseProblem):
    def __init__(self, expected_returns, covariance_matrix, rf, current_composition=None):
        super().__init__(n_var=len(expected_returns), n_obj=1, n_constr=2, xl=0.0, xu=1.0)
        self.expected_returns = expected_returns
        self.covariance_matrix = covariance_matrix
        self.rf = rf
        self.current_composition = current_composition

    def _evaluate(self, x, out, *args, **kwargs):
        weights = x / np.sum(x)
        portfolio_return = np.dot(weights, self.expected_returns)
        portfolio_variance = np.dot(weights.T, np.dot(self.covariance_matrix, weights))
        portfolio_volatility = np.sqrt(portfolio_variance)
        sharpe_ratio = (portfolio_return - self.rf) / portfolio_volatility
        # Objective: maximize Sharpe ratio (minimize negative Sharpe ratio)
        out["F"] = -sharpe_ratio
        # Constraints:
        # 1. Weights sum to 1
        out["G"] = [np.sum(weights) - 1]
        # 2. Optionally, include transaction cost constraint if current_composition is provided
        if self.current_composition is not None:
            # For example, limit the turnover to a maximum value
            max_turnover = 0.2  # Maximum allowable turnover (20%)
            # current_composition is a dictionary with tickers as keys and weights as values
            current_weights = np.array([self.current_composition[ticker] for ticker in self.current_composition.keys()])
            turnover = np.sum(np.abs(weights - current_weights))
            out["G"].append(turnover - max_turnover)
        else:
            out["G"].append(0)  # No additional constraint

def optimize_portfolio(tickers, start_date, end_date, current_composition=None, forecast_period_days=30):
    prices = get_historical_data(tickers, start_date, end_date)
    log_returns = np.log(prices / prices.shift(1)).dropna()
    expected_returns = predict_expected_returns(prices)
    covariance_matrix = calculate_covariance_matrix(log_returns)
    
    rf = 0.04
    
    problem = PortfolioOptimizationProblem(expected_returns, covariance_matrix, rf, current_composition)
    algorithm = GA(pop_size=100, eliminate_duplicates=True)
    res = minimize(problem, algorithm, termination=('n_gen', 100), verbose=False)
    optimal_weights = res.X / np.sum(res.X)
    
    # Forecast future returns
    forecasted_returns = forecast_returns(prices, forecast_period_days)
    
    # Calculate expected portfolio return over the forecast period
    expected_portfolio_return = np.dot(optimal_weights, forecasted_returns)
    
    return dict(zip(tickers, optimal_weights)), expected_portfolio_return