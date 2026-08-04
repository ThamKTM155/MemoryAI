def analyze(knowledge):

    impact = {}

    if (
        knowledge.get("document_role") == "core_document"
        and knowledge.get("impact_level") == "high"
    ):

        impact["change_warning"] = True

    return impact