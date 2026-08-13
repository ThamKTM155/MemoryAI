from service.memory_graph_explorer import (
    explore_graph,
)

def get_explorer_stats(
    title,
    depth=2,
):

    data = explore_graph(
        title,
        depth
    )

    levels = {}

    for level, node in data:

        levels[level] = (
            levels.get(
                level,
                0
            )
            + 1
        )

    return {
        "total_nodes": len(data),
        "levels": levels,
    }