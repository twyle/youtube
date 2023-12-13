from pydantic import Field
from typing import Optional
from .youtube_request import Part, Filter, OptionalParameters


class ChannelPart(Part):
    part: list[str] = Field(default=['contentDetails', 'id','localizations',
        'snippet','statistics', 'status'])


class ChannelFilter(Filter):
    forUsername: Optional[str] = None
    id: Optional[list[str]] = Field(default_factory=list)
    managedByMe: Optional[str] = None
    mine: Optional[bool] = None


class ChannelOptionalParameters(OptionalParameters):
    h1: Optional[str] = None
    onBehalfOfContentOwner: Optional[str] = None
    pageToken: Optional[str] = None
    maxResults: Optional[int] = None
