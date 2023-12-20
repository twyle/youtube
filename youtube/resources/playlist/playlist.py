from typing import Any

from ...schemas import YouTubeRequest
from ..resource import YouTubeResource


class YouTubePlaylist(YouTubeResource):
    def __init__(self, youtube_client: Any) -> None:
        super().__init__(youtube_client)
        self.my_playlists_schema: YouTubeRequest = None
        self.my_playlists_nxt_page_tkn: str = None
