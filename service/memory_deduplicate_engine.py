from service.memory_service import (
    MemoryService,
)

def remove_exact_duplicates():

    memories = MemoryService.get_all_memories()

    unique = []
    seen = set()

    for memory in memories:

        content = (
            memory.get(
                "content",
                ""
            )
            .strip()
        )

        if content in seen:
            continue

        seen.add(content)

        unique.append(memory)

    return unique