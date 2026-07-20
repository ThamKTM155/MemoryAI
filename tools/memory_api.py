import os
from tools.memory_search import search_memory
MEMORY_FILE = (
    r"D:\MemoryAI\09_AI_Memory\memory_context.txt"
)


def ask_memory(query):

    result = search_memory(query)

    if result:

        return result

    return "Không tìm thấy thông tin liên quan."

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