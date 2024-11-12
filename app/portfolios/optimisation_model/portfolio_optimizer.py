import numpy as np
import yfinance as yf
from sklearn.ensemble import RandomForestRegressor
from sklearn.covariance import LedoitWolf
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.core.problem import ElementwiseProblem
from pymoo.optimize import minimize

def get_historical_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
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
    expected_returns = np.array(predicted_returns) * 250
    return expected_returns

def calculate_covariance_matrix(log_returns):
    lw = LedoitWolf()
    lw.fit(log_returns)
    covariance_matrix = lw.covariance_ * 250
    return covariance_matrix

class PortfolioOptimizationProblem(ElementwiseProblem):
    def __init__(self, expected_returns, covariance_matrix, rf):
        super().__init__(n_var=len(expected_returns), n_obj=1, n_constr=1, xl=0.0, xu=1.0)
        self.expected_returns = expected_returns
        self.covariance_matrix = covariance_matrix
        self.rf = rf

    def _evaluate(self, x, out, *args, **kwargs):
        weights = x / np.sum(x)
        portfolio_return = np.dot(weights, self.expected_returns)
        portfolio_variance = np.dot(weights.T, np.dot(self.covariance_matrix, weights))
        portfolio_volatility = np.sqrt(portfolio_variance)
        sharpe_ratio = (portfolio_return - self.rf) / portfolio_volatility
        out["F"] = -sharpe_ratio
        out["G"] = np.sum(weights) - 1

def optimize_portfolio(tickers, start_date, end_date, current_composition):
    prices = get_historical_data(tickers, start_date, end_date)
    log_returns = np.log(prices / prices.shift(1)).dropna()
    expected_returns = predict_expected_returns(prices)
    covariance_matrix = calculate_covariance_matrix(log_returns)
    rf = 0.01
    problem = PortfolioOptimizationProblem(expected_returns, covariance_matrix, rf)
    algorithm = GA(pop_size=100, eliminate_duplicates=True)
    res = minimize(problem, algorithm, termination=('n_gen', 100), verbose=False)
    optimal_weights = res.X / np.sum(res.X)
    return dict(zip(tickers, optimal_weights))
