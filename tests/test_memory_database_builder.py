from tools.memory_database_builder import build_memory_database


def test_memory_database_builder():

    knowledge_records = [
        {
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
    ]

    memory_db = build_memory_database(knowledge_records)

    # ======================================================
    # Top-level keys
    # ======================================================

    assert "keywords" in memory_db
    assert "projects" in memory_db
    assert "decisions" in memory_db
    assert "lessons" in memory_db
    assert "tasks" in memory_db
    assert "relationships" in memory_db

    # ======================================================
    # Keywords
    # ======================================================

    assert len(memory_db["keywords"]) == 2

    assert memory_db["keywords"][0]["diary_id"] == "SUMMARY-001"
    assert memory_db["keywords"][0]["keyword"] == "MemoryAI"

    assert memory_db["keywords"][1]["keyword"] == "BUILD-36"

    # ======================================================
    # Projects
    # ======================================================

    assert len(memory_db["projects"]) == 1
    assert memory_db["projects"][0]["project"] == "MemoryAI"

    # ======================================================
    # Decisions
    # ======================================================

    assert len(memory_db["decisions"]) == 1
    assert (
        memory_db["decisions"][0]["decision"]
        == "Use layered architecture"
    )

    # ======================================================
    # Lessons
    # ======================================================

    assert len(memory_db["lessons"]) == 1
    assert (
        memory_db["lessons"][0]["lesson"]
        == "Always write unit tests first"
    )

    # ======================================================
    # Tasks
    # ======================================================

    assert len(memory_db["tasks"]) == 1
    assert (
        memory_db["tasks"][0]["task"]
        == "Implement BUILD-36"
    )

    # ======================================================
    # Relationships
    # ======================================================

    assert memory_db["relationships"] == []