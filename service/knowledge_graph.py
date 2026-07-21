"""
knowledge_graph.py
==================

Knowledge Graph
"""

from service.graph_engine import GraphEngine
from service.relationship_engine import RelationshipEngine


class KnowledgeGraph:

    def __init__(self):

        self.graph_engine = GraphEngine()
        self.relationship_engine = RelationshipEngine()

    # ==========================
    # NODE
    # ==========================

    def add_node(self, node):

        self.graph_engine.add(node)

    def add_nodes(self, nodes):

        self.graph_engine.add_many(nodes)

    # ==========================
    # RELATIONSHIP
    # ==========================

    def add_relationship(self, relationship):

        self.relationship_engine.add(relationship)

    def add_relationships(self, relationships):

        self.relationship_engine.add_many(relationships)
    # ==========================
    # ACCESS
    # ==========================

    def find_node(self, node_id):

        return self.graph_engine.find_by_id(node_id)

    def all_nodes(self):

        return self.graph_engine.all()

    def all_relationships(self):

        return self.relationship_engine.all()

    def has_node(self, node_id):

        return self.find_node(node_id) is not None

    def has_relationship(self, source_id, target_id):

        for relation in self.relationship_engine.all():

            if (
                relation.source_id == source_id
                and relation.target_id == target_id
            ):
                return True

        return False
    # ==========================
    # QUERY
    # ==========================

    def neighbors(self, node_id):

        neighbors = []

        for relation in self.relationship_engine.all():

            if relation.source_id == node_id:

                node = self.graph_engine.find_by_id(
                    relation.target_id
                )

                if node is not None:
                    neighbors.append(node)

        return neighbors

    def related_nodes(self, node_id):

        related = []

        for relation in self.relationship_engine.all():

            if relation.source_id == node_id:

                node = self.graph_engine.find_by_id(
                    relation.target_id
                )

                if node is not None:
                    related.append(node)

            elif relation.target_id == node_id:

                node = self.graph_engine.find_by_id(
                    relation.source_id
                )

                if node is not None:
                    related.append(node)

        return related

    def connected_nodes(self, node_id):

        return self.related_nodes(node_id)