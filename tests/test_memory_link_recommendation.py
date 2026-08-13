from service.memory_link_recommendation import (
    get_best_recommendation,
    get_top_recommendations,
)


print()

print(
    "MEMORY LINK RECOMMENDATION TEST"
)

print(
    "=" * 50
)

title = "SYSTEM CONSTITUTION"

best = get_best_recommendation(
    title
)

print(
    "BEST:",
    best
)

top = get_top_recommendations(
    title,
    limit=5,
)

print(
    "TOP:",
    top
)

print()