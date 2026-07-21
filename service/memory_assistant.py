"""
memory_assistant.py
===================

Memory Assistant
"""

from service.reasoning_engine import ReasoningEngine
from service.context_builder import ContextBuilder
from service.reflection_engine import ReflectionEngine
from service.planner_engine import PlannerEngine


class MemoryAssistant:

    def __init__(self, query):

        self.query = query

        self.reasoning = ReasoningEngine(query)

        self.context_builder = ContextBuilder(query)

        self.reflector = ReflectionEngine()

        self.planner = PlannerEngine()

    def ask(self, question):

        reasoning_result = self.reasoning.answer(question)

        if not reasoning_result:

            return None

        node = reasoning_result[0]

        context = self.context_builder.build(node.node_id)

        reflection = self.reflector.reflect(context)

        plan = self.planner.plan(reflection)

        return {

            "question": question,

            "node": node,

            "context": context,

            "reflection": reflection,

            "plan": plan,

        }