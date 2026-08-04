from pprint import pprint

from tools.memory_pipeline import (
    run,
)

result = run("GRAPH_RULES")

print("=" * 60)
print("MEMORY PIPELINE TEST")
print("=" * 60)

print()

pprint(result)