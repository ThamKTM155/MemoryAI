from core.reasoning.base_reasoner import BaseReasoner


class TimelineReasoner(BaseReasoner):

    def get_build_history(self):

        summary = self.memory.summary()

        return summary["builds"]

    def answer(self):

        builds = self.get_build_history()

        return (
            f"Dự án hiện có {len(builds)} BUILD đã được ghi nhận."
        )