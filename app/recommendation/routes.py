# app/recommendation/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.recommendation.controllers import (
    create_new_recommendation,
    read_recommendation_by_id,
    read_recommendations_by_user_id,
    update_existing_recommendation,
    delete_existing_recommendation,
)
from app.recommendation.schemas import StockRecommendationCreate, StockRecommendationUpdate, StockRecommendationResponse
from app.common.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/recommendation/", response_model=StockRecommendationResponse)
def create_recommendation(recommendation: StockRecommendationCreate, db: Session = Depends(get_db)):
    try:
        return create_new_recommendation(db, recommendation)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/recommendation/{recommendation_id}", response_model=StockRecommendationResponse)
def read_recommendation(recommendation_id: int, db: Session = Depends(get_db)):
    try:
        return read_recommendation_by_id(db, recommendation_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/recommendations/user/{user_id}", response_model=list[StockRecommendationResponse])
def read_recommendations_by_user(user_id: str, db: Session = Depends(get_db)):
    return read_recommendations_by_user_id(db, user_id)

@router.put("/recommendation/{recommendation_id}", response_model=StockRecommendationResponse)
def update_recommendation(recommendation_id: int, recommendation: StockRecommendationUpdate, db: Session = Depends(get_db)):
    try:
        return update_existing_recommendation(db, recommendation_id, recommendation)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/recommendation/{recommendation_id}", response_model=StockRecommendationResponse)
def delete_recommendation(recommendation_id: int, db: Session = Depends(get_db)):
    try:
        return delete_existing_recommendation(db, recommendation_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
