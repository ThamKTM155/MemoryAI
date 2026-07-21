from service.graph_builder import GraphBuilder
from service.relationship_builder import RelationshipBuilder
from service.knowledge_graph import KnowledgeGraph
from service.memory_query import MemoryQuery


def run():

    print("=" * 50)
    print("MEMORY QUERY")
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
                "node_id": "BUILD-002",
                "node_type": "BUILD",
                "label": "Timeline Foundation",
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

    print()

    builds = query.find_builds()

    print("BUILDS")

    for node in builds:
        print(node.node_id)

    print()

    adrs = query.find_adrs()

    print("ADRS")

    for node in adrs:
        print(node.node_id)

    print()

    related = query.find_related("BUILD-001")

    print("RELATED BUILD-001")

    for node in related:
        print(node.node_id)

    assert len(builds) == 2
    assert len(adrs) == 1
    assert len(related) == 2

    print()
    print("PASS")


if __name__ == "__main__":
    run()