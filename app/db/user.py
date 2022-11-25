from beanie import PydanticObjectId
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase
from models import UserModel
from pymongo import IndexModel


class UserDoc(BeanieBaseUser[PydanticObjectId], UserModel):
    UserModel

    class Settings:
        name = "user"

        indexes = [
            IndexModel("email", unique=True),
        ]


async def get_user_db():
    yield BeanieUserDatabase(UserDoc)
