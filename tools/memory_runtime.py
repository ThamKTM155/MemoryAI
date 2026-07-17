from core.memory_loader import load_memory_db
from config import MEMORY_DB

memory = load_memory_db(MEMORY_DB)

print("=" * 60)
print("MEMORY RUNTIME")
print("=" * 60)

print("\nDatabase")
print(memory["metadata"]["database"])

print("\nVersion")
print(memory["metadata"]["version"])

print("\nProjects")

for project in memory["projects"]:
    print("-", project["name"])