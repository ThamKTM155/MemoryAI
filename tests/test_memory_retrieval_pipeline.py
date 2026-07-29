"""
========================================================

MemoryAI
BUILD-037

NEW FILE

test_memory_retrieval_pipeline.py

Search
    ↓
Ranking
    ↓
Context Builder

========================================================
"""

from tools.memory_search import search_memory_raw
from tools.memory_ranking import rank_memories
from tools.context_builder import build_context
from tools.memory_repository import load_memory_database
from tools.memory_optimizer import optimize_memories
from pathlib import Path

memory_db = load_memory_database(
    Path("11_Diary_Summary/memory_db.json")
)

def test_pipeline(query: str):

    print("=" * 80)
    print("MEMORY PIPELINE TEST")
    print("=" * 80)

    print(f"\nQuery : {query}")

    # --------------------------------------------------
    # STEP 1
    # --------------------------------------------------

    print("\n[1] SEARCH")

    search_result = search_memory_raw(
        query=query,
        memory_db=memory_db
    )

    if not search_result:

        print("❌ Search không có kết quả")

        return

    print("✓ Search OK")

    # --------------------------------------------------
    # STEP 2
    # --------------------------------------------------

    print("\n[2] RANKING")

    if isinstance(search_result, list):

        ranked = rank_memories(
            memories=search_result,
            query=query
        )

        print(f"✓ Ranking OK ({len(ranked)} results)")

    else:

        ranked = search_result

        print(
            "⚠ Search hiện trả về String."
        )

        print(
            "⚠ Ranking được bỏ qua."
        )

    # --------------------------------------------------
    # STEP 3
    # --------------------------------------------------

    print("\n[3] CONTEXT")

    if isinstance(ranked, list):

        optimized = optimize_memories(ranked)

        context = build_context(optimized)

    else:

        context = ranked

    print("✓ Context Builder OK")

    # --------------------------------------------------
    # RESULT
    # --------------------------------------------------

    print("\n" + "=" * 80)
    print("FINAL CONTEXT")
    print("=" * 80)

    print(context)

    print("\n")
    print("=" * 80)
    print("PIPELINE SUCCESS")
    print("=" * 80)


if __name__ == "__main__":

    while True:

        query = input("\nQuery : ").strip()

        if query.lower() in ("exit", "quit"):

            break

        test_pipeline(query)