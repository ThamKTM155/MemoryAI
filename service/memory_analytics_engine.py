from service.memory_importance_engine import (
    get_importance_score,
)

from service.memory_authority_engine import (
    get_authority_score,
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

from service.memory_authority_engine import (
    get_final_score,
)
def explain_score(
    memory,
):

    title = memory.get(
        "title",
        ""
    )

    return {

        "title": title,

        "importance":
            get_importance_score(
                memory
            ),

        "authority":
            get_authority_score(
                memory
            ),

        "usage":
            get_usage_score(
                title
            ),

        "freshness":
            get_freshness_score(
                title
            ),

        "confidence":
            get_confidence_score(
                title
            ),

        "final":
            get_final_score(
                memory
            ),
    }
def print_score_report(
    memory
):
    data = explain_score(
        memory
    )

    print()

    print(
        "TITLE:",
        data["title"]
    )

    print(
        "Importance:",
        data["importance"]
    )

    print(
        "Authority :",
        data["authority"]
    )

    print(
        "Usage     :",
        data["usage"]
    )

    print(
        "Freshness :",
        data["freshness"]
    )

    print(
        "Confidence:",
        data["confidence"]
    )

    print(
        "Final     :",
        data["final"]
    )

    print()