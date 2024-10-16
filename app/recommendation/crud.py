# app/recommendation/crud.py
from sqlalchemy.orm import Session
from app.recommendation.models import StockRecommendation
from app.recommendation.schemas import StockRecommendationCreate, StockRecommendationUpdate

def get_recommendation(db: Session, recommendation_id: int):
    return db.query(StockRecommendation).filter(StockRecommendation.recommendation_id == recommendation_id).first()

def get_recommendations_by_user_id(db: Session, user_id: str):
    return db.query(StockRecommendation).filter(StockRecommendation.user_id == user_id).all()

def create_recommendation(db: Session, recommendation: StockRecommendationCreate):
    db_recommendation = StockRecommendation(**recommendation.dict())
    db.add(db_recommendation)
    db.commit()
    db.refresh(db_recommendation)
    return db_recommendation

def update_recommendation(db: Session, recommendation_id: int, recommendation: StockRecommendationUpdate):
    db_recommendation = get_recommendation(db, recommendation_id)
    if db_recommendation:
        for key, value in recommendation.dict().items():
            setattr(db_recommendation, key, value)
        db.commit()
        db.refresh(db_recommendation)
    return db_recommendation

def delete_recommendation(db: Session, recommendation_id: int):
    db_recommendation = get_recommendation(db, recommendation_id)
    if db_recommendation:
        db.delete(db_recommendation)
        db.commit()
    return db_recommendation
