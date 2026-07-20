from core.reasoning.base_reasoner import BaseReasoner


class BuildReasoner(BaseReasoner):

    def get_latest_build(self):

        state = self.get_project_state()

        return state["latest_build"]

    def answer(self):

        latest_build = self.get_latest_build()

        return (
            f"BUILD gần nhất là {latest_build}. "
            "Hệ thống đã ghi nhận BUILD này và sẵn sàng tiếp tục phát triển."
        )