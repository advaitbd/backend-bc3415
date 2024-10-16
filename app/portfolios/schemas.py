# app/portfolios/schemas.py
from pydantic import BaseModel
from datetime import datetime

class PortfolioBase(BaseModel):
    user_id: str
    composition: dict
    current_value: int
    forecasted_value: int

class PortfolioCreate(PortfolioBase):
    pass

class PortfolioUpdate(PortfolioBase):
    pass

class PortfolioResponse(PortfolioBase):
    portfolio_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
