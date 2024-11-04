# app/user_profile/controllers.py
from sqlalchemy.orm import Session
from app.user_profile.crud import (
    get_user_profile,
    get_user_profile_by_user_id,
    create_user_profile,
    update_user_profile,
    delete_user_profile,
)
from app.user_profile.schemas import UserProfileCreate, UserProfileUpdate

def create_new_user_profile(db: Session, profile: UserProfileCreate):
    db_profile = get_user_profile_by_user_id(db, user_id=profile.user_id)
    if db_profile:
        raise ValueError("User profile already exists")
    return create_user_profile(db=db, profile=profile)

def read_user_profile(db: Session, profile_id: int):
    db_profile = get_user_profile(db, profile_id=profile_id)
    if db_profile is None:
        raise ValueError("User profile not found")
    return db_profile

def read_user_profile_by_user_id(db: Session, user_id: str):
    db_profile = get_user_profile_by_user_id(db, user_id=user_id)
    if db_profile is None:
        raise ValueError("User profile not found")
    return db_profile

def update_existing_user_profile(db: Session, profile_id: int, profile: UserProfileUpdate):
    db_profile = update_user_profile(db=db, profile_id=profile_id, profile=profile)
    if db_profile is None:
        raise ValueError("User profile not found")
    return db_profile

def delete_existing_user_profile(db: Session, profile_id: int):
    db_profile = delete_user_profile(db=db, profile_id=profile_id)
    if db_profile is None:
        raise ValueError("User profile not found")
    return db_profile
