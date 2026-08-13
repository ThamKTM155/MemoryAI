from service.memory_service import (
    MemoryService,
)

from service.memory_keyword_repository import (
    MemoryKeywordRepository,
)


def build_keywords():

    memories = MemoryService.get_all_memories()

    keyword_map = {}

    for memory in memories:

        title = memory.get(
            "title",
            ""
        )

        content = memory.get(
            "content",
            ""
        )

        words = set()

        for word in title.split():

            if len(word) >= 3:

                words.add(
                    word.lower()
                )

        for word in content.split():

            word = (
                word
                .replace(".", "")
                .replace(",", "")
                .replace(":", "")
                .replace(";", "")
                .replace("-", "")
                .lower()
            )

            if len(word) >= 4:

                words.add(word)

        keyword_map[title] = sorted(
            list(words)
        )

    MemoryKeywordRepository.save(
        keyword_map
    )

    return keyword_map

def find_titles_by_keyword(
    keyword,
):

    data = MemoryKeywordRepository.load()

    keyword = keyword.lower().strip()

    results = []

    for title, words in data.items():

        title_lower = (
            title.lower()
        )

        if keyword in words:

            results.append(
                title
            )

            continue

        if keyword in title_lower:

            results.append(
                title
            )

    return results

def has_keyword(
    keyword,
):

    data = MemoryKeywordRepository.load()

    keyword = keyword.lower()

    for words in data.values():

        if keyword in words:

            return True

    return False