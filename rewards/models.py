from pydantic import BaseModel

class Reward(BaseModel):
    id: int
    title: str
    description: str
    image_url: str
