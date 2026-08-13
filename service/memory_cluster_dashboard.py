from service.memory_cluster_engine import (
    build_clusters,
)


def print_clusters():

    clusters = build_clusters()

    print()
    print("MEMORY CLUSTERS")
    print("=" * 50)
    print()

    for index, cluster in enumerate(
        clusters,
        start=1
    ):

        print(
            f"CLUSTER {index}"
        )

        print(
            f"SIZE: {len(cluster)}"
        )

        print()

        for item in cluster:

            print(
                "-",
                item
            )

        print()