"""
BUILD-004.2
Smart Router V1

Nhiệm vụ:
- Nhận câu hỏi.
- Quyết định nên chuyển đến module nào.
"""

class SmartRouter:

    def __init__(self):
        pass

    def route(self, question: str) -> str:

        question = question.lower()

        TIMELINE_KEYWORDS = [
            "build",
            "hoàn thành",
            "kết quả",
            "mục tiêu",
            "kiểm thử"
        ]

        for keyword in TIMELINE_KEYWORDS:
            if keyword in question:
                return "timeline"

        if "knowledge" in question:
            return "knowledge"

        if "adr" in question:
            return "adr"

        if "roadmap" in question:
            return "roadmap"

        return "unknown"