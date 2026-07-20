from core.memory_api import Memory
from core.reasoning.timeline_reasoner import TimelineReasoner

memory = Memory("05_Diary")
memory.load()
print("SUMMARY =")
print(memory.summary())
print()
reasoner = TimelineReasoner(memory)

print("=" * 60)
print("TIMELINE REASONER")
print("=" * 60)

print()

print("BUILD HISTORY")
print(reasoner.get_build_history())

print()

print("ANSWER")
print(reasoner.answer())