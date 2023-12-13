from pydantic import Field
from typing import Optional
from .youtube_request import Part, Filter, OptionalParameters
from datetime import datetime


class SubscriptionPart(Part):
    part: list[str] = Field(default=['contentDetails', 'id', 'snippet', 'subscriberSnippet'])


class SubscriptionFilter(Filter):
    channelId: Optional[str] = None
    mine: Optional[bool] = None
    id: Optional[bool] = None
    myRecentSubscribers: Optional[bool] = None
    mySubscribers: Optional[bool] = None


class SubscriptionOptionalParameters(OptionalParameters):
    forChannelId: Optional[str] = None
    order: Optional[str] = None
    pageToken: Optional[str] = None
    maxResults: Optional[int] = None
