from pathlib import Path
import json


# Đường dẫn
BASE_DIR = Path(__file__).resolve().parent.parent
SUMMARY_DIR = BASE_DIR / "11_Diary_Summary" / "summaries"
OUTPUT_FILE = BASE_DIR / "11_Diary_Summary" / "summary_index.json"


def parse_summary_metadata(summary_file):
    metadata = {
        "id": "",
        "date": "",
        "source": "",
        "version": "",
        "keywords": [],
        "projects": []
    }

    current_section = None

    with open(summary_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith("ID:"):
                metadata["id"] = line.replace("ID:", "").strip()

            elif line.startswith("Date:"):
                metadata["date"] = line.replace("Date:", "").strip()

            elif line.startswith("Source:"):
                metadata["source"] = line.replace("Source:", "").strip()

            elif line.startswith("Version:"):
                metadata["version"] = line.replace("Version:", "").strip()

            elif line.startswith("## Keywords"):
                current_section = "keywords"

            elif line.startswith("## Related Projects"):
                current_section = "projects"

            elif line.startswith("##"):
                current_section = None

            elif line.startswith("- "):
                value = line[2:].strip()

                if current_section == "keywords":
                    metadata["keywords"].append(value)

                elif current_section == "projects":
                    metadata["projects"].append(value)

    return metadata


def build_summary_index(summary_dir):
    """
    Quét toàn bộ thư mục Summary.
    """
    index = []

    for summary_file in sorted(summary_dir.glob("*_summary.md")):
        item = parse_summary_metadata(summary_file)

        if item:
            index.append(item)

    return index


def save_summary_index(index, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            index,
            f,
            ensure_ascii=False,
            indent=2
        )


def main():
    print("=" * 60)
    print("BUILD-35A : REBUILD SUMMARY INDEX")
    print("=" * 60)

    print(f"Summary Folder : {SUMMARY_DIR}")

    index = build_summary_index(SUMMARY_DIR)

    save_summary_index(index, OUTPUT_FILE)

    print(f"Output : {OUTPUT_FILE}")
    print(f"Total Summary : {len(index)}")


if __name__ == "__main__":
    main()