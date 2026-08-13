from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent

GRAPH_FILE = BASE_DIR / "memory_graph.json"


def search(keyword):

    keyword = keyword.lower()

    with open(
        GRAPH_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        graph = json.load(f)

    results = []

    for node in graph["nodes"]:

        text = str(node).lower()

        if keyword in text:

            results.append(node["id"])

    return results