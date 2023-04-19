from ..utils.stat import Stat


class YouTubeVideoStats:
    def __init__(self, viewCount: int, likeCount: int, commentCount: int):
        self.__view_count = Stat(int(viewCount))
        self.__like_count = Stat(int(likeCount))
        self.__comment_count = Stat(int(commentCount))
        
    def get_video_stats(self):
        video_stats = {
            'view_count': self.__view_count.get_stat(),
            'like_count': self.__like_count.get_stat(),
            'comment_count': self.__comment_count.get_stat()
        }
        return video_stats
    
    def get_formatted_video_stats(self):
        video_stats = {
            'view_count': self.__view_count.get_formatted_stat(),
            'like_count': self.__like_count.get_formatted_stat(),
            'comment_count': self.__comment_count.get_formatted_stat()
        }
        return video_stats