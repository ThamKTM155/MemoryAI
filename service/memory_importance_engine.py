"""
Memory Importance Engine
BUILD-69I
"""

def get_importance_score(
    memory,
):

    score = 0

    content = memory.get(
        "content",
        ""
    )

    title = memory.get(
        "title",
        ""
    )

    score += len(content)

    score += len(title) * 5

    return score

def rank_by_importance(
    memories,
):

    ranked = []

    for memory in memories:

        score = get_importance_score(
            memory
        )

        ranked.append(
            (
                score,
                memory
            )
        )

    ranked.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return ranked