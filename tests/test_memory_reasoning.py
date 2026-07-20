from core.knowledge_repository import KnowledgeRepository
from core.memory_reasoning import MemoryReasoning

repo = KnowledgeRepository("05_Diary")

repo.load()

reasoning = MemoryReasoning(repo)

print("=" * 60)
print("MEMORY REASONING")
print("=" * 60)

print()

print("LATEST BUILD")

print(reasoning.latest_build()["filename"])

print()

print("CURRENT ROADMAP")

print(reasoning.current_roadmap()["filename"])

print()

print("LATEST ADR")

print(reasoning.latest_adr()["filename"])

print()

print("PROJECT SUMMARY")

print(reasoning.project_summary())