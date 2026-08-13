from service.memory_service import (
    MemoryService,
)


def get_winner_memories():

    memories = (
        MemoryService.get_all_memories()
    )

    results = []

    for memory in memories:

        if (
            memory.get(
                "source"
            )
            ==
            "WinnerAI"
        ):

            results.append(
                memory
            )

    return results


def print_winner_count():

    data = (
        get_winner_memories()
    )

    print()

    print(
        "# WINNER MEMORIES"
    )

    print()

    print(
        "TOTAL:",
        len(data)
    )

    print()


def get_top_view_memories(
    limit=10,
):

    memories = (
        get_winner_memories()
    )

    best_titles = {}

    for memory in memories:

        content = memory.get(
            "content",
            ""
        )

        views = 0

        for line in (
            content.split("\n")
        ):

            if line.startswith(
                "VIEWS="
            ):

                try:

                    views = int(
                        line.replace(
                            "VIEWS=",
                            ""
                        )
                    )

                except:
                    views = 0

        title = memory["title"]

        old_views = (
            best_titles.get(
                title,
                -1
            )
        )

        if views > old_views:

            best_titles[
                title
            ] = views

    result = []

    for title, views in (
        best_titles.items()
    ):

        result.append(
            (
                views,
                title
            )
        )

    result.sort(
        reverse=True
    )

    return result[:limit]

def print_top_views():

    data = (
        get_top_view_memories()
    )

    print()

    print(
        "# TOP VIEWS"
    )

    print()

    for views, title in data:

        print(
            views,
            "-",
            title
        )

    print()


def search_winner_by_topic(
    topic,
    limit=10,
):

    memories = (
        get_winner_memories()
    )

    results = []

    topic = (
        topic.lower()
    )

    for memory in memories:

        content = memory.get(
            "content",
            ""
        )

        if topic not in (
            content.lower()
        ):
            continue

        views = 0

        for line in (
            content.split("\n")
        ):

            if line.startswith(
                "VIEWS="
            ):

                try:

                    views = int(
                        line.replace(
                            "VIEWS=",
                            ""
                        )
                    )

                except:
                    views = 0

        results.append(
            (
                views,
                memory["title"]
            )
        )

    results.sort(
        reverse=True
    )

    return results[:limit]


def print_topic_winners(
    topic,
):

    data = (
        search_winner_by_topic(
            topic
        )
    )

    print()

    print(
        "# TOPIC:",
        topic
    )

    print()

    for views, title in data:

        print(
            views,
            "-",
            title
        )

    print()

def get_top_retention_memories(
    limit=10,
):

    memories = (
        get_winner_memories()
    )

    best_titles = {}

    for memory in memories:

        content = memory.get(
            "content",
            ""
        )

        retention = 0.0

        for line in (
            content.split("\n")
        ):

            if line.startswith(
                "RETENTION="
            ):

                try:

                    retention = float(
                        line.replace(
                            "RETENTION=",
                            ""
                        )
                    )

                except:

                    retention = 0.0

        title = memory["title"]

        old_retention = (
            best_titles.get(
                title,
                -1
            )
        )

        if retention > old_retention:

            best_titles[
                title
            ] = retention

    result = []

    for title, retention in (
        best_titles.items()
    ):

        result.append(
            (
                retention,
                title
            )
        )

    result.sort(
        reverse=True
    )

    return result[:limit]

def print_top_retention():

    data = (
        get_top_retention_memories()
    )

    print()

    print(
        "# TOP RETENTION"
    )

    print()

    for retention, title in data:

        print(
            retention,
            "-",
            title
        )

    print()

def get_top_winner_scores(
    limit=10,
):

    memories = (
        get_winner_memories()
    )

    best_titles = {}

    for memory in memories:

        content = memory.get(
            "content",
            ""
        )

        views = 0
        retention = 0.0

        for line in (
            content.split("\n")
        ):

            if line.startswith(
                "VIEWS="
            ):

                try:
                    views = int(
                        line.replace(
                            "VIEWS=",
                            ""
                        )
                    )
                except:
                    views = 0

            if line.startswith(
                "RETENTION="
            ):

                try:
                    retention = float(
                        line.replace(
                            "RETENTION=",
                            ""
                        )
                    )
                except:
                    retention = 0.0

        score = round(
            views * retention,
            2
        )

        title = memory["title"]

        old_score = (
            best_titles.get(
                title,
                -1
            )
        )

        if score > old_score:

            best_titles[
                title
            ] = score

    result = []

    for title, score in (
        best_titles.items()
    ):

        result.append(
            (
                score,
                title
            )
        )

    result.sort(
        reverse=True
    )

    return result[:limit]

def print_top_winner_scores():

    data = (
        get_top_winner_scores()
    )

    print()

    print(
        "# TOP WINNER SCORES"
    )

    print()

    for score, title in data:

        print(
            score,
            "-",
            title
        )

    print()

def get_topic_statistics():

    memories = (
        get_winner_memories()
    )

    stats = {}

    for memory in memories:

        content = memory.get(
            "content",
            ""
        )

        topic = "UNKNOWN"

        for line in (
            content.split("\n")
        ):

            if line.startswith(
                "TOPIC="
            ):

                topic = (
                    line.replace(
                        "TOPIC=",
                        ""
                    )
                    .strip()
                )

        stats[topic] = (
            stats.get(
                topic,
                0
            )
            + 1
        )

    return stats

