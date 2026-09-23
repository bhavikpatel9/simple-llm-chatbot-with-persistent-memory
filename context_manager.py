from database import (
    get_summary,
    get_messages,
)


def build_context(conversation_id, limit=10):
    summary = get_summary(conversation_id) or ""

    # Get recent messages from database
    recent_messages = get_messages(
        conversation_id,
        limit=limit,
    )

    context = []

    # Include summary of older messages
    if summary:
        context.append({
            "role": "user",
            "content": (
                "Context from earlier conversation history "
                "(use as background, not as a new request):\n"
                f"{summary}"
            ),
        })

    # Include recent messages
    for role, content in recent_messages:
        context.append({
            "role": role,
            "content": content,
        })

    return context