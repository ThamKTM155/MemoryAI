"""
Knowledge Extractor
===================

Phân tích nhiều Experience để tìm
ra các quy luật (Pattern).

Không lưu dữ liệu.
Không tạo Knowledge.
Chỉ trích xuất Pattern.
"""


class KnowledgeExtractor:

    def extract(self, experiences):

        patterns = []

        if not experiences:
            return patterns

        for exp in experiences:

            pattern = {

                "topic": getattr(exp, "topic", ""),

                "hook": getattr(exp, "hook", ""),

                "status": getattr(exp, "status", ""),

                "reason": getattr(exp, "reason", "")

            }

            patterns.append(pattern)

        return patterns