# app/recommendation/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from app.common.database import Base
from datetime import datetime

class StockRecommendation(Base):
    __tablename__ = "recommendations"

    recommendation_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"), index=True)
    stock_id = Column(Integer, ForeignKey("stocks.stock_id"), index=True)
    recommended_at = Column(DateTime, default=datetime.utcnow)
    reasoning = Column(Text)

    user = relationship("User", back_populates="recommendations")
    stock = relationship("Stock", back_populates="recommendations")
