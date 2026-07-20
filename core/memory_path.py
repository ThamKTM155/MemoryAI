"""
Memory Path
BUILD-31.1
"""

from collections import deque


def find_path(graph, start, end):
    """
    Tìm đường đi ngắn nhất giữa hai node.
    Trả về đầy đủ thông tin từng bước.
    """

    if start == end:
        return []

    visited = set()

    queue = deque()

    queue.append(
        (
            start,
            []
        )
    )

    while queue:

        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        for relation in graph.get(current, []):

            neighbor = relation["to"]

            step = {
                "from": current,
                "to": neighbor,
                "type": relation["type"]
            }

            if neighbor == end:
                return path + [step]

            if neighbor not in visited:

                queue.append(
                    (
                        neighbor,
                        path + [step]
                    )
                )

    return None