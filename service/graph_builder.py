"""
graph_builder.py
================

Graph Builder
"""

from data_model.graph_node import GraphNode


class GraphBuilder:

    @staticmethod
    def build(
        node_id: str,
        node_type: str,
        label: str,
        metadata=None,
    ):

        if metadata is None:
            metadata = {}

        return GraphNode(
            node_id=node_id,
            node_type=node_type,
            label=label,
            metadata=metadata,
        )

    @staticmethod
    def build_many(definitions):

        nodes = []

        for item in definitions:

            nodes.append(
                GraphBuilder.build(
                    node_id=item["node_id"],
                    node_type=item["node_type"],
                    label=item["label"],
                    metadata=item.get("metadata", {}),
                )
            )

        return nodes