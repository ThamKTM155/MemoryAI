from service.memory_service import (
    MemoryService,
)

from service.memory_authority_engine import (
    get_final_score,
)
def get_top_memories(
    limit=10,
):

    all_memories = (
        MemoryService.get_all_memories()
    )

    unique = {}

    for memory in all_memories:

        title = memory.get(
            "title",
            ""
        )

        if title not in unique:

            unique[title] = memory

    memories = list(
        unique.values()
    )

    ranked = []

    for memory in memories:

        score = get_final_score(
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

    return ranked[:limit]
def print_top_memories(
    limit=10,
):

    ranked = get_top_memories(
        limit
    )

    print()

    print(
        "TOP MEMORIES"
    )

    print(
        "=" * 50
    )

    for index, (
        score,
        memory
    ) in enumerate(
        ranked,
        start=1
    ):

        print(
            f"{index}.",
            memory.get(
                "title",
                ""
            )
        )

        print(
            "   Final:",
            score
        )

        print()
