"""
==========================================
MEMORY API V2
BUILD-19
==========================================
"""

from memory_search_v2 import search_memory


# ==========================================
# ASK MEMORY
# ==========================================

def ask_memory(question):

    if not question:

        return "Anh chưa nhập câu hỏi."

    return search_memory(question)


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    while True:

        q = input("\n🧠 Ask Memory V2: ").strip()

        if q.lower() in ["exit", "quit"]:

            break

        print()

        print(ask_memory(q))

        print("\n" + "=" * 80)