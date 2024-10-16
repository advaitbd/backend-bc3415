# app/stocks/schemas.py
from pydantic import BaseModel

class StockBase(BaseModel):
    ticker: str
    name: str
    sector: str
    industry: str
    fundamental_data: dict
    technical_data: dict

class StockCreate(StockBase):
    pass

class StockUpdate(StockBase):
    pass

class StockResponse(StockBase):
    stock_id: int

    class Config:
        orm_mode = True
