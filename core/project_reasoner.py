from core.reasoning.build_reasoner import BuildReasoner
from core.reasoning.roadmap_reasoner import RoadmapReasoner
from core.reasoning.adr_reasoner import ADRReasoner

class ProjectReasoner:

    def __init__(self, memory):

        self.memory = memory

        self.build_reasoner = BuildReasoner(memory)

        self.roadmap_reasoner = RoadmapReasoner(memory)

        self.adr_reasoner = ADRReasoner(memory)

    def get_project_state(self):

        return self.memory.get_project_state()

    def answer_project(self):

        state = self.memory.get_project_state()

        return (
            f"Dự án hiện có {state['documents']} tài liệu, "
            f"{state['daily_logs']} nhật ký phát triển. "
            f"BUILD gần nhất là {state['latest_build']}. "
            f"Roadmap hiện hành là {state['current_roadmap']}. "
            f"Trạng thái hệ thống: {state['status']}."
        )

    def answer(self, question):

        question = question.lower()

        if "roadmap" in question:

            return self.roadmap_reasoner.answer()

        if "adr" in question:

            return self.adr_reasoner.answer()

        if "build" in question:

            return self.build_reasoner.answer()

        if "ở đâu" in question or "giai đoạn" in question:

            return self.answer_project()

        return "Tôi chưa hiểu câu hỏi."