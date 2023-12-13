from pydantic import BaseModel, Field
from typing import Optional


class Part(BaseModel):
    pass

class Filter(BaseModel):
    id: Optional[list[str]] = Field(default_factory=list)

class OptionalParameters(BaseModel):
    pass


class YouTubeRequest(BaseModel):
    part: Part
    filter: Optional[Filter] = Field(default_factory=list)
    optional_parameters: Optional[OptionalParameters] = OptionalParameters()
