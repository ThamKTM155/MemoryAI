import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

GRAPH_FILE = BASE_DIR / "memory_graph.json"


def load_graph():

    with open(
        GRAPH_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def load_nodes():

    return load_graph()["nodes"]


def load_edges():

    return load_graph()["edges"]