from pydantic import BaseModel

class ClassificationResponse(BaseModel):

    translated_text: str

    label: str