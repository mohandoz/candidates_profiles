from api.routes import candidate
from fastapi import APIRouter

router = APIRouter()
router.include_router(candidate.router, tags=["candidates"], prefix="/v1")
