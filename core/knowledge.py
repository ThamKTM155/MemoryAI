"""
Knowledge Data Model
====================

Định nghĩa một Knowledge (tri thức)
được rút ra từ nhiều Experience.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Knowledge:

    id: str = ""

    category: str = ""

    topic: str = ""

    pattern: str = ""

    evidence: list = field(default_factory=list)

    sample_size: int = 0

    confidence: float = 0.0

    status: str = "ACTIVE"

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    updated_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )