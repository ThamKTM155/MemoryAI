"""
=========================================
QUESTION CLASSIFIER

BUILD-61A

Classify user intent.

Không xử lý nghiệp vụ.

Chỉ xác định ý định của người chủ.
=========================================
"""


def classify(question):

    if question is None:
        return "lookup"

    text = str(question).lower().strip()

    # ----------------------------------
    # Identity
    # ----------------------------------

    if (
        "bạn là ai" in text
        or "bạn tên gì" in text
        or "tên là gì" in text
        or "ai tạo" in text
    ):
        return "identity"

    # ----------------------------------
    # Continue Work
    # ----------------------------------

    if (
        "tiếp tục" in text
        or "làm tiếp" in text
        or "tiếp theo" in text
    ):
        return "continue_work"

    # ----------------------------------
    # Planning
    # ----------------------------------

    if (
        "hôm nay" in text
        or "kế hoạch" in text
        or "nên làm gì" in text
    ):
        return "plan_work"

    # ----------------------------------
    # Save Memory
    # ----------------------------------

    if (
        "ghi nhớ" in text
        or "hãy nhớ" in text
        or "lưu lại" in text
    ):
        return "save_memory"
    # ----------------------------------
    # Legacy Support
    # ----------------------------------

    if "what is" in text:
        return "explain"

    if "important" in text:
        return "importance"

    if "project" in text:
        return "project"

    if "before" in text:
        return "action"

    return "lookup"
    # ----------------------------------
    # Search Memory
    # ----------------------------------

    if (
        "tìm" in text
        or "nhớ" in text
        or "graph_rules" in text.lower()
    ):
        return "search_memory"

    # ----------------------------------
    # System Status
    # ----------------------------------

    if (
        "trạng thái" in text
        or "health" in text
        or "hệ thống" in text
    ):
        return "system_status"