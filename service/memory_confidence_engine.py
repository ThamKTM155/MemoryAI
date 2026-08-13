from service.memory_confidence_repository import (
    MemoryConfidenceRepository,
)

DEFAULT_SCORE = 50

def get_confidence_score(
    title,
):

    data = (
        MemoryConfidenceRepository.load()
    )

    return data.get(
        title,
        DEFAULT_SCORE
    )

def increase_confidence(
    title,
    amount=1,
):

    data = (
        MemoryConfidenceRepository.load()
    )

    current = data.get(
        title,
        DEFAULT_SCORE
    )

    data[title] = min(
        100,
        current + amount
    )

    MemoryConfidenceRepository.save(
        data
    )
def decrease_confidence(
    title,
    amount=1,
):

    data = (
        MemoryConfidenceRepository.load()
    )

    current = data.get(
        title,
        DEFAULT_SCORE
    )

    data[title] = max(
        0,
        current - amount
    )

    MemoryConfidenceRepository.save(
        data
    )