from service.memory_exact_duplicate_detector import (
    find_exact_duplicates,
)

from service.memory_service import (
    MemoryService,
)

def get_duplicate_stats():

    memories = (
        MemoryService.get_all_memories()
    )

    duplicates = (
        find_exact_duplicates()
    )

    total_records = len(
        memories
    )

    duplicate_records = 0

    for count, _, _ in duplicates:

        duplicate_records += (
            count - 1
        )

    unique_records = (
        total_records
        - duplicate_records
    )

    saving_percent = round(
        duplicate_records
        * 100
        / total_records,
        2
    )

    return {
        "total_records":
            total_records,

        "duplicate_records":
            duplicate_records,

        "unique_records":
            unique_records,

        "saving_percent":
            saving_percent,
    }
def print_duplicate_stats():

    data = (
        get_duplicate_stats()
    )

    print()

    print(
        "DUPLICATE STATS"
    )

    print(
        "=" * 50
    )

    print()

    print(
        "TOTAL:",
        data["total_records"]
    )

    print(
        "DUPLICATES:",
        data["duplicate_records"]
    )

    print(
        "UNIQUE:",
        data["unique_records"]
    )

    print(
        "SAVING:",
        str(
            data[
                "saving_percent"
            ]
        )
        + "%"
    )

    print()