from pathlib import Path
import json

FILE = (
    Path("data")
    / "memory_confidence.json"
)

class MemoryConfidenceRepository:

    @staticmethod
    def load():

        if not FILE.exists():
            return {}

        return json.loads(
            FILE.read_text(
                encoding="utf-8"
            )
        )

    @staticmethod
    def save(data):

        FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        FILE.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )