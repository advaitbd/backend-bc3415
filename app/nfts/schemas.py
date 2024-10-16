# app/nfts/schemas.py
from pydantic import BaseModel
from datetime import datetime

class NFTBase(BaseModel):
    token_id: str
    owner_user_id: str
    metadata: dict

class NFTCreate(NFTBase):
    pass

class NFTUpdate(NFTBase):
    transferred_at: datetime | None

class NFTResponse(NFTBase):
    nft_id: int
    created_at: datetime
    transferred_at: datetime | None

    class Config:
        orm_mode = True
