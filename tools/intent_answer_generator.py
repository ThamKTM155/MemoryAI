def generate_explanation(result):

    facts = result["facts"]

    return (
        f'{facts["id"]} belongs to project '
        f'{facts["project"]}.'
    )


def generate_importance(result):

    knowledge = result["knowledge"]

    if knowledge.get("impact_level") == "high":

        return (
            "Yes.\n\n"
            "It is considered a core document "
            "with a high impact level."
        )

    return "No."


def generate_project(result):

    facts = result["facts"]

    return facts["project"]


def generate_action(result):

    action = result["action"]

    return action["next_step"]