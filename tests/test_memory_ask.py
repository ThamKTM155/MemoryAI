from pprint import pprint

from tools.memory_ask import (
    ask,
)

print("=" * 60)
print("MEMORY ASK TEST")
print("=" * 60)

print()

result = ask("GRAPH_RULES")

pprint(result)