from pydantic import BaseModel
from .snippet import BaseSnippet
from typing import Optional

class Resource(BaseModel):
    id: Optional[str] = None
    snippet: Optional[BaseSnippet] = None
