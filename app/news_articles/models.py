# app/news_articles/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from app.common.database import Base
from datetime import datetime

class NewsArticle(Base):
    __tablename__ = "news_articles"

    article_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    source = Column(String)
    published_at = Column(DateTime)
    category = Column(String)
