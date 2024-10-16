# app/recommendation/schemas.py
from pydantic import BaseModel
from datetime import datetime

class StockRecommendationBase(BaseModel):
    user_id: str
    stock_id: int
    reasoning: str

class StockRecommendationCreate(StockRecommendationBase):
    pass

class StockRecommendationUpdate(StockRecommendationBase):
    pass

class StockRecommendationResponse(StockRecommendationBase):
    recommendation_id: int
    recommended_at: datetime

    class Config:
        orm_mode = True
