from tools.collect_facts import (
    collect_facts,
)

from tools.summary_generator import (
    generate_summary,
)


facts = collect_facts("GRAPH_RULES")

summary = generate_summary(facts)

print("=" * 60)
print("SUMMARY GENERATOR TEST")
print("=" * 60)

print()

print("FACTS")
print(facts)

print()

print("SUMMARY")
print(summary)