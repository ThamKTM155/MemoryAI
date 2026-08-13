def generate(result):

    lines = []

    facts = result["facts"]
    knowledge = result["knowledge"]
    impact = result["impact"]
    action = result["action"]

    lines.append(
        f'{facts["id"]} belongs to project {facts["project"]}.'
    )

    if knowledge.get("document_role"):

        lines.append(
            "This is a core document."
        )

    if knowledge.get("impact_level") == "high":

        lines.append(
            "Its impact level is high."
        )

    if impact.get("change_warning"):

        lines.append(
            "Changes should be reviewed before modification."
        )

    if action.get("next_step"):

        lines.append(
            action["next_step"]
        )

    return "\n\n".join(lines)