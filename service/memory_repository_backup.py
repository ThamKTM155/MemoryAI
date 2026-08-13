"""
Memory Repository
BUILD-21

Store and retrieve MemoryRecord objects.
"""

from data_model.memory_record import MemoryRecord


class MemoryRepository:
    """Repository for MemoryRecord persistence."""

    @staticmethod
    def save(
        memory: MemoryRecord,
    ) -> MemoryRecord:
        """Save a MemoryRecord."""
        return memory