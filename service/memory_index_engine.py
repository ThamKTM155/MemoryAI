"""
Memory Index Engine
BUILD-70F

Create indexes for MemoryAI.
"""

import json

from pathlib import Path

from service.memory_service import (
    MemoryService,
)

INDEX_DIR = (
    Path(__file__).parent.parent
    / "data"
    / "indexes"
)

TITLE_INDEX_FILE = (
    INDEX_DIR
    / "title_index.json"
)


def build_title_index():

    memories = (
        MemoryService.get_all_memories()
    )

    title_index = {}

    for i, memory in enumerate(
        memories
    ):

        title = (
            memory.get(
                "title",
                ""
            )
            .strip()
        )

        if not title:
            continue

        if title not in title_index:

            title_index[
                title
            ] = []

        title_index[
            title
        ].append(i)

    INDEX_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        TITLE_INDEX_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            title_index,
            f,
            ensure_ascii=False,
            indent=4
        )

    return len(title_index)