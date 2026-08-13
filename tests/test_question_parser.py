from tools.question_parser import parse

print("=" * 60)
print("QUESTION PARSER TEST")
print("=" * 60)

print()

questions = [
    "GRAPH_RULES",
    "What is GRAPH_RULES?",
    "Is GRAPH_RULES important?",
    "Which project is GRAPH_RULES in?",
]

for question in questions:
    print(question)
    print("->", parse(question))
    print()