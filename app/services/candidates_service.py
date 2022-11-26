from db import CandidateDoc
from exceptions import DuplicteRecordException
from models import CandidateModel, CandidateOutModel
from pydantic import parse_obj_as
from pymongo.errors import DuplicateKeyError


async def create_candidate_service(candidate: CandidateModel):
    try:
        candidate = CandidateDoc(**candidate.dict())
        await candidate.create()
    except DuplicateKeyError as e:
        raise DuplicteRecordException() from e

    return candidate


async def get_candidates_list_service():
    candidates = await CandidateDoc.find_all().to_list()
    return parse_obj_as(list[CandidateOutModel], candidates)
