# app/user_profile/crud.py
from sqlalchemy.orm import Session
from app.user_profile.models import UserProfile
from app.user_profile.schemas import UserProfileCreate, UserProfileUpdate

def get_user_profile(db: Session, profile_id: int):
    return db.query(UserProfile).filter(UserProfile.profile_id == profile_id).first()

def get_user_profile_by_user_id(db: Session, user_id: str):
    return db.query(UserProfile).filter(UserProfile.user_id == user_id).first()

def create_user_profile(db: Session, profile: UserProfileCreate):
    db_profile = UserProfile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def update_user_profile(db: Session, profile_id: int, profile: UserProfileUpdate):
    db_profile = get_user_profile(db, profile_id)
    if db_profile:
        for key, value in profile.dict().items():
            setattr(db_profile, key, value)
        db.commit()
        db.refresh(db_profile)
    return db_profile

def delete_user_profile(db: Session, profile_id: int):
    db_profile = get_user_profile(db, profile_id)
    if db_profile:
        db.delete(db_profile)
        db.commit()
    return db_profile
