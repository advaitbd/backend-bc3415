from pydantic import BaseModel
from datetime import datetime

class NewsArticle(BaseModel):
    id: int
    title: str
    url: str
    source: str
    published_at: datetime
    content: str
