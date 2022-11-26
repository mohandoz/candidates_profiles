from auth import auth_backend, current_active_user, fastapi_users
from db.user import UserDoc
from fastapi import APIRouter, Depends
from fastapi_users.authentication import BearerTransport
from models import UserCreate, UserRead

router = APIRouter()

bearer_transport = BearerTransport(tokenUrl="/v1/auth/jwt/login")


router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["users"]
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["users"],
)


@router.get("/user", response_model=UserRead, tags=["users"])
async def get_active_user(user: UserDoc = Depends(current_active_user)):
    return user
