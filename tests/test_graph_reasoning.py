from core.memory_loader import load_memory_db
from core.memory_graph import build_memory_graph
from core.memory_path import find_path

from core.memory_reasoning import (
    explain_path,
    summarize_path
)

DB = r"D:\MemoryAI\11_Diary_Summary\memory_db.json"


def main():

    db = load_memory_db(DB)

    graph = build_memory_graph(db)

    path = find_path(
        graph,
        "MemoryAI",
        "Github"
    )

    print("=" * 50)
    print("MEMORY REASONING")
    print("=" * 50)

    print()

    print(explain_path(path))
    print()

    print("Summary")

    print(
        summarize_path(path)
    )

if __name__ == "__main__":
    main()