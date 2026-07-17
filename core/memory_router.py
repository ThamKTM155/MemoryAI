"""
Memory Router
BUILD-24.2
"""

from core.memory_query import (
    query_project,
    query_keyword
)


def memory_query(project_intelligence, query_type, value):

    if query_type == "project":
        return query_project(project_intelligence, value)

    if query_type == "keyword":
        return query_keyword(project_intelligence, value)

    return None