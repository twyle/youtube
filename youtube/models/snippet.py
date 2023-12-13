from pydantic import BaseModel
from .thumbnail import Thumbnail
from .localized import Localized
from datetime import datetime


class BaseSnippet(BaseModel):
    title: str
    description: str
    thumbnails: Thumbnail
    published_at: datetime
