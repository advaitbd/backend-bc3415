# app/chat/controllers.py
from app.chat.schemas import ChatRequest, ChatResponse
from openai import OpenAI
from app.common.config import settings
import logging


client = OpenAI(api_key=settings.OPENAI_API_KEY)

def send_message_to_ai(message: str, context: str) -> str:
    # You can customize the prompt based on the context if needed
    messages = [
        {"role": "system", "content": f"Context: You are a financial advisor and are providing guidance about this article: {context}"},
        {"role": "user", "content": message}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    logging.info(response)

    return response.choices[0].message.content

def handle_chat_request(chat_request: ChatRequest) -> ChatResponse:
    response = send_message_to_ai(chat_request.message, chat_request.context)
    return ChatResponse(response=response)
