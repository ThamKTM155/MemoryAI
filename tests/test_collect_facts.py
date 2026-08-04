from pprint import pprint

from tools.collect_facts import (
    collect_facts,
)


facts = collect_facts("GRAPH_RULES")

print("=" * 60)
print("COLLECT FACTS TEST")
print("=" * 60)

print()

pprint(facts)