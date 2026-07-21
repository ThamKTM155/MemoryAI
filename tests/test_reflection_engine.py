from service.graph_builder import GraphBuilder
from service.relationship_builder import RelationshipBuilder

from service.knowledge_graph import KnowledgeGraph
from service.memory_query import MemoryQuery
from service.context_builder import ContextBuilder
from service.reflection_engine import ReflectionEngine


def run():

    print("=" * 50)
    print("REFLECTION ENGINE")
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

    builder = ContextBuilder(query)

    reflector = ReflectionEngine()

    context = builder.build("BUILD-001")

    result = reflector.reflect(context)

    print()

    print("NODE")
    print(result["node_id"])

    print()

    print("TYPE")
    print(result["node_type"])

    print()

    print("LABEL")
    print(result["label"])

    print()

    print("RELATED COUNT")
    print(result["related_count"])

    print()

    print("RELATED")

    for node in result["related_nodes"]:
        print(node)

    print()

    print("SUMMARY")
    print(result["summary"])

    assert result["node_id"] == "BUILD-001"
    assert result["node_type"] == "BUILD"
    assert result["related_count"] == 2
    assert len(result["related_nodes"]) == 2

    print()
    print("PASS")


if __name__ == "__main__":

    run()