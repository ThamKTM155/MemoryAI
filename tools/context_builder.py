"""
========================================================

MemoryAI
BUILD-037

Module:
context_builder.py

Description:
Context Builder.

Chịu trách nhiệm:

- Ghép Ranked Memories
- Tạo Context cho AI

========================================================
"""

from typing import List, Dict


SEPARATOR = "\n" + "=" * 80 + "\n"


def format_memory(
    memory: Dict,
    index: int
) -> str:
    """
    Format một Memory thành text.
    """

    lines = []

    lines.append(
        f"Memory #{index}"
    )

    lines.append("-" * 40)

    for key, value in memory.items():

        if key == "_score":
            continue

        lines.append(
            f"{key}: {value}"
        )

    return "\n".join(lines)


def build_context(
    memories: List[Dict]
) -> str:
    """
    Build Context cho AI.
    """

    if not memories:

        return ""

    blocks = []

    for idx, memory in enumerate(
        memories,
        start=1
    ):

        blocks.append(
            format_memory(
                memory,
                idx
            )
        )

    return SEPARATOR.join(blocks)