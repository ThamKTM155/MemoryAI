from service.graph_builder import GraphBuilder
from service.graph_engine import GraphEngine


def run():

    print("=" * 50)
    print("GRAPH ENGINE")
    print("=" * 50)

    definitions = [

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

    nodes = GraphBuilder.build_many(definitions)

    engine = GraphEngine()

    engine.add_many(nodes)

    print()

    print("TOTAL NODES")
    print(len(engine.all()))

    print()

    build = engine.find_by_id("BUILD-001")

    print("FIND BY ID")
    print(build.node_id)
    print(build.label)

    print()

    builds = engine.find_by_type("BUILD")

    print("BUILD NODES")
    print(len(builds))

    assert len(engine.all()) == 4
    assert build.node_id == "BUILD-001"
    assert len(builds) == 2

    print()
    print("PASS")


if __name__ == "__main__":
    run()