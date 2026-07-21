from service.graph_builder import GraphBuilder
from service.relationship_builder import RelationshipBuilder
from service.knowledge_graph import KnowledgeGraph


def run():

    print("=" * 50)
    print("KNOWLEDGE GRAPH")
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

    print()

    print("NEIGHBORS BUILD-001")

    neighbors = graph.neighbors("BUILD-001")

    for node in neighbors:

        print(node.node_id)

    print()

    print("RELATED BUILD-001")

    related = graph.related_nodes("BUILD-001")

    for node in related:

        print(node.node_id)

    assert len(neighbors) == 2
    assert len(related) == 2
    print()

    print("ALL NODES")
    print(len(graph.all_nodes()))

    print()

    print("ALL RELATIONSHIPS")
    print(len(graph.all_relationships()))

    print()

    print("HAS NODE BUILD-001")
    print(graph.has_node("BUILD-001"))

    print()

    print("HAS NODE BUILD-999")
    print(graph.has_node("BUILD-999"))

    print()

    print("HAS RELATIONSHIP")
    print(
        graph.has_relationship(
            "BUILD-001",
            "ADR-001"
        )
    )

    print()

    node = graph.find_node("ADR-001")

    print("FIND NODE")
    print(node.node_id)
    print(node.label)

    assert len(graph.all_nodes()) == 3
    assert len(graph.all_relationships()) == 2
    assert graph.has_node("BUILD-001")
    assert not graph.has_node("BUILD-999")
    assert graph.has_relationship("BUILD-001", "ADR-001")
    assert node.node_id == "ADR-001"
    print()
    print("PASS")


if __name__ == "__main__":
    run()