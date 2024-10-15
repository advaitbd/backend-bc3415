from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.controllers import register_user, login_user
from app.auth.schemas import UserCreate, UserResponse
from app.common.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    try:
        return login_user(email, password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
