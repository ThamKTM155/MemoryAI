from service.memory_service import (
    MemoryService,
)


def retrieve(
    keyword,
):

    return (
        MemoryService.search_memory(
            keyword
        )
    )