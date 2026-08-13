"""
Memory Usage Repository
BUILD-69K
"""

import json

from pathlib import Path


FILE_PATH = (
    Path(__file__).parent.parent
    /
    "data"
    /
    "memory_usage.json"
)


class MemoryUsageRepository:

    @staticmethod
    def load():

        if not FILE_PATH.exists():

            return {}

        with open(
            FILE_PATH,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(
                f
            )

    @staticmethod
    def save(
        data
    ):

        FILE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            FILE_PATH,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=2
            )