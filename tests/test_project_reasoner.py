from core.memory_api import Memory
from core.project_reasoner import ProjectReasoner

memory = Memory("05_Diary")
memory.load()

reasoner = ProjectReasoner(memory)

print("=" * 60)
print("PROJECT REASONER")
print("=" * 60)

questions = [

    "Dự án đang ở đâu?",

    "Roadmap hiện tại là gì?",

    "ADR mới nhất?",

    "Build gần nhất?",

    "Xin chào"

]

for question in questions:

    print()
    print("Q:", question)
    print("A:", reasoner.answer(question))