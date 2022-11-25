from uuid import UUID, uuid4

from beanie import Document
from fastapi_users.db import BeanieUserDatabase
from models import CandidateModel
from pydantic import Field
from pymongo import IndexModel


class CandidateDoc(Document, CandidateModel):
    uid: UUID = Field(default_factory=uuid4)

    class Settings:
        name = "candidates"

        indexes = [
            IndexModel("email", unique=True),
            IndexModel("uid", unique=True),
        ]


async def get_candidate_db():
    yield BeanieUserDatabase(CandidateDoc)
