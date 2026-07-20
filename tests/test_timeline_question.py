import json

from core.memory_api import Memory
from core.reasoning.timeline_reasoner import TimelineReasoner

memory = Memory("05_Diary")
memory.load()

reasoner = TimelineReasoner(memory)

with open("tests/data/timeline_questions.json", encoding="utf-8") as f:
    test_data = json.load(f)

for group_name, group in test_data.items():

    print()
    print("=" * 70)
    print("GROUP :", group_name)
    print("CANONICAL :", group["canonical"])
    print("=" * 70)
    print(f"TOTAL QUESTIONS : {len(group['questions'])}")
    for i, q in enumerate(group["questions"], start=1):
        print()
        print(f"[{i}/{len(group['questions'])}] QUESTION : {q}")
        print(reasoner.answer(q))