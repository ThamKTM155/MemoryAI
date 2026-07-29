from tools.build_memory_database import (
    build_memory_database_pipeline,
)

from tools.memory_repository import (
    load_memory_database,
)

import json


def test_memory_pipeline(tmp_path):
    """
    End-to-End Test

    Knowledge JSON
            ↓
    Memory Builder
            ↓
    Relationships
            ↓
    Save memory_db.json
            ↓
    Load memory_db.json
            ↓
    Compare
    """

    # =====================================
    # Create Knowledge Directory
    # =====================================

    knowledge_dir = tmp_path / "knowledge"
    knowledge_dir.mkdir()

    knowledge = {
        "diary_id": "SUMMARY-001",
        "keywords": [
            "MemoryAI",
            "Pipeline"
        ],
        "projects": [
            "MemoryAI"
        ],
        "decisions": [
            "Use layered architecture"
        ],
        "lessons": [
            "Always test modules"
        ],
        "tasks": [
            "Finish BUILD-36"
        ]
    }

    with open(
        knowledge_dir / "SUMMARY-001.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            knowledge,
            f,
            ensure_ascii=False,
            indent=4
        )

    # =====================================
    # Build + Save
    # =====================================

    output_file = tmp_path / "memory_db.json"

    memory_db = build_memory_database_pipeline(
        knowledge_dir,
        output_file=output_file
    )

    # =====================================
    # File exists
    # =====================================

    assert output_file.exists()

    # =====================================
    # Load
    # =====================================

    loaded = load_memory_database(
        output_file
    )

    # =====================================
    # Compare
    # =====================================

    assert loaded == memory_db

    # =====================================
    # Basic checks
    # =====================================

    assert len(memory_db["keywords"]) == 2
    assert len(memory_db["projects"]) == 1
    assert len(memory_db["decisions"]) == 1
    assert len(memory_db["lessons"]) == 1
    assert len(memory_db["tasks"]) == 1

    assert len(memory_db["relationships"]) > 0