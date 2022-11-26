from beanie import PydanticObjectId
from db.user import UserDoc, get_user_manager
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.db import BaseOAuthAccount


class OAuthAccount(BaseOAuthAccount):
    pass


bearer_transport = BearerTransport(tokenUrl="/api/v1/auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret="SECRET", lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[UserDoc, PydanticObjectId](
    get_user_manager, [auth_backend]
)


current_active_user = fastapi_users.current_user(active=True)
