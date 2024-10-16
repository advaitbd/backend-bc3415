# app/transactions/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.transactions.controllers import (
    create_new_transaction,
    read_transaction,
    read_transactions_by_user,
    update_existing_transaction,
    delete_existing_transaction,
)
from app.transactions.schemas import TransactionCreate, TransactionUpdate, TransactionResponse
from app.common.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transaction/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    try:
        return create_new_transaction(db, transaction)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/transaction/{transaction_id}", response_model=TransactionResponse)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    try:
        return read_transaction(db, transaction_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/transactions/user/{user_id}", response_model=list[TransactionResponse])
def read_transactions_by_user(user_id: str, db: Session = Depends(get_db)):
    return read_transactions_by_user(db, user_id)

@router.put("/transaction/{transaction_id}", response_model=TransactionResponse)
def update_transaction(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    try:
        return update_existing_transaction(db, transaction_id, transaction)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/transaction/{transaction_id}", response_model=TransactionResponse)
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    try:
        return delete_existing_transaction(db, transaction_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
