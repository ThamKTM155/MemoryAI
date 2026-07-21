"""
graph_engine.py
===============

Graph Engine
"""

from data_model.graph_node import GraphNode


class GraphEngine:

    def __init__(self):
        self._nodes = []

    def add(self, node: GraphNode):
        self._nodes.append(node)

    def add_many(self, nodes):
        self._nodes.extend(nodes)

    def all(self):
        return self._nodes

    def find_by_id(self, node_id: str):

        for node in self._nodes:
            if node.node_id == node_id:
                return node

        return None

    def find_by_type(self, node_type: str):

        return [
            node
            for node in self._nodes
            if node.node_type == node_type
        ]