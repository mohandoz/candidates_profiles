from typing import Optional
from uuid import UUID, uuid4

from beanie import PydanticObjectId
from fastapi import Depends, Request
from fastapi_users import BaseUserManager
from fastapi_users.db import BaseOAuthAccount, BeanieBaseUser, BeanieUserDatabase
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
