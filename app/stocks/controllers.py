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
