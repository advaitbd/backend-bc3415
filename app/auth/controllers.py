from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.common.database import SessionLocal
from app.auth.models import User
from app.auth.crud import get_user_by_email, create_user
from app.auth.schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(user: UserCreate):
    with SessionLocal() as session:
        db_user = get_user_by_email(session, email=user.email)
        if db_user:
            raise ValueError("Email already registered")
        return create_user(session, user)

def login_user(email: str, password: str):
    with SessionLocal() as session:
        db_user = get_user_by_email(session, email=email)
        if not db_user or not pwd_context.verify(password, db_user.password_hash):
            raise ValueError("Invalid credentials")
        # Logic for generating a token can be added here
        return db_user
