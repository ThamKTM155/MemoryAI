import sys
from pathlib import Path

ROOT = (
    Path(__file__).resolve().parent.parent
)

sys.path.append(
    str(ROOT)
)

from service.memory_repository import (
    MemoryRepository,
)

from service.memory_freshness_engine import (
    update_timestamp,
)
memories = MemoryRepository.load_all()

count = 0

for memory in memories:

    title = memory.get(
        "title",
        ""
    )

    if not title:
        continue

    update_timestamp(
        title
    )

    count += 1

print(
    "UPDATED:",
    count
)