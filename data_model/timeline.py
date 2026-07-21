"""
timeline.py
===========

Timeline container for MemoryAI.

Stores TimelineEvent objects grouped by date.

Contains no business logic.
"""

from __future__ import annotations

from collections import defaultdict
from datetime import date

from data_model.timeline_event import TimelineEvent


class Timeline:
    """
    Timeline container.

    Stores events grouped by date.
    """

    def __init__(self) -> None:
        self._events: dict[date, list[TimelineEvent]] = defaultdict(list)

    def add_event(self, event: TimelineEvent) -> None:
        """Add a timeline event."""
        self._events[event.date].append(event)

    def get_by_date(self, event_date: date) -> list[TimelineEvent]:
        """Return all events for a specific date."""
        return list(self._events.get(event_date, []))

    def dates(self) -> list[date]:
        """Return all dates in chronological order."""
        return sorted(self._events.keys())

    def events(self) -> list[TimelineEvent]:
        """Return every event in chronological order."""
        result: list[TimelineEvent] = []

        for d in self.dates():
            result.extend(self._events[d])

        return result

    def earliest(self) -> TimelineEvent | None:
        """Return the earliest event."""
        events = self.events()
        return events[0] if events else None

    def latest(self) -> TimelineEvent | None:
        """Return the latest event."""
        events = self.events()
        return events[-1] if events else None

    def __len__(self) -> int:
        return sum(len(events) for events in self._events.values())

    def __bool__(self) -> bool:
        return len(self) > 0
