# app/transactions/schemas.py
from pydantic import BaseModel
from datetime import datetime

class TransactionBase(BaseModel):
    user_id: str
    points: int
    transaction_type: str
    related_nft_id: int | None

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    transaction_id: int
    timestamp: datetime

    class Config:
        orm_mode = True
