from tools.knowledge_builder import build_knowledge


def test_knowledge_builder():

    metadata = {
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
        ]
    }

    knowledge = build_knowledge(metadata)

    assert knowledge["id"] == "SUMMARY-001"
    assert knowledge["date"] == "2026-07-28"
    assert knowledge["source"] == "05_Diary/2026-07-28.md"
    assert knowledge["version"] == "1.0"

    assert knowledge["keywords"] == [
        "MemoryAI",
        "BUILD-35"
    ]

    assert knowledge["projects"] == [
        "MemoryAI"
    ]

    assert knowledge["decisions"] == []
    assert knowledge["lessons"] == []
    assert knowledge["tasks"] == []