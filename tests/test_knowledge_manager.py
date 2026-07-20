from core.knowledge_repository import KnowledgeRepository
from core.knowledge_manager import KnowledgeManager


repo = KnowledgeRepository(
    r"D:\MemoryAI\05_Diary"
)

repo.load()

km = KnowledgeManager(repo)

print("=" * 60)
print("SUMMARY")
print("=" * 60)

print(km.summary())

print()

print("=" * 60)
print("SEARCH : Builder")
print("=" * 60)

for doc in km.search("Builder"):

    print(doc["filename"])