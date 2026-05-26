import os

from google import genai

from app.prompts.burnout_prompt import (
    SYSTEM_PROMPT
)

from app.utils.context_builder import (
    build_context
)

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

async def generate_motivation(results):

    client = get_genai_client()

    context = build_context(results)

    prompt = f"""
    {SYSTEM_PROMPT}

    {context}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text