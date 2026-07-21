"""
test_timeline_engine.py
"""

from datetime import datetime

from data_model.memory_record import MemoryRecord
from service.timeline_engine import TimelineEngine


def run():

    records = [

        MemoryRecord(
            id="1",
            memory_type="BUILD",
            title="BUILD-001",
            content="...",
            project="MemoryAI",
            source="build1.md",
            created_at=datetime(2026, 7, 18),
        ),

        MemoryRecord(
            id="2",
            memory_type="BUILD",
            title="BUILD-002",
            content="...",
            project="MemoryAI",
            source="build2.md",
            created_at=datetime(2026, 7, 21),
        )

    ]

    engine = TimelineEngine()

    timeline = engine.build(records)

    print("=" * 50)
    print("TIMELINE ENGINE")
    print("=" * 50)

    print()

    print("TOTAL EVENTS")
    print(len(timeline))

    print()

    print("EARLIEST")

    print(engine.earliest().title)

    print()

    print("LATEST")

    print(engine.latest().title) 
if __name__ == "__main__":
    run()