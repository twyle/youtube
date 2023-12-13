from pydantic import BaseModel, Field
from ...models.resource import Resource
from .common import PageInfo
from typing import Optional


class YouTubeResponse(BaseModel):
    kind: str
    etag: str
    pageInfo: PageInfo
    items: list[Resource] = Field(default_factory=list)
    nextPageToken: Optional[str] = ''
    prevPageToken: Optional[str] = ''
