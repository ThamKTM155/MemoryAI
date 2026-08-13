from service.memory_graph_engine import (
    get_related_titles,
)
def explore_graph(
    title,
    depth=2,
):

    visited = set()

    result = []

    def dfs(
        current,
        level,
    ):

        if level > depth:
            return

        if current in visited:
            return

        visited.add(
            current
        )

        result.append(
            (
                level,
                current
            )
        )

        for related in get_related_titles(
            current
        ):

            dfs(
                related,
                level + 1
            )

    dfs(
        title,
        0
    )

    return result
def print_explorer(
    title,
    depth=2,
):

    data = explore_graph(
        title,
        depth
    )

    print()

    print(
        "GRAPH EXPLORER"
    )

    print(
        "=" * 50
    )

    print()

    for level, node in data:

        print(
            "  " * level
            +
            "├─ "
            +
            node
        )

    print()