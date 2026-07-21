"""
timeline_engine.py
==================

Timeline Engine

BUILD-22
Business Logic Layer
"""

from data_model.memory_record import MemoryRecord
from data_model.timeline import Timeline
from service.timeline_builder import TimelineBuilder


class TimelineEngine:
    """
    Build a Timeline from MemoryRecord objects.
    """

    def __init__(self) -> None:
        self._timeline = Timeline()

    def build(self, records: list[MemoryRecord]) -> Timeline:
        """
        Build timeline from memory records.
        """

        self._timeline = Timeline()

        events = TimelineBuilder.build_many(records)

        for event in events:
            self._timeline.add_event(event)

        return self._timeline

    def timeline(self) -> Timeline:
        """
        Return current timeline.
        """

        return self._timeline

    def latest(self):
        """
        Latest timeline event.
        """

        return self._timeline.latest()

    def earliest(self):
        """
        Earliest timeline event.
        """

        return self._timeline.earliest()