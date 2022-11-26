from typing import Any, Dict, Optional, Sequence, Type

from fastapi import HTTPException


class DuplicteRecordException(HTTPException):
    def __init__(
        self,
        detail: Any = "duplicate record",
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(status_code=409, detail=detail, headers=headers)
