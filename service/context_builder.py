"""
context_builder.py
==================

Context Builder
"""

from service.memory_query import MemoryQuery


class ContextBuilder:

    def __init__(self, query: MemoryQuery):

        self.query = query

    def build(self, node_id):

        node = None

        for item in self.query.all_nodes():

            if item.node_id == node_id:
                node = item
                break

        if node is None:

            return None

        related = self.query.find_related(node_id)

        return {

            "node": node,

            "related": related,

        }