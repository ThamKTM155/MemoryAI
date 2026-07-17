import os

MEMORY_FILE = (
    r"D:\MemoryAI\09_AI_Memory\memory_context.txt"
)


def ask_memory(query):

    if not os.path.exists(
        MEMORY_FILE
    ):
        return (
            "Không tìm thấy "
            "memory_context.txt"
        )

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        text = f.read()

    query = query.lower()

    chunks = text.split(
        "=" * 80
    )

    matches = []

    for chunk in chunks:

        score = (
            chunk.lower()
            .count(query)
        )

        if score > 0:

            matches.append(
                (
                    score,
                    chunk
                )
            )

    if not matches:

        return (
            "Không tìm thấy "
            "thông tin liên quan."
        )

    matches.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return (
        matches[0][1]
        [:2000]
    )


if __name__ == "__main__":

    while True:

        q = input(
            "\n🧠 Ask Memory: "
        )

        if q.lower() in [
            "exit",
            "quit"
        ]:
            break

        print(
            "\n"
            + ask_memory(q)
        )