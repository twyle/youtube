from pydantic import BaseModel
from .activity_type import ActivityType
from .resource import Resource
from .snippet import BaseSnippet
from typing import Optional
from .content_details import BaseContentDetails
from .activity_type import ActivityType


class ActivitySnippet(BaseSnippet):
    channel_id: str
    channel_title: str
    type: str
    group_id: Optional[str] = None


class ActivityContentDetails(BaseModel):
    activity_type: ActivityType


class Activity(Resource):
    snippet: BaseSnippet
    content_details: ActivityContentDetails
