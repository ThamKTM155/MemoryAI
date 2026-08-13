from service.memory_cluster_engine import (
    build_clusters,
)

def get_cluster_stats():

    clusters = build_clusters()

    sizes = []

    for cluster in clusters:

        sizes.append(
            len(cluster)
        )

    return {
        "clusters": len(clusters),
        "largest_cluster": max(sizes),
        "smallest_cluster": min(sizes),
        "isolated_clusters": sizes.count(1),
        "total_nodes": sum(sizes),
    }