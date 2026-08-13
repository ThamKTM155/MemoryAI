"""
Memory Repository
BUILD-69R-3F

Store and retrieve MemoryRecord objects.
"""

import json
from pathlib import Path

from data_model.memory_record import MemoryRecord

from service.memory_duplicate_logger import (
    log_duplicate,
)

DATA_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "memory_records.json"
)

class MemoryRepository:
    """Repository for MemoryRecord persistence."""
    
    @staticmethod
    def exists_content(
        content,
    ):

        memories = (
            MemoryRepository.load_all()
        )

        content = (
            content.strip()
            .lower()
        )

        for memory in memories:

            old_content = (
                memory.get(
                    "content",
                    ""
                )
                .strip()
                .lower()
            )

            if old_content == content:

                return True

        return False        

    @staticmethod
    def save(
        memory: MemoryRecord,
    ) -> MemoryRecord:
        """Save a MemoryRecord."""

        if DATA_FILE.exists():

            try:
                with open(
                    DATA_FILE,
                    "r",
                    encoding="utf-8"
                ) as f:
                    records = json.load(f)

            except Exception:
                records = []

        else:
            records = []

        if MemoryRepository.exists_content(
            memory.content
        ):

            log_duplicate(
                memory.title,
                memory.source,
            )

            return memory

        records.append(
            memory.to_dict()
        )

        with open(
            DATA_FILE,
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                records,
                f,
                ensure_ascii=False,
                indent=4
            )

        return memory

    @staticmethod
    def load_all():
        """Load all memories."""

        if not DATA_FILE.exists():
            return []

        try:

            with open(
                DATA_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except Exception:

            return []