from core.diary_loader import DiaryLoader

loader = DiaryLoader(
    r"D:\MemoryAI\05_Diary"
)

docs = loader.load_all()

print("=" * 50)

print(f"Loaded {len(docs)} documents")

print("=" * 50)

for doc in docs:

    print(doc["filename"])