from pydantic import BaseModel
from typing import Optional


class PageInfo(BaseModel):
    totalResults: Optional[int] = None
    resultsPerPage: int
