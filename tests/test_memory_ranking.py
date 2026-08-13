from service.memory_retrieval_engine import (
    retrieve,
)

from service.memory_ranking_engine import (
    rank_memories,
)

keyword = "constitution"

results = retrieve(
    keyword
)

ranked = rank_memories(
    keyword,
    results,
)

print()

print(
    "FOUND:",
    len(ranked)
)

print()

for score, memory in ranked[:10]:

    print(
        score,
        "-",
        memory["title"]
    )

print()