"""
Memory Query Engine
BUILD-69A

Search memories from memory_records.json
"""

from service.memory_service import (
    MemoryService,
)

from service.memory_keyword_engine import (
    has_keyword,
)

from service.memory_keyword_engine import (
    find_titles_by_keyword,
)

def search(keyword):

    memories = MemoryService.search_memory(
        keyword
    )

    results = []

    keyword = keyword.lower()

    for memory in memories:

        title = memory.get(
            "title",
            "",
        ).lower()

        content = memory.get(
            "content",
            "",
        ).lower()

        if (
            keyword in title
            or
            keyword in content
        ):

            results.append(
                memory
            )

    return results

def search_best(keyword):

    results = search(keyword)

    if not results:
        return None

    keyword = keyword.lower()

    if not has_keyword(
        keyword
    ):
        return None

    ranked = rank_memories(
        keyword,
        results,
    )

    return ranked[0][1]

def search_by_title(
    title,
):

    memories = MemoryService.search_memory(
        title
    )

    for memory in memories:

        if (
            memory.get(
                "title",
                ""
            )
            ==
            title
        ):

            return memory

    return None

def search_by_keyword_index(
    keyword,
):

    titles = find_titles_by_keyword(
        keyword
    )

    results = []

    for title in titles:

        memory = search_by_title(
            title
        )

        if memory:

            results.append(
                memory
            )

    return results

def score_memory(
    keyword,
    memory,
):

    keyword = keyword.lower()

    score = 0

    title = memory.get(
        "title",
        "",
    ).lower()

    content = memory.get(
        "content",
        "",
    ).lower()

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