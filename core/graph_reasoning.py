"""
Memory Reasoning
BUILD-32.0
"""


def explain_path(path):
    """
    Chuyển Path thành lời giải thích.
    """

    if not path:
        return "Không tìm thấy mối liên hệ."

    lines = []

    for step in path:

        relation = step["type"]

        if relation == "HAS_KEYWORD":

            text = (
                f'"{step["to"]}" '
                f'là keyword của "{step["from"]}".'
            )

        elif relation == "REVERSE_HAS_KEYWORD":

            text = (
                f'"{step["from"]}" '
                f'là keyword của "{step["to"]}".'
            )

        elif relation == "HAS_DECISION":

            text = (
                f'"{step["to"]}" '
                f'là decision của "{step["from"]}".'
            )

        elif relation == "REVERSE_HAS_DECISION":

            text = (
                f'"{step["from"]}" '
                f'là decision của "{step["to"]}".'
            )

        elif relation == "HAS_LESSON":

            text = (
                f'"{step["to"]}" '
                f'là lesson của "{step["from"]}".'
            )

        elif relation == "REVERSE_HAS_LESSON":

            text = (
                f'"{step["from"]}" '
                f'là lesson của "{step["to"]}".'
            )

        else:

            text = (
                f'{step["from"]} '
                f'--[{relation}]--> '
                f'{step["to"]}'
            )

        lines.append(text)

    return "\n".join(lines)

def summarize_path(path):
    """
    Tóm tắt ý nghĩa của đường đi.
    """

    if not path:
        return "Không tìm thấy mối liên hệ."

    if len(path) == 2:

        first = path[0]
        second = path[1]

        if (
            first["type"] == "REVERSE_HAS_KEYWORD"
            and
            second["type"] == "HAS_KEYWORD"
        ):

            diary = first["to"]

            return (
                f'{first["from"]} và '
                f'{second["to"]} '
                f'có liên hệ vì cả hai đều là '
                f'keyword của {diary}.'
            )

    return "Đã tìm thấy đường đi giữa hai node."