# app/user_profile/schemas.py
from pydantic import BaseModel

class UserProfileBase(BaseModel):
    investment_preferences: str
    risk_tolerance: str
    budget: int
    financial_goals: str

class UserProfileCreate(UserProfileBase):
    user_id: str

class UserProfileUpdate(UserProfileBase):
    pass

class UserProfileResponse(UserProfileBase):
    profile_id: int
    user_id: str

    class Config:
        orm_mode = True
