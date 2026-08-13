"""
Memory Authority Engine
BUILD-69J
"""
from service.memory_importance_engine import (
    get_importance_score,
)
from service.memory_usage_engine import (
    get_usage_score,
)
from service.memory_freshness_engine import (
    get_freshness_score,
)
from service.memory_confidence_engine import (
    get_confidence_score,
)

FOUNDATION_TITLES = {

    "Mục đích": 100,

    "Vai trò của ThamAI": 100,

    "Sứ mệnh": 100,

    "OWNER VISION": 100,

    "SYSTEM CONSTITUTION": 100,

    "MEMORYAI MISSION": 90,

    "MEMORYAI PRINCIPLES": 90,

    "MEMORYAI VALUES": 90,

    "Mục tiêu số 1": 80,

    "Mục tiêu cuối cùng": 80,

}


def get_authority_score(
    memory,
):

    title = memory.get(
        "title",
        ""
    )

    return FOUNDATION_TITLES.get(
        title,
        0
    )

def get_final_score(
    memory,
):

    importance = get_importance_score(
        memory
    )

    authority = get_authority_score(
        memory
    )

    title = memory.get(
        "title",
        ""
    )

    usage = get_usage_score(
        title
    )

    freshness = get_freshness_score(
        title
    )
    confidence = get_confidence_score(
        title
    )
    return (
        importance
        +
        authority * 10
        +
        usage * 20
        +
        freshness
        +
        confidence
    )

def rank_by_final_score(
    memories,
):

    ranked = []

    for memory in memories:

        score = get_final_score(
            memory
        )

        ranked.append(
            (
                score,
                memory
            )
        )

    ranked.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return ranked