from .video import YouTubeVideo
from ...storage.sql.database import Database
from elasticsearch import Elasticsearch
import json
import pandas as pd


class YouTubeVideoCollection:
    def __init__(self):
        self.__youtube_videos = []
        self.__es_client = None
        self.__database = None
        
    def get_youtube_videos(self):
        return self.__youtube_videos
    
    def add_video(self, video: YouTubeVideo):
        self.__youtube_videos.append(video)
        
    def add_videos(self, videos: list[YouTubeVideo]):
        for video in videos:
            self.__youtube_videos.append(video)
    
    def save_to_database(self, POSTGRES_HOST, POSTGRES_PORT, 
                        POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB):
        if not self.__database:
            self.__database = Database(POSTGRES_HOST, POSTGRES_PORT, 
                        POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)
        self.__database.save_to_database(self.get_youtube_videos())
    
    def save_to_elasticsearch(self, index_name, elastic_search_host):
        if not self.__es_client:
            self.__create_es_client(elastic_search_host)
        for video in self.__youtube_videos:
            video_details = video.to_dict()
            self.__es_client.index(index=index_name, document=video_details, id=video_details['video_id'])
        
    def __delete_index(self, index_name):
        self.__es_client.indices.delete(index=index_name, ignore=[400, 404])
        
    def __create_index(self, index_name):
        self.__es_client.indices.create(index = index_name)
    
    def __create_es_client(self, es_host):
        if not self.__es_client:
            self.__es_client = Elasticsearch(hosts=[es_host])
    
    def save_to_csv(self):
        pass
    
    def save_to_json(self, file=''):
        if not file:
            file = 'file.json'
        with open(file, 'w') as file_path:
            videos = [video.to_dict() for video in self.__youtube_videos]
            json.dump(videos, file_path)
    
    def to_pandas(self):
        videos = [video.to_dict() for video in self.__youtube_videos]
        video_ids = []
        video_titles = []
        video_descriptions = []
        video_thumbnails = []
        video_tags = []
        channel_ids = []
        channel_titles = []
        for video in videos:
            video_ids.append(video['video_id'])
            video_titles.append(video['video_title'])
            video_descriptions.append(video['video_description'])
            video_thumbnails.append(video['video_thumbnail'])
            video_tags.append(video['video_tags'])
            channel_ids.append(video['channel_id'])
            channel_titles.append(video['channel_title'])
        data = {
            'video_id': video_ids,
            'video_title': video_titles,
            'video_description': video_descriptions,
            'video_thumbnail': video_thumbnails,
            'video_tags': video_tags,
            'channel_id': channel_ids,
            'channel_title': channel_titles
        }

        df = pd.DataFrame(data)