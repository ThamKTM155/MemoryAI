from pathlib import Path
from tools.summary_parser import parse_summary

BASE_DIR = Path(__file__).resolve().parent.parent
SUMMARY_DIR = BASE_DIR / "11_Diary_Summary" / "summaries"


def test_summary_parser():
    summary = sorted(SUMMARY_DIR.glob("*_summary.md"))[0]

    print(summary.name)
    print()

    metadata = parse_summary(summary)

    for k, v in metadata.items():
        print(f"{k}: {v}")

    assert metadata