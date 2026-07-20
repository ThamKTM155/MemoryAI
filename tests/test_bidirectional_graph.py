from core.memory_loader import load_memory_db
from core.memory_graph import (
    build_memory_graph,
    get_related_by_type
)

DB = r"D:\MemoryAI\11_Diary_Summary\memory_db.json"


def main():

    db = load_memory_db(DB)

    graph = build_memory_graph(db)

    print("=" * 50)
    print("BIDIRECTIONAL GRAPH")
    print("=" * 50)

    print()

    print("MemoryAI xuất hiện trong các Diary:")

    diaries = get_related_by_type(
        graph,
        "MemoryAI",
        "REVERSE_HAS_KEYWORD"
    )

    for diary in diaries:
        print("-", diary)

    print()

    print("Diary có Keyword:")

    keywords = get_related_by_type(
        graph,
        "DS-2026-06-16",
        "HAS_KEYWORD"
    )

    for keyword in keywords:
        print("-", keyword)


if __name__ == "__main__":
    main()