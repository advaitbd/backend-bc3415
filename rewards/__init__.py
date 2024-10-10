from fastapi import APIRouter

from .routes import router as rewards_router

router = APIRouter()
router.include_router(rewards_router, prefix="/rewards", tags=["rewards"])