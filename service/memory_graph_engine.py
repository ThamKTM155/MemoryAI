from service.memory_service import (
    MemoryService,
)

from service.memory_graph_repository import (
    MemoryGraphRepository,
)

from service.memory_keyword_repository import (
    MemoryKeywordRepository,
)

from service.memory_query_engine import (
    search_by_title,
)

def build_graph():

    memories = MemoryService.get_all_memories()

    keywords = MemoryKeywordRepository.load()

    graph = {}

    for memory in memories:

        title = memory.get(
            "title",
            ""
        )

        content = memory.get(
            "content",
            ""
        ).lower()

        graph[title] = set()

        current_keywords = set(
            keywords.get(
                title,
                []
            )
        )

        for other in memories:

            other_title = other.get(
                "title",
                ""
            )
            other_keywords = set(
                keywords.get(
                    other_title,
                    []
                )
            )
            common_keywords = (
                current_keywords
                &
                other_keywords
            )

            if other_title == title:
                continue

            if len(common_keywords) >= 5:

                graph[title].add(
                    other_title
                )

    for title in graph:

        graph[title] = sorted(
            list(
                graph[title]
            )
            )
    MemoryGraphRepository.save(
        graph
    )

    return graph

def get_related_titles(
    title,
):

    graph = MemoryGraphRepository.load()

    return graph.get(
        title,
        []
    )
def get_related_memories(
    title,
):

    titles = get_related_titles(
        title
    )

    memories = []

    for related_title in titles:

        memory = search_by_title(
            related_title
        )

        if memory:

            memories.append(
                memory
            )

    return memories