from typing import Any

from fastapi import APIRouter

router = APIRouter()
from typing import List

from auth import auth_backend, current_active_user, fastapi_users
from db import UserDoc
from fastapi import APIRouter, Depends, HTTPException
from models import CandidateModel, CandidateOutModel
from services import create_candidate_service, get_candidates_list_service


@router.get(
    "/all-candidates",
    response_model=list[CandidateOutModel],
    name="candidates:list",
)
async def get_candidates_list(
    user: UserDoc = Depends(current_active_user),
) -> List[CandidateOutModel]:
    return await get_candidates_list_service()


@router.post(
    "/candidates",
    response_model=CandidateOutModel,
    name="candidates:create",
    status_code=201,
)
async def create_candidate(
    candidate: CandidateModel, user: UserDoc = Depends(current_active_user)
):
    return await create_candidate_service(candidate)
