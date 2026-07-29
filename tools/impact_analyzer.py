from pathlib import Path

ROOT = Path(r"D:\MemoryAI")

KEYWORDS = [
    "_summary.md",
    "summary_index.json",
    "DS-",
    "11_Diary_Summary",
    "extract_date(",
    "save_summary(",
]

print("=" * 80)
print("MEMORYAI BUILD-33D")
print("Impact Analyzer")
print("=" * 80)

results = []

for py in ROOT.rglob("*.py"):

    try:
        text = py.read_text(encoding="utf-8")
    except Exception:
        continue

    found = []

    for key in KEYWORDS:
        if key in text:
            found.append(key)

    if found:
        results.append((py, found))

print()

for path, found in sorted(results):

    print(path.relative_to(ROOT))
    for item in found:
        print("   ->", item)
    print()

print("=" * 80)
print("FILES AFFECTED :", len(results))
print("=" * 80)