from service.memory_index_engine import (
    build_title_index,
)

count = (
    build_title_index()
)

print()

print(
    "TITLES:",
    count
)

print()