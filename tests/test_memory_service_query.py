from service.memory_service import (
    MemoryService,
)


print()

print(
    "=== MEMORY SERVICE QUERY TEST ==="
)

print()


results = MemoryService.search_memory(
    "SYSTEM CONSTITUTION"
)


print(
    "FOUND:",
    len(results)
)

print()


for memory in results[:5]:

    print(
        memory.get(
            "title",
            ""
        )
    )

print()