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


facts = collect_facts("GRAPH_RULES")

reasoning = reason(facts)

knowledge = infer(
    facts,
    reasoning,
)

print("=" * 60)
print("INFERENCE ENGINE TEST")
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