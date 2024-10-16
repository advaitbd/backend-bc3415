# app/stocks/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.stocks.controllers import (
    create_new_stock,
    read_stock,
    update_existing_stock,
    delete_existing_stock,
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
def read_stock(stock_id: int, db: Session = Depends(get_db)):
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
