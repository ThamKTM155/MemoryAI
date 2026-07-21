"""
test_timeline_builder.py
========================

Unit tests for TimelineBuilder.
"""

from datetime import datetime

from data_model.memory_record import MemoryRecord
from service.timeline_builder import TimelineBuilder


def create_record() -> MemoryRecord:
    return MemoryRecord(
        id="MEM-001",
        memory_type="BUILD",
        title="BUILD-22 Started",
        content="Start BUILD-22",
        project="MemoryAI",
        source="build22.md",
        created_at=datetime(2026, 7, 21, 10, 30),
        tags=["build", "timeline"],
    )


def run():

    print("=" * 50)
    print("TIMELINE BUILDER")
    print("=" * 50)

    record = create_record()

    event = TimelineBuilder.build(record)

    print()
    print("SINGLE BUILD")
    print(event.id)
    print(event.title)
    print(event.event_type)

    records = [
        create_record(),
        create_record(),
        create_record(),
    ]

    events = TimelineBuilder.build_many(records)

    print()
    print("MULTI BUILD")
    print(len(events))

    assert event.id == record.id
    assert event.title == record.title
    assert event.event_type == record.memory_type
    assert event.source == record.source
    assert event.date == record.created_at.date()
    assert event.tags == record.tags

    assert len(events) == 3

    print()
    print("PASS")


if __name__ == "__main__":
    run()