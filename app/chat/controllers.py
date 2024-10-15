# app/chat/controllers.py
import openai
from app.chat.schemas import ChatRequest, ChatResponse

# Initialize OpenAI API
openai.api_key = "your_openai_api_key"

def send_message_to_ai(message: str, context: dict) -> str:
    # You can customize the prompt based on the context if needed
    prompt = f"Context: {context}\nUser: {message}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def handle_chat_request(chat_request: ChatRequest) -> ChatResponse:
    response = send_message_to_ai(chat_request.message, chat_request.context)
    return ChatResponse(response=response)
