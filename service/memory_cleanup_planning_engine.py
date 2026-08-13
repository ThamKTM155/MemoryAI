"""
BUILD-70H3

MEMORY CLEANUP PLANNING ENGINE
"""

from collections import defaultdict

from service.memory_service import (
    MemoryService,
)


def build_cleanup_plan():

    memories = (
        MemoryService.get_all_memories()
    )
    title_groups = defaultdict(
        list
    )

    for memory in memories:

        title = (
            memory.get(
                "title",
                ""
            )
            .strip()
        )

        title_groups[
            title
        ].append(
            memory
        )

    keep_count = 0
    review_count = 0

    review_items = []

    for title, items in (
        title_groups.items()
    ):

        if len(items) == 1:

            keep_count += 1

            continue

        review_count += len(
            items
        )

        review_items.append(
            (
                title,
                len(items)
            )
        )

    review_items.sort(
        key=lambda x: x[1],
        reverse=True,
    )

    return {
        "total_memories":
            len(memories),

        "unique_titles":
            len(title_groups),

        "keep_count":
            keep_count,

        "review_count":
            review_count,

        "review_items":
            review_items,
    }


def print_cleanup_plan():

    plan = (
        build_cleanup_plan()
    )

    print()

    print(
        "=" * 40
    )

    print(
        "MEMORY CLEANUP PLAN"
    )

    print(
        "=" * 40
    )

    print()

    print(
        "TOTAL MEMORIES:",
        plan[
            "total_memories"
        ]
    )

    print(
        "UNIQUE TITLES:",
        plan[
            "unique_titles"
        ]
    )

    print(
        "KEEP:",
        plan[
            "keep_count"
        ]
    )

    print(
        "REVIEW:",
        plan[
            "review_count"
        ]
    )

    print()

    print(
        "TOP REVIEW ITEMS"
    )

    print()

    for title, count in (
        plan[
            "review_items"
        ][:20]
    ):

        print(
            f"{count} - {title}"
        )

    print()