from fastapi import APIRouter
from app.api.routes import ideas, trends, market_gap

router = APIRouter()

router.include_router(
    ideas.router,
    prefix="/ideas",
    tags=["Ideas"]
)

router.include_router(
    trends.router,
    prefix="/trends",
    tags=["Trends"]
)

router.include_router(
    market_gap.router,
    prefix="/market-gap",
    tags=["Market Gap"]
)
