from core.memory_api import Memory
from core.reasoning.roadmap_reasoner import RoadmapReasoner

memory = Memory("05_Diary")
memory.load()

reasoner = RoadmapReasoner(memory)

print("=" * 60)
print("ROADMAP REASONER")
print("=" * 60)

print()

print("CURRENT ROADMAP")
print(reasoner.get_current_roadmap())

print()

print("ANSWER")
print(reasoner.answer())