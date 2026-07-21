"""
Memory Service
BUILD-21

Coordinate memory operations.
"""

from data_model.memory_record import MemoryRecord
from data_model.memory_factory import MemoryFactory
from service.memory_repository import MemoryRepository
from service.memory_validator import MemoryValidator


class MemoryService:
    """Service layer for MemoryRecord operations."""
    @staticmethod
    def create_memory(
        memory_type: str,
        title: str,
        content: str,
        project: str,
        source: str = "",
    ) -> MemoryRecord:
        """Create and save a new MemoryRecord."""
        MemoryValidator.validate(
            memory_type=memory_type,
            title=title,
            content=content,
            project=project,
        )

        memory = MemoryFactory.create_memory(
            memory_type=memory_type,
            title=title,
            content=content,
            project=project,
            source=source,
        )

        return MemoryRepository.save(memory)