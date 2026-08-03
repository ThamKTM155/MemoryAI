"""
Knowledge Repository
====================

Quản lý việc lưu và đọc Knowledge.
"""

import json
from dataclasses import asdict
from pathlib import Path

from data_model.knowledge import Knowledge


class KnowledgeRepository:

    def __init__(self, storage_path="memory/knowledge"):

        self.storage_path = Path(storage_path)

        self.storage_path.mkdir(parents=True, exist_ok=True)

    def save(self, knowledge: Knowledge):

        filename = self.storage_path / f"{knowledge.id}.json"

        with open(filename, "w", encoding="utf-8") as f:

            json.dump(
                asdict(knowledge),
                f,
                ensure_ascii=False,
                indent=4
            )

    def load_all(self):

        result = []

        for file in self.storage_path.glob("*.json"):

            with open(file, "r", encoding="utf-8") as f:

                data = json.load(f)

            result.append(Knowledge(**data))

        return result