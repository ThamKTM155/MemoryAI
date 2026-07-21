"""
memory_query.py
===============

Memory Query Engine
"""

from service.knowledge_graph import KnowledgeGraph


class MemoryQuery:

    def __init__(self, graph: KnowledgeGraph):

        self.graph = graph

    # ==========================
    # NODE
    # ==========================

    def all_nodes(self):

        return self.graph.all_nodes()

    def find_by_type(self, node_type):

        return [

            node

            for node in self.graph.all_nodes()

            if node.node_type == node_type

        ]

    # ==========================
    # COMMON TYPES
    # ==========================

    def find_builds(self):

        return self.find_by_type("BUILD")

    def find_adrs(self):

        return self.find_by_type("ADR")

    def find_roadmaps(self):

        return self.find_by_type("ROADMAP")

    def find_notes(self):

        return self.find_by_type("NOTE")

    # ==========================
    # GRAPH
    # ==========================

    def find_related(self, node_id):

        return self.graph.related_nodes(node_id)

    def neighbors(self, node_id):

        return self.graph.neighbors(node_id)