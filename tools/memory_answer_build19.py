# ====================================
# MEMORY ANSWER V2
# Updated: 15/06/2026
# ====================================
from memory_api_v2 import ask_memory


def answer_memory(question):

    return ask_memory(question)


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