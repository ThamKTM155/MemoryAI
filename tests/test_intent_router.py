from tools.memory_chat import chat

print("=" * 60)
print("INTENT ROUTER TEST")
print("=" * 60)

print()

questions = [
    "GRAPH_RULES",
    "What is GRAPH_RULES?",
    "Is GRAPH_RULES important?",
]

for question in questions:

    print("-" * 60)
    print(question)
    print()

    print(chat(question))
    print()