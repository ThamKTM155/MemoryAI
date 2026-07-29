from pathlib import Path

from tools.knowledge_repository import (
    save_knowledge,
    load_knowledge
)


def test_knowledge_repository():

    knowledge = {
        "id": "SUMMARY-001",
        "date": "2026-07-28",
        "source": "05_Diary/2026-07-28.md",
        "version": "1.0",

        "keywords": [
            "MemoryAI",
            "BUILD-35"
        ],

        "projects": [
            "MemoryAI"
        ],

        "decisions": [],
        "lessons": [],
        "tasks": []
    }

    output_file = Path("tests") / "knowledge_test.json"

    # Save
    save_knowledge(
        knowledge,
        output_file
    )

    assert output_file.exists()

    # Load
    loaded = load_knowledge(output_file)

    # Compare
    assert loaded == knowledge

    # Cleanup
    output_file.unlink()