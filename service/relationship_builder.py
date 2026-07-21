"""
relationship_builder.py
=======================

Build Relationship objects.
"""

from data_model.relationship import Relationship


class RelationshipBuilder:
    """
    Factory for Relationship objects.
    """

    @staticmethod
    def build(
        source_id: str,
        target_id: str,
        relation_type: str,
        confidence: float = 1.0,
    ) -> Relationship:

        return Relationship(
            source_id=source_id,
            target_id=target_id,
            relation_type=relation_type,
            confidence=confidence,
        )

    @staticmethod
    def build_many(definitions):

        relationships = []

        for item in definitions:

            relationships.append(
                RelationshipBuilder.build(
                    source_id=item["source_id"],
                    target_id=item["target_id"],
                    relation_type=item["relation_type"],
                    confidence=item.get("confidence", 1.0),
                )
            )

        return relationships