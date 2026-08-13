"""
=========================================
IDENTITY GATEWAY

BUILD-58A

Chịu trách nhiệm xử lý
toàn bộ truy vấn Identity.
=========================================
"""

from tools.core_identity import answer_identity


def ask(question):

    return answer_identity(question)