from service.memory_service import (
    MemoryService,
)

from service.memory_graph_engine import (
    get_related_titles,
)

def count_common_words(
    text1,
    text2,
):

    words1 = set(
        text1.lower().split()
    )

    words2 = set(
        text2.lower().split()
    )

    return len(
        words1.intersection(
            words2
        )
    )

def get_best_recommendation(
    title,
):

    memories = MemoryService.get_all_memories()

    current = None

    for memory in memories:

        if memory.get(
            "title"
        ) == title:

            current = memory

            break

    if not current:

        return None

    current_text = (
        current.get(
            "content",
            ""
        )
    )

    best_score = 0

    best_title = None

    for memory in memories:

        other_title = memory.get(
            "title",
            ""
        )

        if other_title == title:

            continue

        score = count_common_words(
            current_text,
            memory.get(
                "content",
                ""
            )
        )

        if score > best_score:

            best_score = score

            best_title = other_title

    return (
        best_title,
        best_score
    )

def get_top_recommendations(
    title,
    limit=5,
):

    memories = MemoryService.get_all_memories()

    current = None

    for memory in memories:

        if memory.get(
            "title"
        ) == title:

            current = memory

            break

    if not current:

        return []

    current_text = current.get(
        "content",
        ""
    )

    results = []
    seen = set()
    for memory in memories:

        other_title = memory.get(
            "title",
            ""
        )

        if other_title in seen:
            continue

        seen.add(
            other_title
        )

        if other_title == title:

            continue

        score = count_common_words(
            current_text,
            memory.get(
                "content",
                ""
            )
        )

        results.append(
            (
                score,
                other_title
            )
        )

    results.sort(
        reverse=True
    )

    return results[:limit]