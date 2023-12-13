from pydantic import BaseModel
from typing import Optional


class ThumbnailResolution(BaseModel):
    url: str
    width: int
    height: int

class Thumbnail(BaseModel):
    default: Optional[ThumbnailResolution] = None
    medium: Optional[ThumbnailResolution] = None
    high: Optional[ThumbnailResolution] = None
    standard: Optional[ThumbnailResolution] = None
    maxres: Optional[ThumbnailResolution] = None
