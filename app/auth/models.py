# app/auth/models.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.common.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    name = Column(String)
    contact_info = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    profile = relationship("UserProfile", back_populates="user", uselist=False)
