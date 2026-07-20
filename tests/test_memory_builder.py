from core.memory_loader import load_memory_db
from core.memory_builder import (
    verify_relationships,
    print_verify_report,
    update_memory_relationships
)

memory_db = load_memory_db(
    "11_Diary_Summary/memory_db.json"
)

result = verify_relationships(memory_db)

print_verify_report(result)

memory_db = update_memory_relationships(
    memory_db,
    result["relationships"]
)

print()
print("Relationships cập nhật trong RAM:",
      len(memory_db["relationships"]))