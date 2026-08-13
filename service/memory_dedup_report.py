from collections import Counter

from service.memory_service import (
    MemoryService,
)

def get_duplicate_report():

    memories = (
        MemoryService.get_all_memories()
    )

    titles = []

    for memory in memories:

        titles.append(
            memory.get(
                "title",
                ""
            )
        )

    counter = Counter(
        titles
    )

    result = []

    for title, count in counter.items():

        if count > 1:

            result.append(
                (
                    count,
                    title
                )
            )

    result.sort(
        reverse=True
    )

    return result


def print_duplicate_report():

    data = (
        get_duplicate_report()
    )

    print()

    print(
        "DUPLICATE REPORT"
    )

    print(
        "=" * 50
    )

    print()

    for count, title in data:

        print(
            title,
            "->",
            count
        )

    print()