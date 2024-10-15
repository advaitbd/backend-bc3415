# app/auth/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: str
    contact_info: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    user_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
