"""
=========================================
KNOWLEDGE GATE

BUILD-58B

Unified Gateway Dispatcher

Mọi truy vấn của hệ sinh thái
đều đi qua cổng này.
=========================================
"""
from tools.gateways.identity_gateway import ask as ask_identity

from tools.gateways.repository_gateway import ask as ask_repository

from tools.gateways.graph_gateway import ask as ask_graph

from tools.gateways.ai_gateway import ask as ask_ai

def ask(question):

    # -------------------------
    # Identity Gateway
    # -------------------------

    reply = ask_identity(question)

    if reply is not None:

        return reply

    # -------------------------
    # Repository Gateway
    # -------------------------

    reply = ask_repository(question)

    if (
        reply
        and reply != "❌ Không tìm thấy"
    ):

        return reply

    # -------------------------
    # Graph Gateway
    # -------------------------

    reply = ask_graph(question)

    if reply is not None:

        return reply

    return ask_ai(question)