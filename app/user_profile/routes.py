# app/user_profile/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.user_profile.crud import get_user_profile, get_user_profile_by_user_id, create_user_profile, update_user_profile, delete_user_profile
from app.user_profile.schemas import UserProfileCreate, UserProfileUpdate, UserProfileResponse
from app.common.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/user_profiles/", response_model=UserProfileResponse)
def create_new_user_profile(profile: UserProfileCreate, db: Session = Depends(get_db)):
    db_profile = get_user_profile_by_user_id(db, user_id=profile.user_id)
    if db_profile:
        raise HTTPException(status_code=400, detail="User profile already exists")
    return create_user_profile(db=db, profile=profile)

@router.get("/user_profiles/{profile_id}", response_model=UserProfileResponse)
def read_user_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = get_user_profile(db, profile_id=profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="User profile not found")
    return db_profile

@router.put("/user_profiles/{profile_id}", response_model=UserProfileResponse)
def update_existing_user_profile(profile_id: int, profile: UserProfileUpdate, db: Session = Depends(get_db)):
    db_profile = update_user_profile(db=db, profile_id=profile_id, profile=profile)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="User profile not found")
    return db_profile

@router.delete("/user_profiles/{profile_id}", response_model=UserProfileResponse)
def delete_existing_user_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = delete_user_profile(db=db, profile_id=profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="User profile not found")
    return db_profile
