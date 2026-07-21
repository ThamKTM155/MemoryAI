"""
reflection_engine.py
====================

Reflection Engine
"""


class ReflectionEngine:

    def reflect(self, context):

        if context is None:
            return None

        node = context["node"]
        related = context["related"]

        return {

            "node_id": node.node_id,
            "node_type": node.node_type,
            "label": node.label,

            "related_count": len(related),

            "related_nodes": [

                item.node_id

                for item in related

            ],

            "summary":

                f"{node.node_id} "

                f"({node.node_type}) "

                f"has {len(related)} related node(s)."

        }