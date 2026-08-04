def reason(facts):

    reasoning = {}

    if facts["related_count"] >= 4:

        reasoning["connected_document"] = True

    if (
        facts["project"] == "MemoryGraph"
        and facts["type"] == "DOCUMENT"
    ):

        reasoning["important_document"] = True
        
    return reasoning