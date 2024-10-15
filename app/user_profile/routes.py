# app/user_profile/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.user_profile.controllers import (
    create_new_user_profile,
    read_user_profile,
    update_existing_user_profile,
    delete_existing_user_profile,
)
from app.user_profile.schemas import UserProfileCreate, UserProfileUpdate, UserProfileResponse
from app.common.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/user_profile/", response_model=UserProfileResponse)
def create_profile(profile: UserProfileCreate, db: Session = Depends(get_db)):
    try:
        return create_new_user_profile(db, profile)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/user_profile/{profile_id}", response_model=UserProfileResponse)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    try:
        return read_user_profile(db, profile_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/user_profile/{profile_id}", response_model=UserProfileResponse)
def update_profile(profile_id: int, profile: UserProfileUpdate, db: Session = Depends(get_db)):
    try:
        return update_existing_user_profile(db, profile_id, profile)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/user_profile/{profile_id}", response_model=UserProfileResponse)
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    try:
        return delete_existing_user_profile(db, profile_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
