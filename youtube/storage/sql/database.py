from .models import (
    Base, ChannelModel, CommentModel, VideoModel
)
from sqlalchemy import create_engine
from ...resources.video import YouTubeVideo
from ...resources.video.comment import YouTubeComment
from ...resources.video.comment_thread import YouTubeCommentThread
from ...resources.channel import YouTubeChannel
from sqlalchemy.orm import Session
from sqlalchemy import exc
from sqlalchemy_utils import database_exists


class Database:
    def __init__(self, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, 
                          POSTGRES_PASSWORD, POSTGRES_DB):
        self.__POSTGRES_HOST = POSTGRES_HOST
        self.__POSTGRES_PORT = POSTGRES_PORT
        self.__POSTGRES_USER = POSTGRES_USER
        self.__POSTGRES_PASSWORD = POSTGRES_PASSWORD
        self.__POSTGRES_DB = POSTGRES_DB
        self.__db_connection_string = self.__create_db_conn_string()
        if not self.__check_if_database_exists():
            raise ValueError(f'The database {self.__db_connection_string} is not connectd!')
        self.__engine = create_engine(self.__db_connection_string, echo=True)
        self.__create_tables()
        
    def __create_tables(self):
        Base.metadata.create_all(self.__engine)
        
    def save_to_database(self, videos: list[YouTubeVideo]):
        self.save_channels_from_videos(videos)
        self.save_videos(videos)
        self.save_comments_from_videos(videos)
        
    def save_channels_from_videos(self, videos: list[YouTubeVideo]):
        with Session(self.__engine) as session:
            for video in videos:
                video_channel = video.get_video_channel()
                channel = ChannelModel(
                    channel_id=video_channel.get_channel_id(),
                    channel_name=video_channel.get_channel_title(),
                    channel_thumbnail=video_channel.get_channel_thumbnail()
                )
                try:
                    session.add(channel)
                    session.commit()
                except exc.IntegrityError:
                    session.rollback()
                        
    def save_channel_from_video(self, video: YouTubeVideo):
        pass
    
    def add_channel(self, channel: ChannelModel):
        pass

    def save_videos(self, videos: list[YouTubeVideo]):
        with Session(self.__engine) as session:
            for video in videos:
                video = VideoModel(
                    video_id=video.get_video_id(),
                    video_name=video.get_video_title(),
                    video_thumbnail=video.get_video_thumbnail(),
                    channel_id=video.get_channel_id()
                )
                try:
                    session.add(video)
                    session.commit()
                except exc.IntegrityError:
                    session.rollback()
                        
    def save_video(self, video: YouTubeVideo):
        pass
    
    def save_comments_from_videos(self, videos: list[YouTubeVideo]):    
        with Session(self.__engine) as session:
            for video in videos:
                for comment in video.get_video_comments():
                    video_comment = comment.get_comment()
                    cm = CommentModel(
                        comment_id=video_comment['id'],
                        comment_text=video_comment['textDisplay'],
                        comment_author_name=video_comment['authorDisplayName'],
                        comment_author_thumbnail=video_comment['authorProfileImageUrl'],
                        video_id=video.get_video_id()
                    )
                    try:
                        session.add(cm)
                        session.commit()
                    except exc.IntegrityError:
                        session.rollback()
                            
    def save_comments_from_video(self, video: YouTubeVideo):
        pass
    
    def save_coments(self, comments: list[YouTubeComment]):
        pass
    
    def save_coment(self, comment: YouTubeComment):
        pass
    
    def save_coment_thread(self, comment_thread: YouTubeCommentThread):
        pass
    
    def __create_db_conn_string(self) -> str:
        """Create the database connection string.

        Creates the database connection string for a given flask environment.

        Returns
        -------
        db_connection_string: str
            The database connection string
        """
        return f"postgresql://{self.__POSTGRES_USER}:{self.__POSTGRES_PASSWORD}@{self.__POSTGRES_HOST}:{self.__POSTGRES_PORT}/{self.__POSTGRES_DB}"


    def __check_if_database_exists(self) -> bool:
        """Check if database exists.

        Ensures that the database exists before starting the application.

        Attributes
        ----------
        db_connection: str
            The database URL

        Raises
        ------
        ValueError:
            If the db_connection_string is empty or is not a string.

        Returns
        -------
        db_exists: bool
            True if database exists or False if it does not
        """
        db_exists = database_exists(self.__db_connection_string)

        return db_exists