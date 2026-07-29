"""
========================================================

MemoryAI
BUILD-037

Module:
memory_retrieval.py

Description:
Core Retrieval Engine.

Chịu trách nhiệm:

- Load Memory Database
- Điều phối quá trình Search
- Điều phối Ranking
- Điều phối Context Builder

Không chứa thuật toán Search.

Không chứa thuật toán Ranking.

Không chứa Business Logic.

========================================================
"""

from tools.memory_repository import load_memory_database
from tools.memory_search import search_memory_raw
from tools.memory_ranking import rank_memories
from tools.context_builder import build_context
import tools.memory_optimizer as memory_optimizer

optimize_memories = memory_optimizer.optimize_memories

print(memory_optimizer.__file__)

class MemoryRetrieval:
    """
    Core Retrieval Engine
    """

    def __init__(self):

        self.memory_db = None

    def load_database(self):
        """
        Load memory database.
        """

        self.memory_db = load_memory_database()

        return self.memory_db

    def retrieve(self, query: str):
        """
        Main Retrieval Pipeline.

        query
            ↓
        Search
            ↓
        Ranking
            ↓
        Context Builder
            ↓
        Final Context
        """

        if self.memory_db is None:
            self.load_database()

        candidates = search_memory_raw(
            query=query,
            memory_db=self.memory_db
        )
        if not candidates:
            return "❌ Không tìm thấy dữ liệu phù hợp."
        ranked = rank_memories(
            query=query,
            memories=candidates
        )
        optimized = optimize_memories(
            ranked
        )

        if not ranked:
            return "❌ Không có kết quả sau khi xếp hạng."
        context = build_context(
            memories=optimized
        )

        return context


def retrieve_context(query: str):
    """
    Public API.

    Example

    context = retrieve_context(
        "Memory Database"
    )
    """

    engine = MemoryRetrieval()

    return engine.retrieve(query)