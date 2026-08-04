def generate_insight(reasoning):

    lines = []

    if reasoning.get("connected_document"):

        lines.append(
            "This is a connected document."
        )

    if reasoning.get("important_document"):

        lines.append(
            "This document is considered important."
        )

    return "\n\n".join(lines)