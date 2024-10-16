from sqlalchemy.orm import Session
from app.stocks.models import Stock
from app.stocks.schemas import StockCreate, StockUpdate

def get_stock(db: Session, stock_id: int):
    return db.query(Stock).filter(Stock.stock_id == stock_id).first()

def get_stock_by_ticker(db: Session, ticker: str):
    return db.query(Stock).filter(Stock.ticker == ticker).first()

def create_stock(db: Session, stock: StockCreate):
    db_stock = Stock(**stock.dict())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

def update_stock(db: Session, stock_id: int, stock: StockUpdate):
    db_stock = get_stock(db, stock_id)
    if db_stock:
        for key, value in stock.dict().items():
            setattr(db_stock, key, value)
        db.commit()
        db.refresh(db_stock)
    return db_stock

def delete_stock(db: Session, stock_id: int):
    db_stock = get_stock(db, stock_id)
    if db_stock:
        db.delete(db_stock)
        db.commit()
    return db_stock
