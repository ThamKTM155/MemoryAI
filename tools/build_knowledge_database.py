"""
Knowledge Database Builder
BUILD-35.3

Nhiệm vụ:
- Quét thư mục Summary.
- Parse Summary.
- Build Knowledge Record.
- Lưu Knowledge JSON.

Không chứa Business Logic.
"""

from pathlib import Path

from tools.summary_parser import parse_summary
from tools.knowledge_builder import build_knowledge
from tools.knowledge_repository import save_knowledge


def build_knowledge_database(summary_dir, output_dir):
    """
    Build toàn bộ Knowledge Database.

    Parameters
    ----------
    summary_dir : str | Path

    output_dir : str | Path

    Returns
    -------
    list[Path]
        Danh sách file đã tạo.
    """

    summary_dir = Path(summary_dir)
    output_dir = Path(output_dir)

    created_files = []

    summaries = sorted(
        summary_dir.glob("*_summary.md")
    )

    for summary_file in summaries:

        metadata = parse_summary(summary_file)

        knowledge = build_knowledge(metadata)

        output_file = (
            output_dir /
            f"{metadata['id']}.json"
        )

        save_knowledge(
            knowledge,
            output_file
        )

        created_files.append(output_file)

    return created_files


if __name__ == "__main__":

    BASE_DIR = Path(__file__).resolve().parent.parent

    summary_dir = (
        BASE_DIR /
        "11_Diary_Summary" /
        "summaries"
    )

    output_dir = (
        BASE_DIR /
        "10_LongTermMemory" /
        "knowledge"
    )

    created = build_knowledge_database(
        summary_dir,
        output_dir
    )

    print()

    print("=" * 50)
    print("KNOWLEDGE DATABASE")
    print("=" * 50)

    print()

    print(f"Created : {len(created)}")

    for file in created:
        print(file.name)