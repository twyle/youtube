from pydantic import BaseModel
from typing import Optional


class VideoReportAbuse(BaseModel):
    video_id: str
    reason_id: str
    secondary_reason_id: Optional[str] = None
    comments: Optional[str] = None
    language: Optional[str] = None
