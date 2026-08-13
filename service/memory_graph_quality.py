from service.memory_graph_repository import (
    MemoryGraphRepository,
)

def find_heavy_nodes(
    threshold=20,
):

    graph = MemoryGraphRepository.load()

    result = []

    for title, links in graph.items():

        if len(links) >= threshold:

            result.append(
                (
                    len(links),
                    title,
                )
            )

    result.sort(
        reverse=True
    )

    return result