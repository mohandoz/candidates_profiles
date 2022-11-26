from typing import Optional
from uuid import UUID, uuid4

from beanie import PydanticObjectId
from fastapi import Depends, Request
from fastapi_users import BaseUserManager
from fastapi_users.db import (
    BaseOAuthAccount,
    BeanieBaseUser,
    BeanieUserDatabase,
    ObjectIDIDMixin,
)
from pydantic import Field
from pymongo import IndexModel


class OAuthAccount(BaseOAuthAccount):
    pass


class UserDoc(BeanieBaseUser[PydanticObjectId]):
    uid: UUID = Field(default_factory=uuid4)
    oauth_accounts: list[OAuthAccount] = Field(default_factory=list)

    class Settings(BeanieBaseUser.Settings):
        name = "user"

        indexes = BeanieBaseUser.Settings.indexes + [IndexModel("uid", unique=True)]


async def get_user_db():
    yield BeanieUserDatabase(UserDoc)


class UserManager(ObjectIDIDMixin, BaseUserManager[UserDoc, PydanticObjectId]):
    async def on_after_register(self, user: UserDoc, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: UserDoc, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: UserDoc, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db: BeanieUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
