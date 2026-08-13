from service.memory_service import (
    MemoryService,
)
from service.memory_retrieval_engine import (
    retrieve,
)

def get_all():

    return (
        MemoryService.get_all_memories()
    )


def search_by_title(
    keyword,
):

    keyword = (
        keyword.lower()
        .strip()
    )

    results = []

    memories = get_all()

    for memory in memories:

        title = (
            memory.get(
                "title",
                ""
            )
            .lower()
        )

        if keyword in title:

            results.append(
                memory
            )

    return results


def search_by_content(
    keyword,
):

    keyword = (
        keyword.lower()
        .strip()
    )

    results = []

    memories = get_all()

    for memory in memories:

        content = (
            memory.get(
                "content",
                ""
            )
            .lower()
        )

        if keyword in content:

            results.append(
                memory
            )

    return results


def search_by_project(
    project,
):

    results = []

    memories = get_all()

    for memory in memories:

        if (
            memory.get(
                "project"
            )
            ==
            project
        ):

            results.append(
                memory
            )

    return results


def search_by_source(
    source,
):

    results = []

    memories = get_all()

    for memory in memories:

        if (
            memory.get(
                "source"
            )
            ==
            source
        ):

            results.append(
                memory
            )

    return results


def search_by_memory_type(
    memory_type,
):

    results = []

    memories = get_all()

    for memory in memories:

        if (
            memory.get(
                "memory_type"
            )
            ==
            memory_type
        ):

            results.append(
                memory
            )

    return results

def retrieve_memories(
    query,
    top_k=10,
):

    return retrieve(
        query
    )