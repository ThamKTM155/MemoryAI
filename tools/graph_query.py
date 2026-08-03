import argparse

from tools.graph_loader import (
    load_graph,
)

graph = load_graph()

nodes = graph["nodes"]
edges = graph["edges"]

def print_relationships(found):

    print()

    print("=" * 60)
    print("RELATIONSHIPS")
    print("=" * 60)

    has_relation = False

    for edge in edges:

        if (
            edge["from"] == found["id"]
            and (
                not args.related
                or edge["relation"] == "RELATED_TO"
            )
        ):

            has_relation = True

            print(
                f'{edge["relation"]:<15} -> {edge["to"]}'
            )

    if not has_relation:

        print("No relationships.")

def query_by_project(project):

    print("=" * 60)
    print(f"PROJECT : {project}")
    print("=" * 60)

    for node in nodes:

        if node.get("project") == project:

            print(node["id"])

def generate_insight_text(found, related):

    if related >= 4:

        return (
            f"{found['id']} is a connected document.\n\n"
            f"It references {related} related documents."
        )

    elif related >= 2:

        return (
            f"{found['id']} has a moderate number "
            f"of relationships."
        )

    else:

        return (
            f"{found['id']} has few relationships."
        )

def generate_summary_text(found, related):

    text = []

    text.append(
        f"{found['id']} belongs to project "
        f"{found.get('project')}."
    )

    text.append(
        f"This document has "
        f"{related} related document(s)."
    )

    return "\n".join(text)

def print_summary(found):

    related = 0

    for edge in edges:

        if edge["from"] == found["id"]:

            if edge["relation"] == "RELATED_TO":

                related += 1

    print()

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print(f"Document : {found['id']}")
    print(f"Project  : {found.get('project')}")
    print(f"Related  : {related}")

    print()

    text = generate_summary_text(
        found,
        related
    )

    print(text)

def print_insight(found):

    related = 0

    for edge in edges:

        if (
            edge["from"] == found["id"]
            and edge["relation"] == "RELATED_TO"
        ):

            related += 1

    print()

    print("=" * 60)
    print("INSIGHT")
    print("=" * 60)

    text = generate_insight_text(
        found,
        related
    )

    print(text)

def query_by_node(node_id):

    found = None

    for node in nodes:

        if node["id"] == node_id:

            found = node

            break

    if found is None:

        print("Node not found.")

        return

    print("=" * 60)
    print("NODE")
    print("=" * 60)

    for key, value in found.items():

        print(f"{key:<12}: {value}")

    print_relationships(found)

    print_summary(found)

    print_insight(found)
parser = argparse.ArgumentParser()

parser.add_argument(
    "node",
    nargs="?"
)

parser.add_argument(
    "--related",
    action="store_true"
)

parser.add_argument(
    "--project"
)

args = parser.parse_args()

if args.project:

    query_by_project(args.project)

    exit()

query_by_node(args.node)