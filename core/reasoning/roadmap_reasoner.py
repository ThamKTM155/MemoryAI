from core.reasoning.base_reasoner import BaseReasoner


class RoadmapReasoner(BaseReasoner):

    def get_current_roadmap(self):

        state = self.get_project_state()

        return state["current_roadmap"]

    def answer(self):

        roadmap = self.get_current_roadmap()

        return (
            f"Roadmap hiện hành là {roadmap}. "
            "Đây là định hướng phát triển chính của dự án."
        )