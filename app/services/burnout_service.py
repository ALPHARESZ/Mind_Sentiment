from app.services.classification_service import (
    classify_journal
)

from app.services.genai_service import (
    generate_motivation
)

NEGATIVE_LABELS = [
    "negative",
    "stress",
    "burnout",
    "sad"
]

async def analyze_weekly_journals(journals):

    results = []

    negative_count = 0

    for journal in journals:

        result = classify_journal(
            journal.text
        )

        item = {
            "day": journal.day,
            "original_text": journal.text,
            **result
        }

        results.append(item)

        if result["label"].lower() in NEGATIVE_LABELS:

            negative_count += 1

    burnout_detected = (
        negative_count >= 4
    )

    motivation = None

    if burnout_detected:

        motivation = await generate_motivation(
            results
        )

    return {
        "burnout_detected": burnout_detected,
        "negative_days": negative_count,
        "results": results,
        "motivation": motivation
    }