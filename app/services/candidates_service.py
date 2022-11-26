import io
from itertools import product

import pandas as pd
from db import CandidateDoc
from exceptions import DuplicteRecordException
from fastapi.responses import StreamingResponse
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


async def generate_candidates_report():
    candidates = await CandidateDoc.find_all().to_list()
    if not candidates:
        return []

    csv_col = [value[0] for value in candidates[0]]

    # super bad i know there must be a better way, can't find any api
    # to do so in the docs
    data = []
    for candidate in candidates:
        values = [value[1] for value in candidate]
        data.append(values)

    df = pd.DataFrame.from_records(data=data, columns=csv_col)
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=candidates.csv"
    return response
