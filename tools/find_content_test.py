from service.memory_repository import (
    MemoryRepository,
)

memories = (
    MemoryRepository.load_all()
)

for memory in memories:

    if (
        "AutoYouTube tạo ra video tốt hơn"
        in memory.get(
            "content",
            ""
        )
    ):

        print()
        print("TITLE:")
        print(
            memory.get(
                "title"
            )
        )

        print()
        print("CONTENT:")
        print(
            memory.get(
                "content"
            )
        )

        break