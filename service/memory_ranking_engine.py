"""
Memory Ranking Engine
BUILD-70H

Rank memories by relevance.
"""

def score_memory(
    keyword,
    memory,
):

    keyword = keyword.lower()

    score = 0

    title = (
        memory.get(
            "title",
            ""
        )
        .lower()
    )

    content = (
        memory.get(
            "content",
            ""
        )
        .lower()
    )

    if keyword in title:

        score += 10

    score += content.count(
        keyword
    )

    return score


def rank_memories(
    keyword,
    memories,
):

    scored = []

    for memory in memories:

        score = score_memory(
            keyword,
            memory,
        )

        scored.append(
            (
                score,
                memory,
            )
        )

    scored.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return scored