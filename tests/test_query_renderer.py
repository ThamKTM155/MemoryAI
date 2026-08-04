from pprint import pprint

from tools.query_renderer import (
    render,
)


result = render("GRAPH_RULES")

print("=" * 60)
print("QUERY RENDERER TEST")
print("=" * 60)

print()

print("RESULT")

pprint(result)

print()

print("SUMMARY")

print(result["summary"])

print()

print("INSIGHT")

print(result["insight"])