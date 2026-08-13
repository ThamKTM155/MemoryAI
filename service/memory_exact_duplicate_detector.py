from collections import defaultdict

from service.memory_service import (
    MemoryService,
)
def find_exact_duplicates():

    memories = (
        MemoryService.get_all_memories()
    )

    groups = defaultdict(
        list
    )

    for index, memory in enumerate(
        memories
    ):

        title = memory.get(
            "title",
            ""
        )

        content = memory.get(
            "content",
            ""
        )

        key = (
            title,
            content
        )

        groups[key].append(
            index
        )

    result = []

    for key, indexes in groups.items():

        if len(indexes) > 1:

            result.append(
                (
                    len(indexes),
                    key[0],
                    indexes
                )
            )

    result.sort(
        reverse=True
    )

    return result
def print_exact_duplicates():

    data = (
        find_exact_duplicates()
    )

    print()

    print(
        "EXACT DUPLICATES"
    )

    print(
        "=" * 50
    )

    print()

    for count, title, indexes in data:

        print()

        print(
            title
        )

        print(
            "COUNT:",
            count
        )

        print(
            "INDEXES:",
            indexes
        )

    print()
