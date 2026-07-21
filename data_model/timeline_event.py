"""
timeline_event.py
=================

Data model for a single event in the MemoryAI timeline.

This module contains no business logic.
It is only used to transport timeline data between services.
"""

from dataclasses import dataclass, field
from datetime import date
from typing import Any


@dataclass(slots=True)
class TimelineEvent:
    """
    Represents a single event on the project timeline.
    """

    id: str
    date: date
    title: str
    event_type: str
    source: str

    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)