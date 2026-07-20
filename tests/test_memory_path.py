from core.memory_loader import load_memory_db
from core.memory_graph import build_memory_graph
from core.memory_path import find_path

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
    print("MEMORY PATH")
    print("=" * 50)

    if not path:
        print("Không tìm thấy đường đi.")
        return

    for i, step in enumerate(path, start=1):
        print(
            f"{i}. {step['from']} --[{step['type']}]--> {step['to']}"
        )


if __name__ == "__main__":
    main()