from service.memory_graph_engine import (
    get_related_titles,
)
from service.memory_graph_repository import (
    MemoryGraphRepository,
)
def print_relationships(
    title,
):

    related = get_related_titles(
        title
    )

    print()

    print(
        "MEMORY:",
        title
    )

    print(
        "=" * 50
    )

    print(
        "LINKS:",
        len(related)
    )

    print()

    for item in related:

        print(
            "-",
            item
        )

    print()

def get_top_relationships(
    limit=10,
):

    graph = (
        MemoryGraphRepository.load()
    )

    ranked = []

    for title, links in graph.items():

        ranked.append(
            (
                len(links),
                title
            )
        )

    ranked.sort(
        reverse=True
    )

    return ranked[:limit]

def print_top_relationships(
    limit=10,
):

    data = get_top_relationships(
        limit
    )

    print()

    print(
        "TOP CONNECTED MEMORIES"
    )

    print(
        "=" * 50
    )

    for count, title in data:

        print(
            title,
            "->",
            count,
            "links"
        )

    print()

def print_graph_tree(
    title,
    limit=10,
):

    related = get_related_titles(
        title
    )

    print()

    print(title)

    print()

    for item in related[:limit]:

        print(
            "├─",
            item
        )

    print()