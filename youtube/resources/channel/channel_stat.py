from ..utils.stat import Stat

class YouTubeChannelStats:
    def __init__(self, viewCount: int, subscriberCount: int, videoCount: int):
        self.__view_count = Stat(int(viewCount))
        self.__subscriber_count = Stat(int(subscriberCount))
        self.__video_count = Stat(int(videoCount))
        
    def get_channel_stats(self):
        video_stats = {
            'view_count': self.__view_count.get_stat(),
            'like_count': self.__subscriber_count.get_stat(),
            'video_count': self.__video_count.get_stat()
        }
        return video_stats
    
    def get_formatted_channel_stats(self):
        video_stats = {
            'view_count': self.__view_count.get_formatted_stat(),
            'subscriber_count': self.__subscriber_count.get_formatted_stat(),
            'video_count': self.__video_count.get_formatted_stat()
        }
        return video_stats