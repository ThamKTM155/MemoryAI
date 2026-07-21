from service.relationship_builder import RelationshipBuilder
def run():

    print("=" * 50)
    print("RELATIONSHIP BUILDER")
    print("=" * 50)

    relationship = RelationshipBuilder.build(
        source_id="BUILD-001",
        target_id="ROADMAP-001",
        relation_type="implements",
    )
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
    ]
    relationships = RelationshipBuilder.build_many(definitions)

    assert relationship.source_id == "BUILD-001"
    assert relationship.target_id == "ROADMAP-001"
    assert relationship.relation_type == "implements"

    assert len(relationships) == 2

    print()

    print("SINGLE BUILD")

    print()

    print("MULTI BUILD")

    print()

    print("PASS")

if __name__ == "__main__":
    run()

 