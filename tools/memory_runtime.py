from pathlib import Path

from core.memory_loader import load_memory_db
from tools.memory_answer import answer_memory

ROOT = Path(__file__).resolve().parent.parent

MEMORY_DB = ROOT / "11_Diary_Summary" / "memory_db.json"

memory = load_memory_db(str(MEMORY_DB))

print("=" * 60)
print("MemoryAI")
print("=" * 60)

print(f"Database : {memory['metadata']['database']}")
print(f"Version  : {memory['metadata']['version']}")

print("\nProjects")

for project in memory["projects"]:
    print(" -", project["name"])

print("\nGõ 'exit' để thoát.")

while True:

    question = input("\nBạn hỏi: ").strip()

    if question.lower() in ["exit", "quit"]:
        break

    if not question:
        continue

    print("\nĐang tìm kiếm...\n")

    answer = answer_memory(question)

    print()
    print(answer)