"""
Memory Answer Engine
BUILD-69C1

Create answers from memories.
"""

from service.memory_query_engine import (
    search,
)

from service.memory_query_engine import (
    search_by_keyword_index,
    rank_memories,
)

from service.memory_summary_engine import (
    summarize_memories,
)
from service.memory_graph_engine import (
    get_related_memories,
)

from service.memory_context_engine import (
    select_context_memories,
)

def answer(question):

    memories = search(
        question
    )

    if not memories:

        return "Không tìm thấy ký ức"

    parts = []

    for memory in memories[:3]:

        content = memory.get(
            "content",
            ""
        ).strip()

        if content:

            parts.append(
                content
            )

    return "\n\n----------------\n\n".join(
        parts
    )

def get_top_memories(
    keyword,
    limit=3,
):

    results = search_by_keyword_index(
        keyword
    )

    if not results:

        return []

    ranked = rank_memories(
        keyword,
        results,
    )

    memories = []

    for score, memory in ranked[:limit]:

        memories.append(
            memory
        )

    return memories

def build_answer(
    keyword,
    limit=3,
):

    memories = get_top_memories(
        keyword,
        limit,
    )

    if not memories:

        return "Không tìm thấy ký ức"

    expanded = list(
        memories
    )

    for memory in memories:

        title = memory.get(
            "title",
            ""
        )

        related = get_related_memories(
            title
        )

        expanded.extend(
            related
        )

    unique = []

    seen = set()

    for memory in expanded:

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

    memories = select_context_memories(
        memories,
        limit=10,
    )

    return summarize_memories(
        memories
    )