def print_topic_statistics():

    data = (
        get_topic_statistics()
    )

    print()

    print(
        "# TOPIC STATS"
    )

    print()

    for topic, count in sorted(
        data.items(),
        key=lambda x: x[1],
        reverse=True
    ):

        print(
            topic,
            ":",
            count
        )

    print()

def get_winner_patterns():

    memories = (
        get_winner_memories()
    )

    stats = {}

    for memory in memories:

        title = (
            memory.get(
                "title",
                ""
            )
            .strip()
            .lower()
        )

        if not title:
            continue

        words = (
            title.split()
        )

        if len(words) >= 2:

            pattern = (
                words[0]
                + " "
                + words[1]
            )

        else:

            pattern = title

        stats[pattern] = (
            stats.get(
                pattern,
                0
            )
            + 1
        )

    return stats

def print_winner_patterns():

    data = (
        get_winner_patterns()
    )

    print()

    print(
        "# WINNER PATTERNS"
    )

    print()

    for pattern, count in sorted(
        data.items(),
        key=lambda x: x[1],
        reverse=True
    )[:20]:

        print(
            pattern,
            ":",
            count
        )

    print()

def recommend_titles(
    topic,
    limit=5,
):

    memories = (
        get_winner_memories()
    )

    best_titles = {}

    for memory in memories:

        content = memory.get(
            "content",
            ""
        )

        if (
            topic.lower()
            not in
            content.lower()
        ):
            continue

        views = 0
        retention = 0.0

        for line in (
            content.split("\n")
        ):

            if line.startswith(
                "VIEWS="
            ):

                try:
                    views = int(
                        line.replace(
                            "VIEWS=",
                            ""
                        )
                    )
                except:
                    views = 0

            if line.startswith(
                "RETENTION="
            ):

                try:
                    retention = float(
                        line.replace(
                            "RETENTION=",
                            ""
                        )
                    )
                except:
                    retention = 0.0

        score = (
            views
            * retention
        )

        title = (
            memory["title"]
        )

        old_score = (
            best_titles.get(
                title,
                -1
            )
        )

        if score > old_score:

            best_titles[
                title
            ] = score

    result = []

    for title, score in (
        best_titles.items()
    ):

        result.append(
            (
                score,
                title
            )
        )

    result.sort(
        reverse=True
    )

    return result[:limit]

def print_recommend_titles(
    topic,
):

    data = (
        recommend_titles(
            topic
        )
    )

    print()

    print(
        f"# RECOMMEND: {topic}"
    )

    print()

    for score, title in data:

        print(
            round(score, 2),
            "-",
            title
        )

    print()

def recommend_by_pattern(
    pattern,
    limit=10,
):

    memories = (
        get_winner_memories()
    )

    best_titles = {}

    pattern = (
        pattern.strip()
        .lower()
    )

    for memory in memories:

        title = (
            memory.get(
                "title",
                ""
            )
            .strip()
        )

        if not (
            title.lower()
            .startswith(pattern)
        ):
            continue

        content = memory.get(
            "content",
            ""
        )

        views = 0
        retention = 0.0

        for line in (
            content.split("\n")
        ):

            if line.startswith(
                "VIEWS="
            ):

                try:
                    views = int(
                        line.replace(
                            "VIEWS=",
                            ""
                        )
                    )

                except:

                    views = 0

            if line.startswith(
                "RETENTION="
            ):

                try:

                    retention = float(
                        line.replace(
                            "RETENTION=",
                            ""
                        )
                    )

                except:

                    retention = 0.0

        score = (
            views
            * retention
        )

        old_score = (
            best_titles.get(
                title,
                -1
            )
        )

        if score > old_score:

            best_titles[
                title
            ] = score

    result = []

    for title, score in (
        best_titles.items()
    ):

        result.append(
            (
                score,
                title
            )
        )

    result.sort(
        reverse=True
    )

    return result[:limit]

def print_pattern_recommendations(
    pattern,
):

    data = (
        recommend_by_pattern(
            pattern
        )
    )

    print()

    print(
        f"# PATTERN: {pattern}"
    )

    print()

    for score, title in data:

        print(
            round(score, 2),
            "-",
            title
        )

    print()

def get_best_titles(
    topic,
    limit=5,
):

    data = recommend_titles(
        topic,
        limit
    )

    result = []

    for score, title in data:

        result.append(
            title
        )

    return result

def get_best_patterns(
    limit=10,
):

    stats = (
        get_winner_patterns()
    )

    data = sorted(
        stats.items(),
        key=lambda x: x[1],
        reverse=True
    )

    result = []

    for pattern, count in (
        data[:limit]
    ):

        result.append(
            pattern
        )

    return result

def get_best_topics(
    limit=10,
):

    stats = (
        get_topic_statistics()
    )

    data = sorted(
        stats.items(),
        key=lambda x: x[1],
        reverse=True
    )

    result = []

    for topic, count in (
        data[:limit]
    ):

        result.append(
            topic
        )

    return result

