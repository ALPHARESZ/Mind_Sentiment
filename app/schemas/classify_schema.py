from pydantic import BaseModel

class JournalRequest(BaseModel):

    content: str