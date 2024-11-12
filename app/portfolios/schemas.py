# app/portfolios/schemas.py
from pydantic import BaseModel, validator
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
    @validator('created_at', 'updated_at', pre=True, always=True)
    def validate_datetime(cls, v):
        if v is None:
            raise ValueError("Datetime field cannot be None")
        return v