import sys

sys.path.append(
    "D:\\MemoryAI"
)
from service.memory_repository import (
    MemoryRepository,
)

memories = MemoryRepository.load_all()

titles = []

for memory in memories:

    titles.append(
        memory.get(
            "title"
        )
    )

print(
    "TOTAL:",
    len(titles)
)

print(
    "UNIQUE:",
    len(set(titles))
)