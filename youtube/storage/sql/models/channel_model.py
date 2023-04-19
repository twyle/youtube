from .base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Text
from typing import List


class ChannelModel(Base):
    __tablename__ = "youtube_channel"
    
    channel_id: Mapped[str] = mapped_column(primary_key=True)
    channel_name: Mapped[str] = mapped_column(String(250))
    channel_thumbnail: Mapped[str] = mapped_column(String(250))
        
    videos: Mapped[List["VideoModel"]] = relationship(
         back_populates="channel", cascade="all, delete-orphan")
        
    def __repr__(self) -> str:
        return f"ChannelModel(channel_id='{self.channel_id!r}', channel_name='{self.channel_name!r}')"
