"""
reasoning_engine.py
===================

Reasoning Engine V1
"""

from service.memory_query import MemoryQuery


class ReasoningEngine:

    def __init__(self, query: MemoryQuery):

        self.query = query

    def answer(self, question: str):

        text = question.strip().lower()

        if "build" in text:

            return self.query.find_builds()

        if "adr" in text:

            return self.query.find_adrs()

        if "roadmap" in text:

            return self.query.find_roadmaps()

        if "note" in text:

            return self.query.find_notes()

        return []