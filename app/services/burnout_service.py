from app.services.genai_service import (
    generate_ai_response
)

from app.utils.burnout_engine import (
    analyze_burnout
)

async def analyze_weekly_journals(
    journals
):

    labels = []

    results = []

    i = 0

    for journal in journals:
        i += 1
        label = journal.label.lower()

        labels.append(label)

        results.append({
            "day": i,
            "translated_text": journal.translated_text,
            "label": label
        })

    burnout_result = analyze_burnout(
        labels
    )

    ai_message = await generate_ai_response(
        results=results,
        prompt_mode=burnout_result[
            "prompt_mode"
        ],
        state=burnout_result[
            "state"
        ]
    )

    return {

        "state": burnout_result[
            "state"
        ],

        "message": ai_message
    }