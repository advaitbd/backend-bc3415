# app/news_articles/schemas.py
from pydantic import BaseModel
from datetime import datetime

class NewsArticleBase(BaseModel):
    title: str
    content: str
    source: str
    published_at: datetime
    category: str

class NewsArticleCreate(NewsArticleBase):
    pass

class NewsArticleUpdate(NewsArticleBase):
    pass

class NewsArticleResponse(NewsArticleBase):
    article_id: int

    class Config:
        orm_mode = True
