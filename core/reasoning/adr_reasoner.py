from core.reasoning.base_reasoner import BaseReasoner


class ADRReasoner(BaseReasoner):

    def get_latest_adr(self):

        state = self.get_project_state()

        return state["latest_adr"]

    def answer(self):

        adr = self.get_latest_adr()

        return (
            f"ADR mới nhất là {adr}. "
            "Đây là quyết định kiến trúc mới nhất của dự án."
        )