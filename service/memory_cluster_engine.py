from service.memory_graph_repository import (
    MemoryGraphRepository,
)


def build_clusters():

    graph = MemoryGraphRepository.load()

    visited = set()

    clusters = []

    for node in graph:

        if node in visited:
            continue

        cluster = []

        stack = [node]

        while stack:

            current = stack.pop()

            if current in visited:
                continue

            visited.add(
                current
            )

            cluster.append(
                current
            )

            for related in graph.get(
                current,
                []
            ):

                if related not in visited:

                    stack.append(
                        related
                    )

        clusters.append(
            sorted(cluster)
        )

    return clusters