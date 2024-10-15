from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: str
    message: str
    context: dict

class ChatResponse(BaseModel):
    response: str
