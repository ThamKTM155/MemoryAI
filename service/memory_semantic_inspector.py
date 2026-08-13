from collections import defaultdict

from service.memory_service import (
    MemoryService,
)

def normalize_text(text):

    text = text.lower()

    text = text.replace("\n", " ")

    text = text.replace(".", " ")
    text = text.replace(",", " ")
    text = text.replace(":", " ")
    text = text.replace(";", " ")
    text = text.replace("!", " ")
    text = text.replace("?", " ")

    words = text.split()

    return set(words)


def similarity_score(
    text1,
    text2,
):

    words1 = normalize_text(text1)

    words2 = normalize_text(text2)

    if not words1 or not words2:
        return 0

    common = (
        len(
            words1.intersection(
                words2
            )
        )
    )

    total = (
        len(
            words1.union(
                words2
            )
        )
    )

    return round(
        common * 100 / total,
        2
    )


def find_similar_memories():

    memories = (
        MemoryService.get_all_memories()
    )

    results = []

    total = len(memories)

    for i in range(total):

        memory_a = memories[i]

        content_a = memory_a.get(
            "content",
            ""
        )

        for j in range(
            i + 1,
            total
        ):

            memory_b = memories[j]

            content_b = memory_b.get(
                "content",
                ""
            )

            score = similarity_score(
                content_a,
                content_b
            )

            if score >= 70:

                results.append(
                    {
                        "score": score,
                        "title_a":
                            memory_a.get(
                                "title",
                                ""
                            ),
                        "title_b":
                            memory_b.get(
                                "title",
                                ""
                            ),
                    }
                )

    return sorted(
        results,
        key=lambda x:
            x["score"],
        reverse=True
    )


def print_semantic_duplicates():

    data = (
        find_similar_memories()
    )

    print()

    print(
        "SEMANTIC DUPLICATES"
    )

    print(
        "=" * 50
    )

    print()

    print(
        "FOUND:",
        len(data)
    )

    print()

    for item in data[:20]:

        print(
            "[" +
            str(item["score"])
            + "%]"
        )

        print(
            item["title_a"]
        )

        print(
            item["title_b"]
        )

        print(
            "-" * 40
        )

    print()