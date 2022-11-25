from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, PositiveFloat, PositiveInt

CAREER_LEVELS_TYPES = Literal[
    "junior",
    "mid",
    "senior",
]
DEGREE_TYPES = Literal[
    "bachelor",
    "high school",
    "master",
]

GENDERS_TYPES = Literal[
    "male",
    "female",
    "not specific",
]


class CandidateModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    career_level: CAREER_LEVELS_TYPES
    job_major: str
    years_of_experience: PositiveInt
    degree_type: DEGREE_TYPES
    skills: list[str]
    nationality: str
    city: str
    salary: PositiveFloat
    gender: GENDERS_TYPES


class CandidateOutModel(CandidateModel):
    uid: UUID
