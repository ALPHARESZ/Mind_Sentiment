from pydantic import BaseModel
from typing import List

class JournalItem(BaseModel):

    translated_text: str

    label: str


class WeeklyJournalRequest(BaseModel):

    journals: List[JournalItem]