# app/stocks/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.stocks.controllers import (
    create_new_stock,
    read_stock,
    update_existing_stock,
    delete_existing_stock,
    get_historical_prices,
    forecast_future_prices,
)
from app.stocks.schemas import StockCreate, StockUpdate, StockResponse
from app.common.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/stock/", response_model=StockResponse)
def create_stock(stock: StockCreate, db: Session = Depends(get_db)):
    try:
        return create_new_stock(db, stock)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/stock/{stock_id}", response_model=StockResponse)
def read_stock_route(stock_id: int, db: Session = Depends(get_db)):
    try:
        return read_stock(db, stock_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/stock/{stock_id}", response_model=StockResponse)
def update_stock(stock_id: int, stock: StockUpdate, db: Session = Depends(get_db)):
    try:
        return update_existing_stock(db, stock_id, stock)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/stock/{stock_id}", response_model=StockResponse)
def delete_stock(stock_id: int, db: Session = Depends(get_db)):
    try:
        return delete_existing_stock(db, stock_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/stock/{ticker}/prices", response_model=dict)
def get_prices(ticker: str, db: Session = Depends(get_db)):
    try:
        return get_historical_prices(ticker)
    except HTTPException as e:
        raise e

@router.get("/stock/{ticker}/forecast", response_model=dict)
def get_forecast(ticker: str, days_ahead: int, db: Session = Depends(get_db)):
    try:
        return forecast_future_prices(ticker, days_ahead)
    except HTTPException as e:
        raise e

# - endpoint for prices over the past 7 days, based on ticker
# - forecast for next x days