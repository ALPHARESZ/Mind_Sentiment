def build_context(results):

    context = (
        "Weekly Journaling Analysis:\n\n"
    )

    for item in results:

        context += (
            f"Day {item['day']} "
            f"({item['label']}): "
            f"{item['translated_text']}\n"
        )

    return context