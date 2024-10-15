from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: str
    message: str
    context: str

class ChatResponse(BaseModel):
    response: str
