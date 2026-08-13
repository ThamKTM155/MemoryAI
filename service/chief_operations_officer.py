"""
=========================================
CHIEF OPERATIONS OFFICER

BUILD-63A

Chief Operations Officer (COO)

Trưởng phòng tác chiến kiêm Trợ lý tổng hợp.

Vai trò:

- Tiếp nhận yêu cầu từ Operations Center.
- Phân tích ý định.
- Quyết định giao nhiệm vụ.
- Tổng hợp kết quả.
- Báo cáo lại Operations Center.

Không trực tiếp:

- Truy cập Repository
- Truy cập Graph
- Gọi AI
- Thực hiện nghiệp vụ chuyên môn

=========================================
"""

from tools.knowledge_gate import ask
from tools.question_classifier import classify
from service.memory_center import remember
from service.planner_center import (
    continue_work,
    today_plan,
)

class ChiefOperationsOfficer:
    """
    Trưởng phòng tác chiến.

    BUILD-63A

    Hiện tại:

    - Phân loại Intent.
    - Điều phối tạm thời tới Knowledge Gate.

    BUILD tiếp theo sẽ bổ sung:

    - Planner Center
    - Memory Center
    - AI Center
    - Action Center
    """

    def handle(self, message):

        if message is None:
            return ""

        message = str(message).strip()

        if not message:
            return "Anh chưa nhập nội dung."

        intent = classify(message)

        # -------------------------------------------------
        # Identity Center
        # -------------------------------------------------

        if intent == "identity":
            return ask(message)

        # -------------------------------------------------
        # Knowledge Center
        # -------------------------------------------------

        if intent == "search_memory":
            return ask(message)

        # -------------------------------------------------
        # Planner Center
        # -------------------------------------------------

        if intent == "continue_work":

            return continue_work()

        if intent == "plan_work":

            return today_plan()
        # -------------------------------------------------
        # Memory Center (Reserved)
        # -------------------------------------------------

        if intent == "save_memory":

            return remember(
                title="Memory Note",
                content=message,
            )
        # -------------------------------------------------
        # Default
        # -------------------------------------------------

        return ask(message)