"""
relationship_engine.py
======================

Relationship Engine
"""

from data_model.relationship import Relationship


class RelationshipEngine:

    def __init__(self):

        self._relationships = []

    def add(self, relationship: Relationship):

        self._relationships.append(relationship)

    def add_many(self, relationships):

        self._relationships.extend(relationships)

    def all(self):

        return self._relationships

    def find_by_source(self, source_id: str):

        return [
            r
            for r in self._relationships
            if r.source_id == source_id
        ]

    def find_by_target(self, target_id: str):

        return [
            r
            for r in self._relationships
            if r.target_id == target_id
        ]

    def find_related(self, node_id: str):

        return [
            r
            for r in self._relationships
            if r.source_id == node_id
            or r.target_id == node_id
        ]