from .comment_thread import YouTubeCommentThread
from ...search.channel.find_channel import FindChannel
from .video_stat import YouTubeVideoStats
from .video_details import YouTubeVideoDetails
from googleapiclient.errors import HttpError
import json
import csv


class YouTubeVideo:
    """A YouTube Video."""
    def __init__(self, video_details, youtube_client):
        self.__youtube_client = youtube_client
        self.__video_stats = self.__create_video_stats(video_details)
        self.__video_details = self.__create_video_details(video_details)
        self.__video_top_level_comments = self.__set_video_comments()
        self.__channel = self.__set_video_channel()
        
    def set_youtube_client(self, youtube_client):
        self.__youtube_client = youtube_client
        
    def get_video_stats_details(self):
        video_stats_details = dict()
        video_stats_details['details'] = self.get_video_details()
        video_stats_details['statistics'] = self.get_video_stats()
        return video_stats_details
    
    def __set_video_comments(self):
        try:
            youtube_commenthread = YouTubeCommentThread(self.get_video_id())
            video_top_level_comments = youtube_commenthread.get_video_comments(self.__youtube_client)
        except HttpError:
            return []
        return video_top_level_comments
    
    def __set_video_channel(self):
        find_channel = FindChannel(self.__youtube_client)
        video_channel = find_channel.find_channel_by_id(self.get_channel_id())
        return video_channel
    
    def get_video_comments(self):
        if not self.__video_top_level_comments:
            self.__set_video_comments()
        return self.__video_top_level_comments
    
    def get_video_channel(self):
        if not self.__channel:
            self.__set_video_channel()
        return self.__channel
        
    def __create_video_stats(self, video_details: dict):
        video_stats = YouTubeVideoStats(**video_details['statistics'])
        return video_stats
    
    def __create_video_details(self, video_details: dict):
        video_details = YouTubeVideoDetails(**video_details['details'])
        return video_details
        
    def get_video_stats(self):
        return self.__video_stats.get_video_stats()
    
    def get_video_details(self):
        return self.__video_details.get_video_details()
    
    def get_video_id(self):
        return self.__video_details.get_video_id()
    
    def get_video_title(self):
        return self.__video_details.get_video_title()
    
    def get_video_description(self):
        return self.__video_details.get_video_description()
    
    def get_video_tags(self):
        return self.__video_details.get_video_tags()
    
    def get_channel_id(self):
        return self.__video_details.get_channel_id()
    
    def get_channel_title(self):
        return self.__video_details.get_channel_title()
    
    def get_video_thumbnail(self):
        return self.__video_details.get_video_thumbnail()
    
    def get_video_channel_thumbnail(self):
        if not self.__channel:
            self.__set_video_channel()
        return self.__channel.get_channel_thumbnail()
    
    def to_dict(self):
        return {
            'video_id': self.get_video_id(),
            'video_title': self.get_video_title(),
            'video_description': self.get_video_description(),
            'video_thumbnail': self.get_video_thumbnail(),
            'video_tags': self.get_video_tags(),
            'channel_id': self.get_channel_id(),
            'channel_title': self.get_channel_title(),
            'channel_thumbnail': self.get_video_channel_thumbnail()
        }
        
    def to_json(self, file_path=''):
        if not file_path:
            file_path = f'{self.get_video_id()}.json'
        with open(file_path, 'w', encoding='utf-8') as f:
            video_dict = self.to_dict()
            json.dump(video_dict, f)
    
    def to_csv(self, file_path=''):
        if not file_path:
            file_path = f'{self.get_video_id()}.csv'
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            video_dict = self.to_dict()
            writer.writerow(list(video_dict.keys()))
            writer.writerow(list(video_dict.values()))
    
    def __str__(self):
        return f'{self.get_video_title()} from {self.get_channel_title()}'
    
    def __repr__(self) -> str:
        return f"YouTubeVideo(id={self.get_video_id()}, video_title={self.get_video_title()})"