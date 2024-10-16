# app/news_articles/crud.py
from sqlalchemy.orm import Session
from app.news_articles.models import NewsArticle
from app.news_articles.schemas import NewsArticleCreate, NewsArticleUpdate

def get_news_article(db: Session, article_id: int):
    return db.query(NewsArticle).filter(NewsArticle.article_id == article_id).first()

def get_news_articles(db: Session):
    return db.query(NewsArticle).all()

def create_news_article(db: Session, article: NewsArticleCreate):
    db_article = NewsArticle(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def update_news_article(db: Session, article_id: int, article: NewsArticleUpdate):
    db_article = get_news_article(db, article_id)
    if db_article:
        for key, value in article.dict().items():
            setattr(db_article, key, value)
        db.commit()
        db.refresh(db_article)
    return db_article

def delete_news_article(db: Session, article_id: int):
    db_article = get_news_article(db, article_id)
    if db_article:
        db.delete(db_article)
        db.commit()
    return db_article
