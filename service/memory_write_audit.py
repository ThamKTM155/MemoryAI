from service.memory_service import (
    MemoryService,
)
def count_memory_sources():

    memories = MemoryService.get_all_memories()

    stats = {}

    for memory in memories:

        source = memory.get(
            "source",
            "UNKNOWN"
        )

        stats[source] = (
            stats.get(source, 0)
            + 1
        )

    return stats

def print_memory_sources():

    data = count_memory_sources()

    print()

    print(
        "MEMORY SOURCES"
    )

    print(
        "=" * 50
    )

    print()

    for source, count in data.items():

        print(
            source,
            ":",
            count
        )

    print()