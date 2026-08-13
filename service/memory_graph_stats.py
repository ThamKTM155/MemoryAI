from service.memory_graph_repository import (
    MemoryGraphRepository,
)

def get_graph_stats():

    graph = MemoryGraphRepository.load()

    total_nodes = len(
        graph
    )

    total_links = 0

    for links in graph.values():

        total_links += len(
            links
        )

    average_links = 0

    if total_nodes:

        average_links = (
            total_links
            /
            total_nodes
        )

    return {
        "nodes": total_nodes,
        "links": total_links,
        "avg_links": round(
            average_links,
            2
        ),
    }