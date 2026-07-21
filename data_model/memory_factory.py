"""
Memory Factory
BUILD-21

Create and validate MemoryRecord objects.
"""

import uuid

from data_model.memory_record import MemoryRecord
class MemoryFactory:
    """Factory for creating MemoryRecord objects."""
    @staticmethod
    def create_memory(
        memory_type: str,
        title: str,
        content: str,
        project: str,
        source: str = "",
    ) -> MemoryRecord:
        """Create a new MemoryRecord."""
        memory_id = str(uuid.uuid4())
        memory = MemoryRecord(
            id=memory_id,
            memory_type=memory_type,
            title=title,
            content=content,
            project=project,
            source=source,
        )
        return memory