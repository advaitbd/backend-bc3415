# app/news_articles/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.news_articles.controllers import (
    create_new_news_article,
    read_news_article,
    read_all_news_articles,
    update_existing_news_article,
    delete_existing_news_article,
)
from app.news_articles.schemas import NewsArticleCreate, NewsArticleUpdate, NewsArticleResponse
from app.common.database import SessionLocal

router = APIRouter()

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
def read_all_news_articles_route(db: Session = Depends(get_db)):
    return read_all_news_articles(db)

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
