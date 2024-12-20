# app/portfolios/crud.py
from sqlalchemy.orm import Session
from app.portfolios.models import Portfolio
from app.portfolios.schemas import PortfolioCreate, PortfolioUpdate

def get_portfolio(db: Session, portfolio_id: int):
    return db.query(Portfolio).filter(Portfolio.portfolio_id == portfolio_id).first()

def get_portfolios_by_user_id(db: Session, user_id: str):
    return db.query(Portfolio).filter(Portfolio.user_id == user_id).all()

def create_portfolio(db: Session, portfolio: PortfolioCreate):
    db_portfolio = Portfolio(**portfolio.dict())
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio

def update_portfolio(db: Session, portfolio_id: int, portfolio: PortfolioUpdate):
    db_portfolio = get_portfolio(db, portfolio_id)
    if db_portfolio:
        # Update the portfolio fields
        for key, value in portfolio.dict().items():
            setattr(db_portfolio, key, value)
        
        # Commit to get the updated_at value
        db.commit()
        db.refresh(db_portfolio)
        
        # If created_at is None, set it to the same value as updated_at
        if db_portfolio.created_at is None:
            db_portfolio.created_at = db_portfolio.updated_at
            db.commit()
            db.refresh(db_portfolio)
        
    return db_portfolio

def delete_portfolio(db: Session, portfolio_id: int):
    db_portfolio = get_portfolio(db, portfolio_id)
    if db_portfolio:
        db.delete(db_portfolio)
        db.commit()
    return db_portfolio
