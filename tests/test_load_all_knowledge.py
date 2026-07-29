from tools.knowledge_repository import (
    save_knowledge,
    load_all_knowledge
)


def test_load_all_knowledge(tmp_path):

    records = [

        {
            "id": "SUMMARY-001",
            "date": "2026-07-28",
            "source": "Diary1.md",
            "version": "1.0",
            "keywords": ["AI"],
            "projects": ["MemoryAI"],
            "decisions": [],
            "lessons": [],
            "tasks": []
        },

        {
            "id": "SUMMARY-002",
            "date": "2026-07-29",
            "source": "Diary2.md",
            "version": "1.0",
            "keywords": ["Python"],
            "projects": ["MemoryAI"],
            "decisions": [],
            "lessons": [],
            "tasks": []
        },

        {
            "id": "SUMMARY-003",
            "date": "2026-07-30",
            "source": "Diary3.md",
            "version": "1.0",
            "keywords": ["Testing"],
            "projects": ["MemoryAI"],
            "decisions": [],
            "lessons": [],
            "tasks": []
        }

    ]

    # Save
    for record in records:

        save_knowledge(
            record,
            tmp_path / f"{record['id']}.json"
        )

    # Load
    loaded = load_all_knowledge(tmp_path)

    # Kiểm tra số lượng
    assert len(loaded) == 3

    # Vì load_all_knowledge() đọc theo sorted()
    # nên thứ tự sẽ ổn định
    assert loaded == records