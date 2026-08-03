import argparse

from tools.graph_loader import (
    load_graph,
)

graph = load_graph()

nodes = graph["nodes"]
edges = graph["edges"]


def show_header():

    print("=" * 60)
    print("GRAPH EXPLORER")
    print("=" * 60)
    print()
    print(f"Nodes : {len(nodes)}")
    print(f"Edges : {len(edges)}")
    print()


def show_node_types():

    types = {}

    for node in nodes:
        t = node["type"]
        types[t] = types.get(t, 0) + 1

    print("NODE TYPES")
    print("-" * 40)

    for t in sorted(types):
        print(f"{t:<15} {types[t]}")

    print()


def show_relation_types():

    relations = {}

    for edge in edges:
        relation = edge["relation"]
        relations[relation] = relations.get(relation, 0) + 1

    print("RELATION TYPES")
    print("-" * 40)

    for relation in sorted(relations):
        print(f"{relation:<20} {relations[relation]}")

    print()


def show_projects():

    print("=" * 60)
    print("PROJECT CONTENT")
    print("=" * 60)

    projects = {}

    for edge in edges:

        if edge["relation"] == "BELONGS_TO":

            project = edge["to"]

            projects.setdefault(project, [])

            projects[project].append(edge["from"])

    for project in sorted(projects):

        print()

        print(f"[{project}]")

        print("-" * 40)

        for item in sorted(projects[project]):

            print(item)


parser = argparse.ArgumentParser()

parser.add_argument(
    "--all",
    action="store_true"
)

parser.add_argument(
    "--projects",
    action="store_true"
)

parser.add_argument(
    "--relations",
    action="store_true"
)

parser.add_argument(
    "--summary",
    action="store_true"
)

args = parser.parse_args()

show_header()

if (
    args.all
    or not (
        args.projects
        or args.relations
        or args.summary
    )
):
    show_node_types()
    show_relation_types()
    show_projects()

if args.projects:
    show_projects()

if args.relations:
    show_relation_types()

if args.summary:
    show_node_types()