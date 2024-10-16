# app/rewards/schemas.py
from pydantic import BaseModel

class RewardBase(BaseModel):
    nft_id: int
    reward_type: str
    details: dict

class RewardCreate(RewardBase):
    pass

class RewardUpdate(RewardBase):
    pass

class RewardResponse(RewardBase):
    reward_id: int

    class Config:
        orm_mode = True
