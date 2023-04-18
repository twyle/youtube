"""The library entry point."""
from .oauth import YouTubeAPIAuth


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
