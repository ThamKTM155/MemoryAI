from tools.question_classifier import classify

print("=" * 60)
print("QUESTION CLASSIFIER TEST")
print("=" * 60)

print()

questions = [
    "GRAPH_RULES",
    "What is GRAPH_RULES?",
    "Is GRAPH_RULES important?",
    "Which project is GRAPH_RULES in?",
    "What should I do before editing GRAPH_RULES?",
]

for q in questions:
    print(q)
    print("->", classify(q))
    print()