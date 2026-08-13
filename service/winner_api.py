from service.winner_memory_search import (
    get_best_titles,
)

from service.winner_memory_search import (
    get_best_patterns,
)

from service.winner_memory_search import (
    get_best_topics,
)
def get_title_advice(
    topic,
):

    return {

        "topic": topic,

        "winner_titles":
        get_best_titles(
            topic
        ),

        "winner_patterns":
        get_best_patterns()[:5]
    }
def suggest_title_seed(
    topic,
):

    data = (
        get_title_advice(
            topic
        )
    )

    titles = (
        data[
            "winner_titles"
        ]
    )

    if titles:

        return titles[0]

    return None

def build_winner_prompt(
    topic,
    title_limit=5,
    pattern_limit=5,
):

    advice = (
        get_title_advice(
            topic
        )
    )

    titles = (
        advice[
            "winner_titles"
        ][:title_limit]
    )

    patterns = (
        advice[
            "winner_patterns"
        ][:pattern_limit]
    )

    lines = []

    lines.append(
        f"TOPIC: {topic}"
    )

    lines.append("")

    lines.append(
        "TOP WINNER TITLES"
    )

    lines.append("")

    for title in titles:

        lines.append(
            f"- {title}"
        )

    lines.append("")
    lines.append(
        "TOP WINNER PATTERNS"
    )
    lines.append("")

    for pattern in patterns:

        lines.append(
            f"- {pattern}"
        )

    lines.append("")
    lines.append(
        "Hãy tạo nội dung mới dựa trên các mẫu thành công ở trên."
    )

    lines.append(
        "Không sao chép nguyên văn."
    )

    lines.append(
        "Giữ phong cách tương tự nhưng tạo giá trị mới."
    )

    return "\n".join(
        lines
    )