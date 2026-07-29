from tools.memory_repository import (
    save_memory_database,
    load_memory_database,
)


def test_memory_repository(tmp_path):
    """
    Unit Test

    Save Memory Database
            ↓
    Load Memory Database
            ↓
    Compare
    """

    memory_db = {
        "keywords": [
            {
                "diary_id": "SUMMARY-001",
                "keyword": "MemoryAI"
            }
        ],

        "projects": [
            {
                "diary_id": "SUMMARY-001",
                "project": "MemoryAI"
            }
        ],

        "decisions": [
            {
                "diary_id": "SUMMARY-001",
                "decision": "Use layered architecture"
            }
        ],

        "lessons": [
            {
                "diary_id": "SUMMARY-001",
                "lesson": "Always write unit tests first"
            }
        ],

        "tasks": [
            {
                "diary_id": "SUMMARY-001",
                "task": "Implement BUILD-36"
            }
        ],

        "relationships": [
            {
                "from": "SUMMARY-001",
                "to": "MemoryAI",
                "type": "HAS_KEYWORD"
            }
        ]
    }

    output_file = tmp_path / "memory_db.json"

    # ======================================
    # Save
    # ======================================

    save_memory_database(
        memory_db,
        output_file
    )

    # File phải tồn tại

    assert output_file.exists()

    # ======================================
    # Load
    # ======================================

    loaded = load_memory_database(
        output_file
    )

    # ======================================
    # Compare
    # ======================================

    assert loaded == memory_db