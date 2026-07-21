from service.graph_builder import GraphBuilder
from service.knowledge_graph import KnowledgeGraph
from service.memory_query import MemoryQuery
from service.reasoning_engine import ReasoningEngine


def run():

    print("=" * 50)
    print("REASONING ENGINE")
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

    query = MemoryQuery(graph)

    reasoning = ReasoningEngine(query)

    print()

    print("QUESTION:")
    print("Show all BUILD")

    result = reasoning.answer("Show all BUILD")

    print()

    print("ANSWER:")

    for node in result:
        print(node.node_id)

    assert len(result) == 2

    print()

    print("QUESTION:")
    print("Show all ADR")

    result = reasoning.answer("Show all ADR")

    print()

    print("ANSWER:")

    for node in result:
        print(node.node_id)

    assert len(result) == 1

    print()

    print("QUESTION:")
    print("Show ROADMAP")

    result = reasoning.answer("Show ROADMAP")

    print()

    print("ANSWER:")

    for node in result:
        print(node.node_id)

    assert len(result) == 1

    print()
    print("PASS")


if __name__ == "__main__":
    run()