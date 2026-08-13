from service.memory_service import (
    MemoryService,
)
def dryrun_deduplicate():

    memories = (
        MemoryService.get_all_memories()
    )

    seen = set()

    unique_memories = []

    for memory in memories:

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

        if key in seen:
            continue

        seen.add(
            key
        )

        unique_memories.append(
            memory
        )

    return unique_memories

def print_dryrun_stats():

    memories = (
        MemoryService.get_all_memories()
    )

    unique_memories = (
        dryrun_deduplicate()
    )

    print()

    print(
        "DEDUP DRY RUN"
    )

    print(
        "=" * 50
    )

    print()

    print(
        "CURRENT:",
        len(memories)
    )

    print(
        "AFTER:",
        len(unique_memories)
    )

    print(
        "REMOVED:",
        len(memories)
        -
        len(unique_memories)
    )

    print()