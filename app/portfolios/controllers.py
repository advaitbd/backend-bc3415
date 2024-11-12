# app/portfolios/controllers.py
from sqlalchemy.orm import Session
from app.portfolios.crud import (
    get_portfolio,
    get_portfolios_by_user_id,
    create_portfolio,
    update_portfolio,
    delete_portfolio,
)
from app.portfolios.schemas import PortfolioCreate, PortfolioUpdate, RebalanceSuggestion
from datetime import datetime, timedelta
from app.portfolios.optimisation_model.portfolio_optimizer import optimize_portfolio

def create_new_portfolio(db: Session, portfolio: PortfolioCreate):
    return create_portfolio(db=db, portfolio=portfolio)

def read_portfolio(db: Session, portfolio_id: int):
    db_portfolio = get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise ValueError("Portfolio not found")
    return db_portfolio

def read_portfolios_by_user(db: Session, user_id: str):
    return get_portfolios_by_user_id(db, user_id=user_id)

def update_existing_portfolio(db: Session, portfolio_id: int, portfolio: PortfolioUpdate):
    db_portfolio = update_portfolio(db=db, portfolio_id=portfolio_id, portfolio=portfolio)
    if db_portfolio is None:
        raise ValueError("Portfolio not found")
    return db_portfolio

def delete_existing_portfolio(db: Session, portfolio_id: int):
    db_portfolio = delete_portfolio(db=db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise ValueError("Portfolio not found")
    return db_portfolio


# Business Logic for Rebalancing
def calculate_rebalance_suggestion(db: Session, portfolio_id: int):
    # Fetch the existing portfolio
    existing_portfolio = read_portfolio(db, portfolio_id)
    current_composition = existing_portfolio.composition
    tickers = list(current_composition.keys())
    
    # Set start and end dates for historical data
    start_date = (datetime.now() - timedelta(days=14)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    
    # Get the optimized composition and expected return
    optimised_composition, expected_return = optimize_portfolio(tickers, start_date, end_date, current_composition)
    
    return RebalanceSuggestion(
        current_composition=current_composition,
        suggested_composition=optimised_composition,
        expected_return=expected_return,
        portfolio_id=portfolio_id
    )

def accept_portfolio_rebalance(db: Session, portfolio_id: int):
    # Get the suggestion first
    suggestion = calculate_rebalance_suggestion(db, portfolio_id)
    existing_portfolio = read_portfolio(db, portfolio_id)
    
    # Create portfolio update object
    portfolio_update = PortfolioUpdate(
        user_id=existing_portfolio.user_id,
        composition=suggestion.suggested_composition,
        current_value=existing_portfolio.current_value
    )
    
    # Update the portfolio with the optimized composition
    updated_portfolio = update_portfolio(db, portfolio_id, portfolio_update)
    
    return updated_portfolio