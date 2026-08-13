from tools.core_identity import answer_identity

print("=" * 60)
print("IDENTITY TEST")
print("=" * 60)
print()

questions = [

    "Bạn tên là gì?",
    "Bạn là ai?",
    "Ai sáng tạo bạn?",
    "Bạn do ai tạo ra?",
    "Tên của bạn là gì?"

]

for q in questions:

    print("-" * 60)
    print(q)
    print()

    answer = answer_identity(q)

    print(answer)
    print()