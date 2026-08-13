from service.memory_keyword_engine import (
    build_keywords,
)


data = build_keywords()

print()

print(
    "MEMORY KEYWORD TEST"
)

print(
    "=" * 50
)

print(
    "TITLES:",
    len(data)
)

print(
    "KEYWORD FILE UPDATED"
)

print()