from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
SUMMARY_DIR = BASE_DIR / "11_Diary_Summary" / "summaries"


def extract_id(summary_file):
    with open(summary_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("ID:"):
                return line.replace("ID:", "").strip()
    return ""


def extract_date(summary_file):
    with open(summary_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("Date:"):
                return line.replace("Date:", "").strip()
    return ""


def extract_source(summary_file):
    with open(summary_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("Source:"):
                return line.replace("Source:", "").strip()
    return ""


def main():

    summaries = sorted(SUMMARY_DIR.glob("*_summary.md"))

    print("=" * 60)
    print("SUMMARY AUDIT")
    print("=" * 60)

    print(f"Total Summary : {len(summaries)}")

    ids = defaultdict(list)
    dates = defaultdict(list)
    sources = defaultdict(list)

    for f in summaries:

        sid = extract_id(f)
        sdate = extract_date(f)
        source = extract_source(f)

        ids[sid].append(f.name)
        dates[sdate].append(f.name)
        sources[source].append(f.name)

    duplicate_date = {
        k: v
        for k, v in dates.items()
        if len(v) > 1
    }

    duplicate_source = {
        k: v
        for k, v in sources.items()
        if len(v) > 1
    }

    print(f"Unique ID          : {len(ids)}")
    print(f"Duplicate Date     : {len(duplicate_date)}")
    print(f"Duplicate Source   : {len(duplicate_source)}")

    print("\nFIRST 10 DUPLICATE DATES\n")

    count = 0

    for date, files in duplicate_date.items():

        print(date)

        for file in files:
            print("   ", file)

        print()

        count += 1

        if count >= 10:
            break


if __name__ == "__main__":
    main()