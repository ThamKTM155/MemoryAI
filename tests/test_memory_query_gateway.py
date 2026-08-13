from service.memory_query_gateway import (
    search_by_title,
)

print()

print(
    "MEMORY QUERY GATEWAY TEST"
)

print(
    "=" * 50
)

results = search_by_title(
    "SYSTEM"
)

print(
    "FOUND:",
    len(results)
)

for item in results[:5]:

    print(
        item.get(
            "title"
        )
    )

print()