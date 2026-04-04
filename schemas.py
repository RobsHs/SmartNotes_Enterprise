from pydantic import BaseModel
from typing import List

class NoteCreate(BaseModel):
    title: str
    content: str
    tags: List[str]

class NoteResponse(NoteCreate):
    id: str
