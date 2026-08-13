from service.memory_retrieval_engine import (
    retrieve,
)

results = retrieve(
    "constitution"
)

print()

print(
    "FOUND:",
    len(results)
)

for item in results[:5]:

    print(
        item["title"]
    )

print()