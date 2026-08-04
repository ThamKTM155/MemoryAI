from pprint import pprint

from tools.collect_facts import (
    collect_facts,
)

from tools.reason_engine import (
    reason,
)


facts = collect_facts("GRAPH_RULES")

reasoning = reason(facts)

print("=" * 60)
print("REASON ENGINE TEST")
print("=" * 60)

print()

print("FACTS")

pprint(facts)

print()

print("REASONING")

pprint(reasoning)