from .base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Text
from typing import List
from sqlalchemy import ForeignKey


class VideoModel(Base):
    __tablename__ = "youtube_video"
    
    video_id: Mapped[str] = mapped_column(primary_key=True)
    video_name: Mapped[str] = mapped_column(String(250))
    video_thumbnail: Mapped[str] = mapped_column(String(250))
        
    channel_id: Mapped[str] = mapped_column(ForeignKey("youtube_channel.channel_id"))
    channel: Mapped["ChannelModel"] = relationship(back_populates="videos")
        
    comments: Mapped[List["CommentModel"]] = relationship(
         back_populates="video", cascade="all, delete-orphan")
        
    def __repr__(self) -> str:
        return f"VideoModel(video_id='{self.video_id!r}', video_name='{self.video_name!r}')"