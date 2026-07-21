"""
timeline_builder.py
===================

Build TimelineEvent objects from MemoryRecord objects.

BUILD-22
Transformation Layer
"""

from data_model.memory_record import MemoryRecord
from data_model.timeline_event import TimelineEvent


class TimelineBuilder:
    """
    Transform MemoryRecord objects into TimelineEvent objects.

    This class contains only transformation logic.
    """

    @staticmethod
    def build(record: MemoryRecord) -> TimelineEvent:
        """
        Convert a single MemoryRecord into a TimelineEvent.
        """

        return TimelineEvent(
            id=record.id,
            date=record.created_at.date(),
            title=record.title,
            event_type=record.memory_type,
            source=record.source,
            tags=list(record.tags),
            metadata={},
        )

    @staticmethod
    def build_many(records: list[MemoryRecord]) -> list[TimelineEvent]:
        """
        Convert multiple MemoryRecord objects into TimelineEvent objects.
        """

        return [
            TimelineBuilder.build(record)
            for record in records
        ]