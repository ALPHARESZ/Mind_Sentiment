from fastapi import APIRouter

from app.schemas.burnout_schema import (
    WeeklyJournalRequest
)

from app.services.burnout_service import (
    analyze_weekly_journals
)

router = APIRouter()

@router.post("/analyze-weekly-journal")
async def analyze_weekly_journal(
    request: WeeklyJournalRequest
):

    result = await analyze_weekly_journals(
        request.journals
    )

    return result