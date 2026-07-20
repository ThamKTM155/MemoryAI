from core.memory_api import Memory
from core.reasoning.build_reasoner import BuildReasoner

memory = Memory("05_Diary")
memory.load()

reasoner = BuildReasoner(memory)

print("=" * 60)
print("BUILD REASONER")
print("=" * 60)

print()

print("LATEST BUILD")

print(reasoner.get_latest_build())

print()

print("ANSWER")

print(reasoner.answer())