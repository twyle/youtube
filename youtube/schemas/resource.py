from pydantic import BaseModel, Field
from .resource_schema import Resource
from .common import PageInfo
from typing import Optional


class Part(BaseModel):
    pass

class Filter(BaseModel):
    pass

class OptionalParameters(BaseModel):
    pass

class RequestSchema(BaseModel):
    part: Part
    filter: Optional[Filter] = Filter()
    optional_parameters: Optional[OptionalParameters] = OptionalParameters()

class YouTubeResponse(BaseModel):
    kind: str
    etag: str
    pageInfo: PageInfo
    items: list[Resource] = Field(default_factory=list)
    nextPageToken: Optional[str] = ''
    prevPageToken: Optional[str] = ''
