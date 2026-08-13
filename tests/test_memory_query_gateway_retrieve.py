from service.memory_query_gateway import (
    retrieve_memories,
)

print()
print(
    "MEMORY QUERY GATEWAY RETRIEVE TEST"
)
print("=" * 50)

results = retrieve_memories(
    "SYSTEM CONSTITUTION"
)

print(
    "FOUND:",
    len(results)
)

for item in results[:5]:

    print(
        item.get(
            "title",
            ""
        )
    )

print()