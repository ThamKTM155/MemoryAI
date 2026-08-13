"""
Memory Context Engine
BUILD-69H
"""
from service.memory_importance_engine import (
    rank_by_importance,
)
from service.memory_authority_engine import (
    rank_by_final_score,
)

from service.memory_usage_engine import (
    increase_usage,
)

def trim_memories(
    memories,
    limit=10,
):

    return memories[:limit]

def select_context_memories(
    memories,
    limit=10,
):

    unique = []

    seen = set()

    for memory in memories:

        title = memory.get(
            "title",
            ""
        )

        if title in seen:
            continue

        seen.add(
            title
        )

        unique.append(
            memory
        )

    ranked = rank_by_final_score(
        unique
    )

    selected = []

    for score, memory in ranked[:limit]:

        selected.append(
            memory
        )
    for memory in selected:

        increase_usage(
            memory.get(
                "title",
                ""
            )
        )
    return selected