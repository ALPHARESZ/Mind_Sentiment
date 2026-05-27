import os

from google import genai

from app.utils.context_builder import (
    build_context
)

from app.prompts.motivation_prompt import (
    SYSTEM_PROMPT as MOTIVATION_PROMPT
)

from app.prompts.support_prompt import (
    SYSTEM_PROMPT as SUPPORT_PROMPT
)

from app.prompts.adjustment_prompt import (
    SYSTEM_PROMPT as ADJUSTMENT_PROMPT
)

from app.prompts.congrats_prompt import (
    SYSTEM_PROMPT as CONGRATS_PROMPT
)

PROMPT_MAP = {
    "motivation": MOTIVATION_PROMPT,
    "support": SUPPORT_PROMPT,
    "adjustment": ADJUSTMENT_PROMPT,
    "congrats": CONGRATS_PROMPT
}

def get_genai_client():

    api_key = os.getenv(
        "GEN_AI_API_KEY"
    )

    if not api_key:

        raise ValueError(
            "GEN_AI_API_KEY not found"
        )

    return genai.Client(
        api_key=api_key
    )

async def generate_ai_response(
    results,
    prompt_mode,
    state
):

    client = get_genai_client()

    context = build_context(results)

    system_prompt = PROMPT_MAP[
        prompt_mode
    ]

    prompt = f"""
    {system_prompt}

    Emotional State:
    {state}

    Weekly Journaling:
    {context}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text