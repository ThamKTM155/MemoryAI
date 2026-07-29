from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
SUMMARY_DIR = BASE_DIR / "11_Diary_Summary" / "summaries"


def main():

    summaries = sorted(SUMMARY_DIR.glob("*_summary.md"))

    by_date = defaultdict(list)

    for f in summaries:

        date = f.name[:10]

        by_date[date].append(f)

    legacy = []

    for date, files in by_date.items():

        if len(files) < 2:
            continue

        for f in files:

            # BUILD mới luôn có tên dài hơn
            if "_nhat-ky-" not in f.stem:
                legacy.append(f)

    print("=" * 60)
    print("SUMMARY MIGRATION PREVIEW")
    print("=" * 60)

    print(f"Legacy Summary : {len(legacy)}")
    print()

    for f in legacy:
        print(f.name)


if __name__ == "__main__":
    main()