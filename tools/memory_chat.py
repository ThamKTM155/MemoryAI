from tools.question_parser import parse
from tools.question_classifier import classify
from tools.memory_query_service import query
from tools.intent_router import route


def chat(question):

    node_id = parse(question)

    intent = classify(question)

    result = query(node_id)

    return route(intent, result)