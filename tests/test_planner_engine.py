from service.graph_builder import GraphBuilder
from service.relationship_builder import RelationshipBuilder

from service.knowledge_graph import KnowledgeGraph
from service.memory_query import MemoryQuery
from service.context_builder import ContextBuilder
from service.reflection_engine import ReflectionEngine
from service.planner_engine import PlannerEngine


def run():

    print("=" * 50)
    print("PLANNER ENGINE")
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

    context = ContextBuilder(query).build("BUILD-001")

    reflection = ReflectionEngine().reflect(context)

    planner = PlannerEngine()

    plan = planner.plan(reflection)

    print()

    print("GOAL")
    print(plan["goal"])

    print()

    print("STEPS")

    for step in plan["steps"]:
        print(step)

    assert plan["goal"] == "Review BUILD-001"
    assert len(plan["steps"]) == 3

    print()
    print("PASS")


if __name__ == "__main__":

    run()