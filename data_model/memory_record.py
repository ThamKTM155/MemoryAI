"""
Memory Record
BUILD-21
Canonical Memory Object
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict
from datetime import datetime


@dataclass
class MemoryRecord:
    """Canonical Memory Record"""
    # Identity

    id: str
    memory_type: str
    # Content

    title: str
    content: str
    project: str
    source: str
    # Management

    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    status: str = "active"
    # Relations

    tags: List[str] = field(default_factory=list)
    relations: List[str] = field(default_factory=list)
    def to_dict(self) -> Dict:
        """Convert MemoryRecord to dictionary."""
        return asdict(self)