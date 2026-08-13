"""
Reason Engine

BUILD-63B

Generate reasoning from retrieved facts.
"""


def reason(facts):

    reasoning = {}

    # ---------------------------------
    # Không có dữ liệu
    # ---------------------------------

    if facts is None:
        return reasoning

    # ---------------------------------
    # Kiểm tra số lượng liên kết
    # ---------------------------------

    if facts.get("related_count", 0) >= 4:

        reasoning["connected_document"] = True

    # ---------------------------------
    # Kiểm tra tài liệu quan trọng
    # ---------------------------------

    if (
        facts.get("project") == "MemoryGraph"
        and facts.get("type") == "DOCUMENT"
    ):

        reasoning["important_document"] = True

    return reasoning