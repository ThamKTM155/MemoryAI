def summarize_memories(
    memories
):

    if not memories:
        return ""

    parts = []

    for memory in memories:

        content = memory.get(
            "content",
            ""
        )

        if content:

            parts.append(
                content.strip()
            )

    return "\n\n".join(
        parts
    )