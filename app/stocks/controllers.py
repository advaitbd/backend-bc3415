# app/stocks/controllers.py
from sqlalchemy.orm import Session
from app.stocks.crud import (
    get_stock,
    get_stock_by_ticker,
    create_stock,
    update_stock,
    delete_stock,
)
from app.stocks.schemas import StockCreate, StockUpdate
from fastapi import HTTPException
import yfinance as yf
from datetime import datetime, timedelta
from statsmodels.tsa.arima.model import ARIMA

def create_new_stock(db: Session, stock: StockCreate):
    db_stock = get_stock_by_ticker(db, ticker=stock.ticker)
    if db_stock:
        raise ValueError("Stock already exists")
    return create_stock(db=db, stock=stock)

def read_stock(db: Session, stock_id: int):
    db_stock = get_stock(db, stock_id=stock_id)
    if db_stock is None:
        raise ValueError("Stock not found")
    return db_stock

def update_existing_stock(db: Session, stock_id: int, stock: StockUpdate):
    db_stock = update_stock(db=db, stock_id=stock_id, stock=stock)
    if db_stock is None:
        raise ValueError("Stock not found")
    return db_stock

def delete_existing_stock(db: Session, stock_id: int):
    db_stock = delete_stock(db=db, stock_id=stock_id)
    if db_stock is None:
        raise ValueError("Stock not found")
    return db_stock

def get_historical_prices(ticker: str):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    if data.empty:
        raise HTTPException(status_code=404, detail="No data found for the given ticker")
    return data['Adj Close'].to_dict()

def forecast_future_prices(ticker: str, days_ahead: int):
    data = yf.download(ticker, period='1y')['Adj Close']
    if data.empty:
        raise HTTPException(status_code=404, detail="No data found for the given ticker")
    
    # Fit ARIMA model (you can optimize the order)
    model = ARIMA(data, order=(1, 0, 0))
    model_fit = model.fit()
    
    # Forecast future prices
    forecast = model_fit.forecast(steps=days_ahead)
    return forecast.to_dict()
