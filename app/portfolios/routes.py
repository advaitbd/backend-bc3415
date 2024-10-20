# app/portfolios/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.portfolios.controllers import (
    create_new_portfolio,
    read_portfolio,
    read_portfolios_by_user,
    update_existing_portfolio,
    delete_existing_portfolio,
)
from app.portfolios.schemas import PortfolioCreate, PortfolioUpdate, PortfolioResponse
from app.common.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/portfolio/", response_model=PortfolioResponse)
def create_portfolio(portfolio: PortfolioCreate, db: Session = Depends(get_db)):
    try:
        return create_new_portfolio(db, portfolio)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/portfolio/{portfolio_id}", response_model=PortfolioResponse)
def read_portfolio_route(portfolio_id: int, db: Session = Depends(get_db)):
    try:
        return read_portfolio(db, portfolio_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/portfolios/user/{user_id}", response_model=list[PortfolioResponse])
def read_portfolios_by_user_route(user_id: str, db: Session = Depends(get_db)):
    return read_portfolios_by_user(db, user_id)

@router.put("/portfolio/{portfolio_id}", response_model=PortfolioResponse)
def update_portfolio(portfolio_id: int, portfolio: PortfolioUpdate, db: Session = Depends(get_db)):
    try:
        return update_existing_portfolio(db, portfolio_id, portfolio)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/portfolio/{portfolio_id}", response_model=PortfolioResponse)
def delete_portfolio(portfolio_id: int, db: Session = Depends(get_db)):
    try:
        return delete_existing_portfolio(db, portfolio_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
