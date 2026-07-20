from core.memory_api import Memory
from core.reasoning.adr_reasoner import ADRReasoner

memory = Memory("05_Diary")
memory.load()

reasoner = ADRReasoner(memory)

print("=" * 60)
print("ADR REASONER")
print("=" * 60)

print()

print("LATEST ADR")
print(reasoner.get_latest_adr())

print()

print("ANSWER")
print(reasoner.answer())