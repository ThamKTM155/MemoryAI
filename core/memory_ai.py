"""
BUILD-004.2A
MemoryAI Unified API V1
"""

from core.memory_api import Memory
from core.routing.smart_router import SmartRouter
from core.reasoning.timeline_reasoner import TimelineReasoner


class MemoryAI:

    def __init__(self):

        self.memory = Memory("05_Diary")
        self.memory.load()

        self.router = SmartRouter()

        self.timeline = TimelineReasoner(self.memory)

    def answer(self, question: str):

        route = self.router.route(question)

        if route == "timeline":
            return self.timeline.answer(question)

        return f"Module '{route}' chưa được triển khai."

    def save_experience(self, experience):

        return self.memory.save_experience(experience)