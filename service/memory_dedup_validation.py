"""
BUILD-70H1

MEMORY DEDUP VALIDATION

Phát hiện dữ liệu trùng trong MemoryAI.
"""

from collections import Counter

from service.memory_service import (
    MemoryService,
)


def find_duplicate_titles():

    memories = (
        MemoryService.get_all_memories()
    )

    titles = []

    for memory in memories:

        title = (
            memory.get(
                "title",
                ""
            )
            .strip()
        )

        if title:

            titles.append(
                title
            )

    counter = Counter(
        titles
    )

    duplicates = {}

    for title, count in (
        counter.items()
    ):

        if count > 1:

            duplicates[
                title
            ] = count

    return duplicates


def print_duplicate_titles():

    duplicates = (
        find_duplicate_titles()
    )

    print()

    print(
        "DUPLICATE TITLES:"
    )

    print()

    if not duplicates:

        print(
            "NO DUPLICATES"
        )

        return

    for title, count in (
        sorted(
            duplicates.items(),
            key=lambda x: x[1],
            reverse=True,
        )
    ):

        print(
            f"{count} - {title}"
        )

    print()