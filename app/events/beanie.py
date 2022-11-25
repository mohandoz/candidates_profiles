from beanie import init_beanie
from db import CandidateDoc, UserDoc, db


async def init_db():
    await init_beanie(
        database=db,
        document_models=[
            UserDoc,
            CandidateDoc,
        ],
    )
