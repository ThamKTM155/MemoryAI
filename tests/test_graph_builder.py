from service.graph_builder import GraphBuilder


def run():

    print("=" * 50)
    print("GRAPH BUILDER")
    print("=" * 50)

    print()

    print("SINGLE BUILD")

    node = GraphBuilder.build(
        node_id="BUILD-001",
        node_type="BUILD",
        label="Relationship Foundation",
    )

    print(node.node_id)
    print(node.node_type)
    print(node.label)

    definitions = [

        {
            "node_id": "ROADMAP-001",
            "node_type": "ROADMAP",
            "label": "MemoryAI Roadmap",
        },

        {
            "node_id": "ADR-001",
            "node_type": "ADR",
            "label": "Memory Architecture",
        },

        {
            "node_id": "BUILD-002",
            "node_type": "BUILD",
            "label": "Timeline Foundation",
        },

    ]

    nodes = GraphBuilder.build_many(definitions)

    print()

    print("MULTI BUILD")
    print(len(nodes))

    assert node.node_id == "BUILD-001"
    assert node.node_type == "BUILD"
    assert node.label == "Relationship Foundation"

    assert len(nodes) == 3

    print()

    print("PASS")


if __name__ == "__main__":
    run()