from service.memory_write_audit import (
    count_memory_sources,
)


data = count_memory_sources()

print()

print(
    "MEMORY SOURCES"
)

print(
    "=" * 50
)

print()

for source, count in data.items():

    print(
        source,
        ":",
        count
    )

print()