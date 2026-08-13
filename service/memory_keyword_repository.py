import json

from pathlib import Path

KEYWORD_FILE = Path(
    r"D:\MemoryAI\data\memory_keywords.json"
)

class MemoryKeywordRepository:

    @staticmethod
    def load():

        if not KEYWORD_FILE.exists():

            return {}

        with open(
            KEYWORD_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    @staticmethod
    def save(data):

        with open(
            KEYWORD_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )