from service.relationship_builder import RelationshipBuilder
from service.relationship_engine import RelationshipEngine


def run():

    print("=" * 50)
    print("RELATIONSHIP ENGINE")
    print("=" * 50)

    engine = RelationshipEngine()

    definitions = [

        {
            "source_id": "BUILD-001",
            "target_id": "ROADMAP-001",
            "relation_type": "implements",
        },

        {
            "source_id": "BUILD-001",
            "target_id": "ADR-001",
            "relation_type": "follows",
        },

        {
            "source_id": "ADR-001",
            "target_id": "BUILD-004",
            "relation_type": "affects",
        },

    ]

    relationships = RelationshipBuilder.build_many(definitions)

    engine.add_many(relationships)

    print()

    print("TOTAL RELATIONSHIPS")
    print(len(engine.all()))

    print()

    print("SOURCE BUILD-001")
    print(len(engine.find_by_source("BUILD-001")))

    print()

    print("TARGET ADR-001")
    print(len(engine.find_by_target("ADR-001")))

    print()

    print("RELATED BUILD-001")
    print(len(engine.find_related("BUILD-001")))

    assert len(engine.all()) == 3

    assert len(engine.find_by_source("BUILD-001")) == 2

    assert len(engine.find_by_target("ADR-001")) == 1

    assert len(engine.find_related("BUILD-001")) == 2

    print()

    print("PASS")


if __name__ == "__main__":
    run()