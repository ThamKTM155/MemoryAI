"""
Memory Usage Engine
BUILD-69K
"""

from service.memory_usage_repository import (
    MemoryUsageRepository,
)


def increase_usage(
    title,
):

    data = (
        MemoryUsageRepository.load()
    )

    data[title] = (
        data.get(
            title,
            0
        )
        + 1
    )

    MemoryUsageRepository.save(
        data
    )


def get_usage_score(
    title,
):

    data = (
        MemoryUsageRepository.load()
    )

    return data.get(
        title,
        0
    )