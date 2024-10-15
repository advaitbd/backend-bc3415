from fastapi import APIRouter, Depends
from app.auth.controllers import login_user, register_user

router = APIRouter()

@router.post("/register")
async def register(username: str, password: str):
    return await register_user(username, password)

@router.post("/login")
async def login(username: str, password: str):
    return await login_user(username, password)
