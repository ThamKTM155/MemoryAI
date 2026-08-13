from tools.answer_generator import generate

from tools.intent_answer_generator import (
    generate_action,
    generate_explanation,
    generate_importance,
    generate_project,
)


def route(intent, result):

    if intent == "explain":
        return generate_explanation(result)

    if intent == "importance":
        return generate_importance(result)

    if intent == "project":
        return generate_project(result)

    if intent == "action":
        return generate_action(result)

    return generate(result)