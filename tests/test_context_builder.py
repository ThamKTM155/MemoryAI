from service.graph_builder import GraphBuilder
from service.relationship_builder import RelationshipBuilder

from service.knowledge_graph import KnowledgeGraph
from service.memory_query import MemoryQuery
from service.context_builder import ContextBuilder


def run():

    print("=" * 50)
    print("CONTEXT BUILDER")
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

    context = builder.build("BUILD-001")

    print()

    print("NODE")
    print(context["node"].node_id)

    print(context["node"].label)

    print()

    print("RELATED")

    for node in context["related"]:

        print(node.node_id)

    assert context["node"].node_id == "BUILD-001"
    assert len(context["related"]) == 2

    print()
    print("PASS")


if __name__ == "__main__":

    run()