import sys

sys.path.append(
    "D:\\MemoryAI"
)

from service.memory_repository import (
    MemoryRepository,
)

memories = MemoryRepository.load_all()

target = "Quy tắc"

for i, memory in enumerate(memories):

    if memory.get("title") == target:

        print()
        print("INDEX:", i)

        print(
            memory.get(
                "content",
                ""
            )[:200]
        )