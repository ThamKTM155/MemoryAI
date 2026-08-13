"""
LEGACY COMPONENT

Original Answer Pipeline
Retained for historical reference.

Retired during BUILD-70
MemoryService Gateway Migration
"""
from service.graph_builder import GraphBuilder
from service.relationship_builder import RelationshipBuilder

from service.knowledge_graph import KnowledgeGraph
from service.memory_query import MemoryQuery
from service.memory_assistant import MemoryAssistant


def run():

    print("=" * 50)
    print("MEMORY ASSISTANT")
    print("=" * 50)

    graph = KnowledgeGraph()

    nodes = GraphBuilder.build_many(

        [

            {
                "node_id": "BUILD-001",
                "node_type": "BUILD",
                "label": "Relationship Foundation",
            },

            {
                "node_id": "ADR-001",
                "node_type": "ADR",
                "label": "Memory Architecture",
            },

            {
                "node_id": "ROADMAP-001",
                "node_type": "ROADMAP",
                "label": "MemoryAI Roadmap",
            },

        ]

    )

    graph.add_nodes(nodes)

    relationships = RelationshipBuilder.build_many(

        [

            {
                "source_id": "BUILD-001",
                "target_id": "ADR-001",
                "relation_type": "implements",
            },

            {
                "source_id": "BUILD-001",
                "target_id": "ROADMAP-001",
                "relation_type": "supports",
            },

        ]

    )

    graph.add_relationships(relationships)

    query = MemoryQuery(graph)

    assistant = MemoryAssistant(query)

    result = assistant.ask("Show BUILD")

    print()

    print("QUESTION")
    print(result["question"])

    print()

    print("NODE")
    print(result["node"].node_id)

    print()

    print("SUMMARY")
    print(result["reflection"]["summary"])

    print()

    print("PLAN")

    print(result["plan"]["goal"])

    for step in result["plan"]["steps"]:

        print(step)

    assert result["node"].node_id == "BUILD-001"

    assert result["plan"]["goal"] == "Review BUILD-001"

    assert len(result["plan"]["steps"]) == 3

    print()

    print("PASS")


if __name__ == "__main__":

    run()