from service.memory_dashboard_engine import (
    get_top_memories,
)

print()

print(
    "MEMORY DASHBOARD ENGINE TEST"
)

print(
    "=" * 50
)

items = get_top_memories(
    limit=10
)

print(
    "FOUND:",
    len(items)
)

print()

for score, memory in items:

    print(
        memory.get(
            "title",
            ""
        )
    )

    print(
        "SCORE:",
        score
    )

    print()