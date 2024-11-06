# app/news_articles/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.news_articles.controllers import (
    create_new_news_article,
    read_news_article,
    read_all_news_articles,
    update_existing_news_article,
    delete_existing_news_article
)
from app.news_articles.schemas import NewsArticleCreate, NewsArticleUpdate, NewsArticleResponse
from app.common.database import SessionLocal
from typing import List, Optional
import requests
from pydantic import BaseModel

router = APIRouter()

class NewsArticleResponse(BaseModel):
    id: str
    title: str
    url: str
    site: str
    time: int
    favicon_url: str
    description: str
    tags: List[str]
    tickers: List[str]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/news_article/", response_model=NewsArticleResponse)
def create_news_article(article: NewsArticleCreate, db: Session = Depends(get_db)):
    try:
        return create_new_news_article(db, article)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/news_article/{article_id}", response_model=NewsArticleResponse)
def read_news_article_route(article_id: int, db: Session = Depends(get_db)):
    try:
        return read_news_article(db, article_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/news_articles/", response_model=list[NewsArticleResponse])
def read_all_news_articles_route():
    # Define the TickerTick API endpoint and parameters
    api_url = "https://api.tickertick.com/feed"
    query = "(or tt:aapl tt:amzn tt:goog)"  # Adjust tickers as needed
    num_articles = 10

    # Build the full URL with query parameters
    full_url = f"{api_url}?q={query}&n={num_articles}"

    try:
        # Fetch data from the TickerTick API
        response = requests.get(full_url)
        response.raise_for_status()  # Raise an error if the request fails

        # Extract 'stories' from the JSON response
        news_data = response.json().get("stories", [])

        # Return data formatted as NewsArticleResponse model
        return news_data

    except requests.exceptions.RequestException as e:
        # Return an error if the request fails
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/news_article/{article_id}", response_model=NewsArticleResponse)
def update_news_article(article_id: int, article: NewsArticleUpdate, db: Session = Depends(get_db)):
    try:
        return update_existing_news_article(db, article_id, article)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/news_article/{article_id}", response_model=NewsArticleResponse)
def delete_news_article(article_id: int, db: Session = Depends(get_db)):
    try:
        return delete_existing_news_article(db, article_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
