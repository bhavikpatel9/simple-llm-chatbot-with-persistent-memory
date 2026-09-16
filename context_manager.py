def build_context(
    client,
    model,
    messages,
    max_input_tokens=4000
):
    selected_messages = []

    for role, content in reversed(messages):

        candidate = [
            (role, content)
        ] + selected_messages

        # Convert candidate history to text
        context_text = ""

        for msg_role, msg_content in candidate:
            context_text += (
                f"{msg_role}: {msg_content}\n"
            )

        # Count tokens using Gemini
        result = client.models.count_tokens(
            model=model,
            contents=context_text
        )
        print("result total tokens:", result.total_tokens)

        if result.total_tokens > max_input_tokens:
            break

        selected_messages = candidate

    return [
        {
            "role": role,
            "content": content
        }
        for role, content in selected_messages
    ]