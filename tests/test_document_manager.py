from core.document_manager import DocumentManager

manager = DocumentManager(
    r"D:\MemoryAI\05_Diary"
)

manager.load()

print("=" * 60)

print("TOTAL DOCUMENTS")

print(manager.count())

print()

print("ROADMAP")

for doc in manager.get_by_type("ROADMAP"):

    print(doc["filename"])

print()

print("ADR")

for doc in manager.get_by_type("ADR"):

    print(doc["filename"])

print()

print("DAILY LOG")

for doc in manager.get_by_type("DAILY_LOG"):

    print(doc["filename"])

print()

print("NOTE")

for doc in manager.get_by_type("NOTE"):

    print(doc["filename"])