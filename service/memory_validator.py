"""
Memory Validator
BUILD-21

Validate data before creating or updating MemoryRecord.
"""

class MemoryValidator:
    """Validate MemoryRecord input data."""

    @staticmethod
    def validate_required_fields(
        memory_type: str,
        title: str,
        content: str,
        project: str,
    ) -> None:
        """Validate required fields."""
        fields = {
            "memory_type": memory_type,
            "title": title,
            "content": content,
            "project": project,
        }

        for field_name, value in fields.items():
            if not value or not value.strip():
                raise ValueError(f"{field_name} is required.")

    @staticmethod
    def validate(
        memory_type: str,
        title: str,
        content: str,
        project: str,
    ) -> None:
        """Validate all MemoryRecord input data."""

        MemoryValidator.validate_required_fields(
            memory_type=memory_type,
            title=title,
            content=content,
            project=project,
        )
