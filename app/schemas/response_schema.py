from pydantic import BaseModel

class ClassificationResponse(BaseModel):

    original_text: str

    translated_text: str

    cleaned_text: str

    label: str

    confidence: float