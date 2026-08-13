from service.memory_service import (
    MemoryService,
)

from service.memory_duplicate_stats import (
    get_duplicate_stats,
)

from collections import Counter
def get_top_titles():

    MemoryService.get_all_memories()

    titles = []

    for memory in memories:

        titles.append(
            memory.get(
                "title",
                ""
            )
        )

    return Counter(
        titles
    ).most_common(10)
from pathlib import Path

LOG_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "duplicate_log.txt"
)


def count_blocked_duplicates():

    if not LOG_FILE.exists():
        return 0

    text = LOG_FILE.read_text(
        encoding="utf-8"
    )

    return text.count(
        "ACTION: DUPLICATE_BLOCKED"
    )
def print_dashboard():

    stats = (
        get_duplicate_stats()
    )

    print()

    print(
        "=" * 50
    )

    print(
        "MEMORY DASHBOARD"
    )

    print(
        "=" * 50
    )

    print()

    print(
        "TOTAL:",
        stats["total_records"]
    )

    print(
        "UNIQUE:",
        stats["unique_records"]
    )

    print(
        "DUPLICATES:",
        stats["duplicate_records"]
    )

    print(
        "SAVING:",
        str(
            stats[
                "saving_percent"
            ]
        ) + "%"
    )

    print()

    print(
        "BLOCKED:",
        count_blocked_duplicates()
    )

    print()

    print(
        "TOP DUPLICATE TITLES"
    )

    print()

    for title, count in get_top_titles():

        if count > 1:

            print(
                title,
                ":",
                count
            )