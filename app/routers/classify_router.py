from fastapi import APIRouter

from app.schemas.classify_schema import (
    JournalRequest
)

from app.services.classification_service import (
    classify_journal
)

router = APIRouter()

@router.post("/classify")
async def classify(request: JournalRequest):

    result = classify_journal(
        request.text
    )

    return result