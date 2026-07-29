from pathlib import Path
from collections import defaultdict
from diary_processor import extract_date

# ==========================================
# MEMORYAI BUILD-33C
# Summary Conflict Detector
# ==========================================

DIARY_DIR = Path(r"D:\MemoryAI\05_Diary")

summary_map = defaultdict(list)

print("=" * 80)
print("MEMORYAI BUILD-33C")
print("Summary Conflict Detector")
print("=" * 80)

files = sorted(DIARY_DIR.glob("*"))

total = 0

for file in files:

    if not file.is_file():
        continue

    total += 1

    date = extract_date(file.name)

    summary_name = f"{date}_summary.md"

    summary_map[summary_name].append(file)

print()
print(f"Total diary files : {total}")
print()

conflicts = 0

for summary in sorted(summary_map):

    group = summary_map[summary]

    if len(group) <= 1:
        continue

    conflicts += 1

    print("=" * 80)
    print("SUMMARY FILE")
    print(summary)
    print("-" * 80)

    print("The following diary files will generate the SAME summary:\n")

    for f in group:

        print(" •", f.name)

    print("\n>>> CONFLICT : YES")
    print()

print("=" * 80)
print("FINAL REPORT")
print("=" * 80)

print(f"Diary files      : {total}")
print(f"Summary files    : {len(summary_map)}")
print(f"Conflicts        : {conflicts}")

if conflicts == 0:
    print("\nSTATUS : SAFE")
else:
    print("\nSTATUS : NOT SAFE")