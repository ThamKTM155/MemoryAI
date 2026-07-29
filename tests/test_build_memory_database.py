from tools.knowledge_repository import save_knowledge
from tools.build_memory_database import build_memory_database_pipeline


def test_build_memory_database(tmp_path):
    """
    Integration Test

    Knowledge JSON
            ↓
    load_all_knowledge()
            ↓
    build_memory_database()
            ↓
    build_relationships()
            ↓
    verify_relationships()
    """

    knowledge_dir = tmp_path / "knowledge"
    knowledge_dir.mkdir()

    knowledge = {
        "id": "SUMMARY-001",
        "date": "2026-07-28",
        "source": "Diary.md",
        "version": "1.0",

        "keywords": [
            "MemoryAI",
            "BUILD-36"
        ],

        "projects": [
            "MemoryAI"
        ],

        "decisions": [
            "Use layered architecture"
        ],

        "lessons": [
            "Always write unit tests first"
        ],

        "tasks": [
            "Implement BUILD-36"
        ]
    }

    save_knowledge(
        knowledge,
        knowledge_dir / "SUMMARY-001.json"
    )

    memory_db = build_memory_database_pipeline(
        knowledge_dir
    )

    # ======================================================
    # Memory Database
    # ======================================================

    assert len(memory_db["keywords"]) == 2
    assert len(memory_db["projects"]) == 1
    assert len(memory_db["decisions"]) == 1
    assert len(memory_db["lessons"]) == 1
    assert len(memory_db["tasks"]) == 1

    # ======================================================
    # Relationships
    # ======================================================

    assert "relationships" in memory_db
    assert isinstance(memory_db["relationships"], list)

    # Quan hệ phải được tạo ra
    assert len(memory_db["relationships"]) > 0

    # ======================================================
    # Verify diary_id mapping
    # ======================================================

    assert memory_db["keywords"][0]["diary_id"] == "SUMMARY-001"

    assert memory_db["projects"][0]["diary_id"] == "SUMMARY-001"

    assert memory_db["decisions"][0]["diary_id"] == "SUMMARY-001"

    assert memory_db["lessons"][0]["diary_id"] == "SUMMARY-001"

    assert memory_db["tasks"][0]["diary_id"] == "SUMMARY-001"