"""
BUILD-70H2

MEMORY DUPLICATE REPORT ENGINE
"""

from service.memory_service import (
    MemoryService,
)

from service.memory_dedup_validation import (
    find_duplicate_titles,
)


def build_report():

    memories = (
        MemoryService.get_all_memories()
    )

    duplicates = (
        find_duplicate_titles()
    )

    unique_titles = set()

    for memory in memories:

        title = memory.get(
            "title",
            ""
        )

        if title:

            unique_titles.add(
                title
            )

    report = {
        "total_memories": len(
            memories
        ),
        "unique_titles": len(
            unique_titles
        ),
        "duplicate_titles": len(
            duplicates
        ),
        "duplicates": duplicates,
    }

    return report


def print_report():

    report = build_report()

    print()

    print(
        "=" * 40
    )

    print(
        "MEMORY DUPLICATE REPORT"
    )

    print(
        "=" * 40
    )

    print()

    print(
        "TOTAL MEMORIES:",
        report[
            "total_memories"
        ]
    )

    print(
        "UNIQUE TITLES:",
        report[
            "unique_titles"
        ]
    )

    print(
        "DUPLICATE TITLES:",
        report[
            "duplicate_titles"
        ]
    )

    print()

    print(
        "TOP DUPLICATES"
    )

    print()

    items = sorted(
        report[
            "duplicates"
        ].items(),
        key=lambda x: x[1],
        reverse=True,
    )

    for title, count in items[:20]:

        print(
            f"{count} - {title}"
        )

    print()