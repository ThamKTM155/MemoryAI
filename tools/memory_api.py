import os
from tools.memory_chat import chat
MEMORY_FILE = (
    r"D:\MemoryAI\09_AI_Memory\memory_context.txt"
)


def ask_memory(query):

    try:

        return chat(query)

    except Exception as e:

        return f"Lỗi MemoryAI: {e}"

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