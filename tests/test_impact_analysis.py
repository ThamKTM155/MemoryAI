from pprint import pprint

from tools.collect_facts import (
    collect_facts,
)

from tools.reason_engine import (
    reason,
)

from tools.inference_engine import (
    infer,
)

from tools.impact_analysis import (
    analyze,
)


facts = collect_facts("GRAPH_RULES")

reasoning = reason(facts)

knowledge = infer(
    facts,
    reasoning,
)

impact = analyze(knowledge)

print("=" * 60)
print("IMPACT ANALYSIS TEST")
print("=" * 60)

print()

print("FACTS")
pprint(facts)

print()

print("REASONING")
pprint(reasoning)

print()

print("KNOWLEDGE")
pprint(knowledge)

print()

print("IMPACT")
pprint(impact)