from tools.graph_loader import (
    load_graph,
)


graph = load_graph()

nodes = graph["nodes"]
edges = graph["edges"]


def collect_facts(node_id):

    found = None

    for node in nodes:

        if node["id"] == node_id:

            found = node

            break

    if found is None:

        return None

    related_count = 0

    for edge in edges:

        if (
            edge["from"] == found["id"]
            and edge["relation"] == "RELATED_TO"
        ):

            related_count += 1

    facts = {}

    facts["id"] = found["id"]

    facts["type"] = found["type"]

    facts["project"] = found.get("project")

    facts["status"] = found.get("status")

    facts["related_count"] = related_count

    return facts
