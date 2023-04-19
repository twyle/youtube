from ..search_type import YouTubeSearchType
from ..search_query import YouTubeSearchQuery
from ...resources.video.video_collection import YouTubeVideoCollection
from .find_video import FindVideo


class Search:
    def __init__(self, youtube_client, query_string, batch_size=10, region_code='us'):
        self.__youtube_client = youtube_client
        self.__batch_size = batch_size
        self.__region_code = region_code
        self.__type = YouTubeSearchType.VIDEO
        self.__query = YouTubeSearchQuery(query_string)
        self.__videos = YouTubeVideoCollection()
        self.__next_page_token = None
        
    def __get_query(self):
        return self.__query.query_string
        
    def __generate_search_params(self):
        search_params = dict(
            part='id',
            type=self.__type,
            q=self.__get_query(),
            maxResults=self.__batch_size,
            regionCode=self.__region_code
        ) 
        return search_params
    
    def __next__(self):
        search_params = self.__generate_search_params()
        if self.__next_page_token:
            search_params['pageToken'] = self.__next_page_token
        search_request = self.__youtube_client.search().list(
            **search_params
        )
        search_response = search_request.execute()
        videos = self.__parse_search_response(search_response)
        return videos
    
    def __parse_search_response(self, search_response):
        videos = []
        self.__previous_page_token = search_response.get('prevPageToken', '')
        self.__next_page_token = search_response.get('nextPageToken', '')
        video_results = search_response['items']
        for video_result in video_results:
            video_id = video_result['id']['videoId']
            youtube_video = FindVideo(self.__youtube_client).find_video(video_id)
            videos.append(youtube_video)
        self.__videos.add_videos(videos)
        return videos
        
    def __iter__(self):
        return self
    
    def get_videos(self):
        return self.__videos