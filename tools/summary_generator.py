def generate_summary(facts):

    lines = []

    lines.append(
        f'Document : {facts["id"]}'
    )

    lines.append(
        f'Project  : {facts["project"]}'
    )

    lines.append(
        f'Status   : {facts["status"]}'
    )

    lines.append(
        f'Related  : {facts["related_count"]}'
    )

    return "\n".join(lines)