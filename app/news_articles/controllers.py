# app/news_articles/controllers.py
from sqlalchemy.orm import Session
from app.news_articles.crud import (
    get_news_article,
    get_news_articles,
    create_news_article,
    update_news_article,
    delete_news_article,
)
from app.news_articles.schemas import NewsArticleCreate, NewsArticleUpdate

def create_new_news_article(db: Session, article: NewsArticleCreate):
    return create_news_article(db=db, article=article)

def read_news_article(db: Session, article_id: int):
    db_article = get_news_article(db, article_id=article_id)
    if db_article is None:
        raise ValueError("News article not found")
    return db_article

def read_all_news_articles(db: Session):
    return get_news_articles(db)

def update_existing_news_article(db: Session, article_id: int, article: NewsArticleUpdate):
    db_article = update_news_article(db=db, article_id=article_id, article=article)
    if db_article is None:
        raise ValueError("News article not found")
    return db_article

def delete_existing_news_article(db: Session, article_id: int):
    db_article = delete_news_article(db=db, article_id=article_id)
    if db_article is None:
        raise ValueError("News article not found")
    return db_article
