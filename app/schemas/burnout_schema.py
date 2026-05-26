from pydantic import BaseModel
from typing import List

class JournalItem(BaseModel):

    day: int
    text: str

class WeeklyJournalRequest(BaseModel):

    journals: List[JournalItem]