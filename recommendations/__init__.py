from fastapi import APIRouter

from .routes import router as recommendations_router

router = APIRouter()
router.include_router(recommendations_router, prefix = "/recommendations", tags = ["recommendations"])