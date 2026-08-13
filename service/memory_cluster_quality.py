from service.memory_cluster_engine import (
    build_clusters,
)

def get_isolated_memories():

    clusters = build_clusters()

    isolated = []

    for cluster in clusters:

        if len(cluster) == 1:

            isolated.append(
                cluster[0]
            )

    return isolated