from pydantic import BaseModel, Field
from enum import Enum, auto
from datetime import datetime
from .thumbnail import Thumbnail
from .resource import Resource

class LiveBroadcastContent(Enum):
    Upcoming = auto()
    Live = auto()
    Null = auto()

class Search(Resource):
    resource_id: str
    resource_type: str
    published_at: datetime
    channel_id: str
    title: str
    description: str
    channel_title: str
    live_broadcast_content: str
    publish_time: str
    thumbnails: Thumbnail

    @property
    def url(self) -> str:
        return f'https://www.youtube.com/watch?v={self.resource_id}'
