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

    @staticmethod
    def save_memory(
        memory: MemoryRecord,
    ) -> MemoryRecord:
        """Save an existing MemoryRecord through MemoryService."""

        if not isinstance(
            memory,
            MemoryRecord,
        ):
            raise TypeError(
                "memory must be a MemoryRecord"
            )

        return MemoryRepository.save(
            memory
        )

    @staticmethod
    def get_memory():
        raise NotImplementedError()
    @staticmethod
    def get_all_memories():

        return MemoryRepository.load_all()
    @staticmethod
    def search_memory(
        keyword: str,
    ):
        """Search memories through the MemoryService gate."""

        memories = (
            MemoryRepository.load_all()
        )

        results = []

        keyword = (
            keyword
            .lower()
            .strip()
        )

        for memory in memories:

            title = (
                memory.get(
                    "title",
                    "",
                )
                .lower()
            )

            content = (
                memory.get(
                    "content",
                    "",
                )
                .lower()
            )

            if (
                keyword in title
                or
                keyword in content
            ):

                results.append(
                    memory
                )

        return results

    @staticmethod
    def update_memory():
        raise NotImplementedError()

    @staticmethod
    def delete_memory():
        raise NotImplementedError()