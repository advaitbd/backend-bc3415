from fastapi import APIRouter
from .controller import RewardsController

router = APIRouter()

@router.get("/", response_model=list)
async def read_rewards():
    return RewardsController.get_rewards()
