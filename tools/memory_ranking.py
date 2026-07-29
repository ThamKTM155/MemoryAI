"""
========================================================

MemoryAI
BUILD-037

Module:
memory_ranking.py

Description:
Memory Ranking Engine.

Chịu trách nhiệm:

- Tính điểm cho Memory
- Xếp hạng kết quả
- Loại bỏ kết quả không hợp lệ

========================================================
"""

from typing import List, Dict


def calculate_score(memory: Dict, query: str) -> int:
    """
    Tính điểm cho một Memory.
    """

    if not query:
        return 0

    score = 0
    query = query.lower()

    for _, value in memory.items():

        if isinstance(value, str):
            score += value.lower().count(query)

        elif isinstance(value, list):
            for item in value:
                score += str(item).lower().count(query)

    return score

def deduplicate_memories(memories):
    """
    Remove duplicate memories while preserving order.

    Priority:
    1. diary_id
    2. id
    3. from + to + type (relationships)
    4. full content (fallback)
    """

    seen = set()
    unique = []

    for memory in memories:

        # Ưu tiên diary_id
        if "diary_id" in memory:
            key = ("diary", memory["diary_id"])

        # Nếu là system/project...
        elif "id" in memory:
            key = ("id", memory["id"])

        # Nếu là relationship
        elif (
            "from" in memory
            and "to" in memory
            and "type" in memory
        ):
            key = (
                "relationship",
                memory["from"],
                memory["to"],
                memory["type"]
            )

        # Dự phòng
        else:
            key = ("fallback", str(sorted(memory.items())))

        if key in seen:
            continue

        seen.add(key)
        unique.append(memory)

    return unique

def rank_memories(
    memories: List[Dict],
    query: str,
    top_k: int = 5
) -> List[Dict]:
    """
    Xếp hạng Memory theo điểm.
    """

    ranked = []

    for memory in memories:

        score = calculate_score(
            memory,
            query
        )

        if score > 0:

            item = memory.copy()
            item["_score"] = score

            ranked.append(item)

    ranked.sort(
        key=lambda x: x["_score"],
        reverse=True
    )
    ranked = deduplicate_memories(ranked)
    return ranked[:top_k]