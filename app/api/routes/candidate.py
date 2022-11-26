from typing import Any

from fastapi import APIRouter

router = APIRouter()
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from models import CandidateModel, CandidateOutModel
from services import create_candidate_service, get_candidates_list_service


@router.get(
    "/all-candidates",
    response_model=list[CandidateOutModel],
    name="candidates:list",
)
async def get_candidates_list() -> List[CandidateOutModel]:
    return await get_candidates_list_service()


@router.post(
    "/candidates",
    response_model=CandidateOutModel,
    name="candidates:create",
)
async def create_candidate(candidate: CandidateModel):
    return await create_candidate_service(candidate)
