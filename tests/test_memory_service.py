"""
Tests for MemoryService.
BUILD-21
"""

from service.memory_service import MemoryService


def test_create_memory():
    """Test creating a MemoryRecord."""

    memory = MemoryService.create_memory(
        memory_type="knowledge",
        title="Python",
        content="Python supports object-oriented programming.",
        project="MemoryAI",
    )

    assert memory is not None
    assert memory.memory_type == "knowledge"
    assert memory.title == "Python"
    assert memory.content == "Python supports object-oriented programming."
    assert memory.project == "MemoryAI"

    print("✅ test_create_memory PASSED")


if __name__ == "__main__":
    test_create_memory()