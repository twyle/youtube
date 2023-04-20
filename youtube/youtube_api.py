"""The library entry point."""
from .oauth import YouTubeAPIAuth
from .search.channel import FindChannel
from .search.video import FindVideo, VideoSearch
from .exceptions import (
    AuthenticationException
)


class YouTube:
    """The main class fo interacting with youtube."""

    MAX_RESULTS = 10
    REGION_CODE = "us"

    def __init__(self):
        """Create a youtube instance."""
        self.__youtube_api_auth = YouTubeAPIAuth()
        self.__youtube_client = None

    def authenticate_from_client_secrets_file(
        self, client_secrets_file: str, credentials_path: str = ""
    ):
        """Authenticate from the secrets file."""
        self.__youtube_client = (
            self.__youtube_api_auth.authenticate_from_client_secrets_file(
                client_secrets_file, credentials_path
            )
        )
        return self.__youtube_client

    def authenticate_from_credentials(self, credentials_path: str):
        """Authenticate from credentials file."""
        self.__youtube_client = self.__youtube_api_auth.authenticate_from_credentials(
            credentials_path
        )
        return self.__youtube_client

    def generate_credentials(
        self, client_secrets_file: str, credentials_path: str = ""
    ):
        """Generate credentials from commandline."""
        self.__youtube_api_auth.generate_credentials(
            client_secrets_file, credentials_path
        )
        
    def get_youtube_client(self):
        return self.__youtube_client
        
    def find_channel_by_id(self, channel_id: str):
        """Find a YouTube channel by id."""
        if not self.__youtube_client:
            raise AuthenticationException('You have not authenticated this instance.')
        channel_finder = FindChannel(self.__youtube_client)
        youtube_channel = channel_finder.find_channel_by_id(channel_id)
        return youtube_channel
    
    def find_video_by_id(self, video_id: str):
        """Find a YouTube video by id."""
        if not self.__youtube_client:
            raise AuthenticationException('You have not authenticated this instance.')
        video_finder = FindVideo(self.__youtube_client)
        youtube_video = video_finder.find_video(video_id)
        return youtube_video
    
    def get_iterator(self, query_string: str):
        """Search for videos."""
        if not self.__youtube_client:
            raise AuthenticationException('You have not authenticated this instance.')
        video_search = VideoSearch(self.__youtube_client, query_string)
        search_iterator = video_search.get_iterator()
        return search_iterator 
    
    def get_search_client(self, query_string: str):
        if not self.__youtube_client:
            raise AuthenticationException('You have not authenticated this instance.')
        video_search = VideoSearch(self.__youtube_client, query_string)
        return video_search
        
