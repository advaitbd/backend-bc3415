# app/recommendation/controllers.py
from sqlalchemy.orm import Session
from app.recommendation.crud import (
    get_recommendation,
    get_recommendations_by_user_id,
    create_recommendation,
    update_recommendation,
    delete_recommendation,
)
from app.recommendation.schemas import StockRecommendationCreate, StockRecommendationUpdate

def create_new_recommendation(db: Session, recommendation: StockRecommendationCreate):
    return create_recommendation(db=db, recommendation=recommendation)

def read_recommendation_by_id(db: Session, recommendation_id: int):
    db_recommendation = get_recommendation(db, recommendation_id=recommendation_id)
    if db_recommendation is None:
        raise ValueError("Recommendation not found")
    return db_recommendation

def read_recommendations_by_user_id(db: Session, user_id: str):
    return get_recommendations_by_user_id(db, user_id=user_id)

def update_existing_recommendation(db: Session, recommendation_id: int, recommendation: StockRecommendationUpdate):
    db_recommendation = update_recommendation(db=db, recommendation_id=recommendation_id, recommendation=recommendation)
    if db_recommendation is None:
        raise ValueError("Recommendation not found")
    return db_recommendation

def delete_existing_recommendation(db: Session, recommendation_id: int):
    db_recommendation = delete_recommendation(db=db, recommendation_id=recommendation_id)
    if db_recommendation is None:
        raise ValueError("Recommendation not found")
    return db_recommendation
