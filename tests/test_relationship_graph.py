from core.memory_loader import load_memory_db
from core.memory_graph import (
    build_memory_graph,
    get_related_by_type
)

DB = r"D:\MemoryAI\11_Diary_Summary\memory_db.json"


def main():

    memory_db = load_memory_db(DB)

    graph = build_memory_graph(memory_db)

    diary = "DS-2026-06-16"

    print("=" * 50)
    print("GRAPH TEST")
    print("=" * 50)

    print()

    print("Keywords")

    for k in get_related_by_type(graph, diary, "HAS_KEYWORD"):
        print("-", k)

    print()

    print("Decisions")

    for d in get_related_by_type(graph, diary, "HAS_DECISION"):
        print("-", d)

    print()

    print("Lessons")

    for l in get_related_by_type(graph, diary, "HAS_LESSON"):
        print("-", l)


if __name__ == "__main__":
    main()