from api.routes import candidate, user
from fastapi import APIRouter

router = APIRouter()
router.include_router(candidate.router, tags=["candidates"], prefix="/v1")
router.include_router(user.router, tags=["users"], prefix="/v1")
