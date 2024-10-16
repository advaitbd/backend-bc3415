# app/portfolios/controllers.py
from sqlalchemy.orm import Session
from app.portfolios.crud import (
    get_portfolio,
    get_portfolios_by_user_id,
    create_portfolio,
    update_portfolio,
    delete_portfolio,
)
from app.portfolios.schemas import PortfolioCreate, PortfolioUpdate

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
