from tools.collect_facts import (
    collect_facts,
)

from tools.reason_engine import (
    reason,
)

from tools.insight_generator import (
    generate_insight,
)


facts = collect_facts("GRAPH_RULES")

reasoning = reason(facts)

insight = generate_insight(reasoning)

print("=" * 60)
print("INSIGHT GENERATOR TEST")
print("=" * 60)

print()

print("FACTS")
print(facts)

print()

print("REASONING")
print(reasoning)

print()

print("INSIGHT")
print(insight)