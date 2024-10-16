# app/transactions/controllers.py
from sqlalchemy.orm import Session
from app.transactions.crud import (
    get_transaction,
    get_transactions_by_user_id,
    create_transaction,
    update_transaction,
    delete_transaction,
)
from app.transactions.schemas import TransactionCreate, TransactionUpdate

def create_new_transaction(db: Session, transaction: TransactionCreate):
    return create_transaction(db=db, transaction=transaction)

def read_transaction(db: Session, transaction_id: int):
    db_transaction = get_transaction(db, transaction_id=transaction_id)
    if db_transaction is None:
        raise ValueError("Transaction not found")
    return db_transaction

def read_transactions_by_user(db: Session, user_id: str):
    return get_transactions_by_user_id(db, user_id=user_id)

def update_existing_transaction(db: Session, transaction_id: int, transaction: TransactionUpdate):
    db_transaction = update_transaction(db=db, transaction_id=transaction_id, transaction=transaction)
    if db_transaction is None:
        raise ValueError("Transaction not found")
    return db_transaction

def delete_existing_transaction(db: Session, transaction_id: int):
    db_transaction = delete_transaction(db=db, transaction_id=transaction_id)
    if db_transaction is None:
        raise ValueError("Transaction not found")
    return db_transaction
