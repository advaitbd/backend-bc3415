from fastapi import APIRouter

from .routes import router as portfolio_router

router = APIRouter()
router.include_router(portfolio_router, prefix = "/portfolio", tags = ["portfolio"])