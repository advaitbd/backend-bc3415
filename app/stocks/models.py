# app/stocks/models.py
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship
from app.common.database import Base

class Stock(Base):
    __tablename__ = "stocks"

    stock_id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, unique=True, index=True)
    name = Column(String)
    sector = Column(String)
    industry = Column(String)
    fundamental_data = Column(JSON)
    technical_data = Column(JSON)

    recommendations = relationship("StockRecommendation", back_populates="stock")
