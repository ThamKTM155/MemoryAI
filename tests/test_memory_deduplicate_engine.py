from service.memory_deduplicate_engine import (
    remove_exact_duplicates,
)

data = remove_exact_duplicates()

print()
print("DEDUPLICATE ENGINE TEST")
print("=" * 50)
print("UNIQUE:", len(data))
print()