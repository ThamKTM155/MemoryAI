def infer(facts, reasoning):

    knowledge = {}

    if reasoning.get("connected_document"):

        knowledge["document_role"] = "core_document"

    if (
        reasoning.get("important_document")
        and knowledge.get("document_role") == "core_document"
    ):

        knowledge["impact_level"] = "high"

    return knowledge