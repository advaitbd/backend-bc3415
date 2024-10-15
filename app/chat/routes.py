# app/chat/routes.py
from fastapi import APIRouter
from app.chat.schemas import ChatRequest, ChatResponse
from app.chat.controllers import handle_chat_request

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(chat_request: ChatRequest):
    return handle_chat_request(chat_request)
