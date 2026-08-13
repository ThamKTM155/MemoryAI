"""
Memory Freshness Engine
BUILD-69L
"""

from datetime import datetime

from service.memory_freshness_repository import (
    MemoryFreshnessRepository,
)


def update_timestamp(
    title,
):

    data = (
        MemoryFreshnessRepository.load()
    )

    data[title] = (
        datetime.now().isoformat()
    )

    MemoryFreshnessRepository.save(
        data
    )


def get_timestamp(
    title,
):

    data = (
        MemoryFreshnessRepository.load()
    )

    return data.get(
        title
    )

def get_freshness_score(
    title,
):

    timestamp = get_timestamp(
        title
    )

    if not timestamp:

        return 0

    try:

        memory_time = (
            datetime.fromisoformat(
                timestamp
            )
        )

    except Exception:

        return 0

    age_days = (
        datetime.now()
        -
        memory_time
    ).days

    score = max(
        0,
        100 - age_days
    )

    return score