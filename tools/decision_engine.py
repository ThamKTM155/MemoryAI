def decide(impact):

    decision = {}

    if impact.get("change_warning"):

        decision["review_required"] = True

    return decision