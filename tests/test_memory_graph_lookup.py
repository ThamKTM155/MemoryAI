from tools.memory_graph_lookup import search

print("=" * 60)
print("MEMORY SEARCH TEST")
print("=" * 60)

print()

keywords = [
    "MemoryGraph",
    "BUILD-41A",
    "DOCUMENT",
]

for keyword in keywords:

    print(keyword)
    print(search(keyword))
    print()