from ..resource import YouTubeResource
from typing import Any


class YouTubePlaylistItem(YouTubeResource):
    def __init__(self, youtube_client: Any) -> None:
        super().__init__(youtube_client)
