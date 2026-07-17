# ====================================
# MEMORY ANSWER V2
# Updated: 15/06/2026
# ====================================
from memory_api import ask_memory
import re

def answer_memory(question):

    result = ask_memory(question)

    keywords = [
        k.lower()
        for k in question.split()
    ]

    # tách theo section markdown

    blocks = re.split(
        r'\n(?=# )',
        result
    )

    best_block = ""

    best_score = 0

    for block in blocks:

        block_lower = block.lower()

        score = sum(
            1
            for k in keywords
            if k in block_lower
        )

        if score > best_score:

            best_score = score
            best_block = block

    if best_block:

        return best_block.strip()

    return result[:3000]
if __name__ == "__main__":

    while True:

        q = input(
            "\n🧠 Ask Memory: "
        ).strip()

        if q.lower() in [
            "exit",
            "quit"
        ]:
            break

        print("\n")

        print(
            answer_memory(q)
        )

        print(
            "\n" + "=" * 80
        )