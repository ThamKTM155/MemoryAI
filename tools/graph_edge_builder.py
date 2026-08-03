from tools.graph_relationship_parser import extract_relationships


def create_edges(node):

    edges = []

    # BELONGS_TO
    if node["project"]:

        edges.append(

            {
                "from": node["id"],
                "to": node["project"],
                "relation": "BELONGS_TO"
            }

        )

    # Chỉ Document mới có thể khai báo quan hệ
    if node["type"] == "DOCUMENT":

        relationships = extract_relationships(node["path"])

        for item in relationships:

            edges.append(

                {
                    "from": node["id"],
                    "to": item["target"],
                    "relation": item["relation"]
                }

            )

    return edges