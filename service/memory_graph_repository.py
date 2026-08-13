import json

from pathlib import Path

GRAPH_FILE = Path(
    r"D:\MemoryAI\data\memory_graph.json"
)


class MemoryGraphRepository:

    @staticmethod
    def load():

        if not GRAPH_FILE.exists():

            return {}

        with open(
            GRAPH_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    @staticmethod
    def save(data):

        with open(
            GRAPH_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )