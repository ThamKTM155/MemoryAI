from service.memory_graph_repository import (
    MemoryGraphRepository,
)

def get_top_hubs(
    limit=10,
):

    graph = MemoryGraphRepository.load()

    data = []

    for title, links in graph.items():

        data.append(
            (
                len(links),
                title,
            )
        )

    data.sort(
        reverse=True
    )

    return data[:limit]