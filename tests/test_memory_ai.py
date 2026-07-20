from core.memory_ai import MemoryAI

ai = MemoryAI()

test_questions = [
    "build mới nhất",
    "build gần nhất",
    "đã hoàn thành gì",
    "kết quả là gì",
    "hello"
]

for i, q in enumerate(test_questions, start=1):

    print()
    print("=" * 70)
    print(f"TEST {i}")
    print("QUESTION :", q)

    answer = ai.answer(q)

    print("ANSWER")
    print("-" * 70)
    print(answer)