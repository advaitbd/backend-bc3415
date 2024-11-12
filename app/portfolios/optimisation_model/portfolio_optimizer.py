import numpy as np
import yfinance as yf
from datetime import datetime
from skfolio import PerfMeasure, RatioMeasure, RiskMeasure
from skfolio.optimization import MeanRisk
from skfolio.preprocessing import prices_to_returns
import pandas as pd

def get_historical_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

def optimize_portfolio(tickers, start_date, end_date, current_composition):
    # Get historical data
    prices = get_historical_data(tickers, start_date, end_date)
    
    # Calculate daily log returns
    log_returns = np.log(prices / prices.shift(1))
    
    # Calculate expected returns (mean of log returns) and covariance matrix
    expected_returns = log_returns.mean() * 250  # Annualize the returns
    covariance_matrix = log_returns.cov() * 250  # Annualize the covariance
    
    # Number of assets
    num_assets = len(tickers)
    
    # Number of portfolios to simulate
    num_portfolios = 10000
    
    # Initialize arrays to store portfolio metrics
    p_returns = []
    p_volatility = []
    p_sharpe = []
    p_weights = []
    
    # Risk-free rate (e.g., 0.01 as in the notebook)
    rf = 0.01
    
    # Simulate random portfolios
    for _ in range(num_portfolios):
        # Random weights
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        p_weights.append(weights)
        
        # Expected return
        portfolio_return = np.dot(weights, expected_returns)
        p_returns.append(portfolio_return)
        
        # Expected volatility
        portfolio_variance = np.dot(weights.T, np.dot(covariance_matrix, weights))
        portfolio_volatility = np.sqrt(portfolio_variance)
        p_volatility.append(portfolio_volatility)
        
        # Sharpe ratio
        sharpe_ratio = (portfolio_return - rf) / portfolio_volatility
        p_sharpe.append(sharpe_ratio)
    
    # Convert lists to arrays
    p_returns = np.array(p_returns)
    p_volatility = np.array(p_volatility)
    p_sharpe = np.array(p_sharpe)
    p_weights = np.array(p_weights)
    
    # Find the index of the portfolio with the maximum Sharpe ratio
    max_sharpe_idx = np.argmax(p_sharpe)
    
    # Get the optimal weights
    optimal_weights = p_weights[max_sharpe_idx]
    
    # Return a dictionary of weights
    return dict(zip(tickers, optimal_weights))