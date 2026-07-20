"""
Test Memory Graph
BUILD-26.0
"""

from core.memory_graph import build_memory_graph


def main():

    # Memory giả lập
    memory = {

        "A": {
            "project": "MemoryAI"
        },

        "B": {
            "project": "MemoryAI"
        },

        "C": {
            "project": "AutoYouTube"
        }

    }

    graph = build_memory_graph(memory)

    print("=" * 40)
    print("MEMORY GRAPH")
    print("=" * 40)

    for memory_id, related in graph.items():
        print(f"{memory_id} -> {related}")


if __name__ == "__main__":
    main()