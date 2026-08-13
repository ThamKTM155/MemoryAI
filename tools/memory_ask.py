import sys

sys.path.append(
    r"D:\MemoryAI"
)

from service.memory_answer_engine import (
    build_answer,
)

def ask(question):

    return build_answer(
        question
    )