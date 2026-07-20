from core.knowledge_repository import KnowledgeRepository

repo = KnowledgeRepository(
    r"D:\MemoryAI\05_Diary"
)

repo.load()

print("=" * 60)

print("STATISTICS")

print("=" * 60)

print(repo.statistics)

print()

print("=" * 60)

print("DOCUMENT TYPES")

print("=" * 60)

for doc_type in repo.by_type:

    print(doc_type)

    print(
        len(
            repo.by_type[doc_type]
        )
    )

    print()

print("=" * 60)

print("LOOKUP BY FILENAME")

print("=" * 60)

doc = repo.by_filename.get(
    "ADR-001_MEMORY_ARCHITECTURE.md"
)

if doc:

    print(doc["filename"])

    print(doc["type"])

print("=" * 60)

print("SPECIAL INDEXES")

print("=" * 60)

print()

print("CURRENT ROADMAP")

print(repo.current_roadmap["filename"])

print()

print("LATEST ADR")

print(repo.latest_adr["filename"])

print()

print("LATEST DAILY LOG")

print(repo.latest_daily_log["filename"])

print()

print("DOCUMENTS BY DATE")

for name in sorted(repo.documents_by_date):

    print(name)
print("=" * 60)
print("TIMELINE")
print("=" * 60)

latest = repo.timeline.latest()

print()

print("LATEST")

print(latest["date"])

print(latest["document"]["filename"])

print()

earliest = repo.timeline.earliest()

print("EARLIEST")

print(earliest["date"])

print(earliest["document"]["filename"])