from uuid import UUID

from pydantic import BaseModel


class UserModel(BaseModel):
    first_name: str
    last_name: str


class UserOutModel(BaseModel):
    uid: UUID
