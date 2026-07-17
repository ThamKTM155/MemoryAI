# =====================================
# KNOWLEDGE AGGREGATOR V1
# =====================================

from memory_search_v2 import search_memory


def aggregate(query):

    docs = search_memory(query)

    if not docs:
        return "Không tìm thấy tri thức."

    answer = []

    used = set()

    for doc in docs:

        title = doc.get("title", "")

        if title in used:
            continue

        used.add(title)

        answer.append(
            f"\n========== {title} ==========\n"
        )

        answer.append(
            doc.get("content", "")[:1200]
        )

    return "\n".join(answer)