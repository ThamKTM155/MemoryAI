from pathlib import Path

from tools.build_knowledge_database import build_knowledge_database
from tools.knowledge_repository import load_all_knowledge


def test_build_knowledge_database(tmp_path):

    summary_dir = tmp_path / "summaries"
    output_dir = tmp_path / "knowledge"

    summary_dir.mkdir()
    output_dir.mkdir()

    summary = summary_dir / "SUMMARY-001_summary.md"

    summary.write_text(
        """ID: SUMMARY-001
Date: 2026-07-28
Source: Diary.md
Version: 1.0

## Keywords

- MemoryAI
- BUILD-35

## Related Projects

- MemoryAI
""",
        encoding="utf-8"
    )

    # Build database
    created = build_knowledge_database(
        summary_dir,
        output_dir
    )

    # Kiểm tra số file tạo ra
    assert len(created) == 1

    # Kiểm tra file tồn tại
    assert created[0].exists()

    # Đọc lại database
    knowledge = load_all_knowledge(output_dir)

    assert len(knowledge) == 1

    record = knowledge[0]

    assert record["id"] == "SUMMARY-001"
    assert record["date"] == "2026-07-28"
    assert record["source"] == "Diary.md"
    assert record["version"] == "1.0"

    assert record["keywords"] == [
        "MemoryAI",
        "BUILD-35"
    ]

    assert record["projects"] == [
        "MemoryAI"
    ]

    assert record["decisions"] == []
    assert record["lessons"] == []
    assert record["tasks"] == []