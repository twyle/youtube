from .base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Text
from typing import List
from sqlalchemy import ForeignKey


class CommentModel(Base):
    __tablename__ = "youtube_comment"
    
    comment_id: Mapped[str] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(Text())
    comment_author_name: Mapped[str] = mapped_column(String(250))
    comment_author_thumbnail: Mapped[str] = mapped_column(String(250))
        
    video_id: Mapped[str] = mapped_column(ForeignKey("youtube_video.video_id"))
    video: Mapped["VideoModel"] = relationship(back_populates="comments")
        
    def __repr__(self) -> str:
        return f"CommentModel(comment_id='{self.comment_id!r}', comment_text='{self.comment_text!r}')"