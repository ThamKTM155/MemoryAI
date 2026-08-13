import json

from service.memory_service import (
    MemoryService,
)

from service.memory_exact_duplicate_detector import (
    find_exact_duplicates,
)
def backup_duplicates():

    memories = (
        MemoryService.get_all_memories()
    )

    duplicates = (
        find_exact_duplicates()
    )

    backup = []

    for count, title, indexes in duplicates:

        for index in indexes:

            backup.append(
                {
                    "index": index,
                    "memory": memories[index]
                }
            )

    with open(
        "data/duplicate_backup.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            backup,
            f,
            ensure_ascii=False,
            indent=2
        )

    return len(
        backup
    )
def print_backup_result():

    total = (
        backup_duplicates()
    )

    print()

    print(
        "BACKUP CREATED"
    )

    print()

    print(
        "RECORDS:",
        total
    )

    print()
