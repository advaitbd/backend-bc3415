# app/user_profile/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.common.database import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"

    profile_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"), unique=True, index=True)
    investment_preferences = Column(String)
    risk_tolerance = Column(String)
    budget = Column(Integer)
    financial_goals = Column(String)

    user = relationship("User", back_populates="profile")
