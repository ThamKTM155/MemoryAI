from tools.memory_chat import chat

print("=" * 60)
print("INTENT ANSWER GENERATOR TEST")
print("=" * 60)

print()

questions = [
    "GRAPH_RULES",
    "What is GRAPH_RULES?",
    "Is GRAPH_RULES important?",
    "Which project is GRAPH_RULES in?",
    "What should I do before editing GRAPH_RULES?",
]

for question in questions:

    print("-" * 60)
    print(question)
    print()

    print(chat(question))
    print()