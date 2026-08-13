from service.memory_retrieval_engine import (
    retrieve,
)


print()

print(
    "=== MEMORY RETRIEVAL SERVICE TEST ==="
)

print()


results = retrieve(
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