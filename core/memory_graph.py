"""
Memory Graph
BUILD-30.0
"""


def build_memory_graph(memory_db):
    """
    Xây dựng Knowledge Graph hai chiều.
    """

    graph = {}

    # ==========================================
    # 1. Build từ relationships
    # ==========================================

    relationships = memory_db.get("relationships", [])

    for relation in relationships:

        add_bidirectional(
            graph,
            relation["from"],
            relation["to"],
            relation["type"]
        )

    # ==========================================
    # 2. Build từ Raw Data
    # ==========================================

    build_keyword_graph(
        graph,
        memory_db
    )

    build_decision_graph(
        graph,
        memory_db
    )

    build_lesson_graph(
        graph,
        memory_db
    )

    build_task_graph(
        graph,
        memory_db
    )

    return graph
def get_related_memory(graph, node):
    """
    Lấy tất cả node liên quan.
    """

    return graph.get(node, [])


def get_related_by_type(graph, node, relation_type):
    """
    Lọc theo loại quan hệ.
    """

    results = []

    for item in graph.get(node, []):

        if item["type"] == relation_type:
            results.append(item["to"])

    return results


def get_neighbors(graph, node):
    """
    Lấy tất cả node hàng xóm.
    """

    return [item["to"] for item in graph.get(node, [])]

def add_edge(graph, source, target, relation):
    """
    Thêm cạnh vào Graph (không tạo cạnh trùng).
    """

    if source not in graph:
        graph[source] = []

    edge = {
        "to": target,
        "type": relation
    }

    if edge not in graph[source]:
        graph[source].append(edge)

def add_bidirectional(graph, source, target, relation):

    add_edge(
        graph,
        source,
        target,
        relation
    )

    add_edge(
        graph,
        target,
        source,
        "REVERSE_" + relation
    )

def build_keyword_graph(graph, memory_db):

    for item in memory_db.get("keywords", []):

        add_bidirectional(
            graph,
            item["diary_id"],
            item["keyword"],
            "HAS_KEYWORD"
        )

def build_decision_graph(graph, memory_db):

    for item in memory_db.get("decisions", []):

        add_bidirectional(
            graph,
            item["diary_id"],
            item["decision"],
            "HAS_DECISION"
        )

def build_lesson_graph(graph, memory_db):

    for item in memory_db.get("lessons", []):

        add_bidirectional(
            graph,
            item["diary_id"],
            item["lesson"],
            "HAS_LESSON"
        )

def build_task_graph(graph, memory_db):

    for item in memory_db.get("tasks", []):

        add_bidirectional(
            graph,
            item["diary_id"],
            item["task"],
            "HAS_TASK"
        )