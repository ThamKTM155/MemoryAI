from pprint import pprint

from tools.memory_query_service import (
    query,
)

result = query("GRAPH_RULES")

print("=" * 60)
print("MEMORY SERVICE TEST")
print("=" * 60)

print()

pprint(result)