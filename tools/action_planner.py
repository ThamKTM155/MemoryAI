def plan(decision):

    action = {}

    if decision.get("review_required"):

        action["next_step"] = (
            "Review related documents before modification."
        )

    return action