from pprint import pprint

from tools.collect_facts import collect_facts
from tools.reason_engine import reason
from tools.inference_engine import infer
from tools.impact_analysis import analyze
from tools.decision_engine import decide

facts = collect_facts("GRAPH_RULES")
reasoning = reason(facts)
knowledge = infer(facts, reasoning)
impact = analyze(knowledge)
decision = decide(impact)

print("=" * 60)
print("DECISION ENGINE TEST")
print("=" * 60)

print()

print("DECISION")
pprint(decision)