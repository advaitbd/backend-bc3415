from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.common.database import SessionLocal
from app.auth.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def register_user(username: str, password: str):
    hashed_password = pwd_context.hash(password)
    user = User(username=username, hashed_password=hashed_password)
    async with SessionLocal() as session:
        session.add(user)
        await session.commit()
        await session.refresh(user)
    return user

async def login_user(username: str, password: str):
    # Logic for verifying user and generating a token
    pass
