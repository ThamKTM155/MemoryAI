from core.reasoning.base_reasoner import BaseReasoner

QUESTION_ALIASES = {
    # Result
    "đã xong chưa": "kết quả là gì",
    "đã hoàn thành chưa": "kết quả là gì",
    "kết quả": "kết quả là gì",

    # Latest build
    "build gần nhất": "build mới nhất",
    "build mới": "build mới nhất",

    # Completed
    "đã làm được gì": "đã hoàn thành gì",

    # Objective
    "đang xây gì": "mục tiêu là gì",

    # Next build
    "tiếp theo làm gì": "build tiếp theo",
}
class TimelineReasoner(BaseReasoner):

    def get_build_history(self):

        return self.memory.get_build_history()

    def answer(self, question=None):
        if question is not None:
            
            question = question.lower().strip()
            question = QUESTION_ALIASES.get(question, question)
        count = self.memory.get_build_count()

        first_build = self.memory.get_first_build()

        latest_build = self.memory.get_latest_build_info()

        lines = []

        lines.append(
            f"Dự án hiện có {count} BUILD đã được ghi nhận."
        )

        if first_build:

            lines.append("")
            lines.append(
                f"BUILD đầu tiên: {first_build['filename']}"
            )

        if question == "build mới nhất":

            if latest_build is None:
                return "Chưa có BUILD."

            return latest_build["filename"]

        if question == "build tiếp theo":

            if latest_build is None:
                return "Chưa có BUILD."

            if latest_build["next_build"]:
                return latest_build["next_build"][0]

            return "BUILD tiếp theo chưa được ghi."
        if question == "đã hoàn thành gì":

            if latest_build is None:
                return "Chưa có BUILD."

            return "\n".join(latest_build["completed"])

        if question == "mục tiêu là gì":

            if latest_build is None:
                return "Chưa có BUILD."

            return "\n".join(latest_build["objective"])

        if question == "đã kiểm thử gì":

            if latest_build is None:
                return "Chưa có BUILD."

            return "\n".join(latest_build["tests"])

        if question == "kết quả là gì":

            if latest_build is None:
                return "Chưa có BUILD."

            return "\n".join(latest_build["result"])

            if latest_build["next_build"]:

                return latest_build["next_build"][0]

            return "BUILD tiếp theo chưa được ghi."

        if latest_build:

            lines.append("")
            lines.append(
                f"BUILD mới nhất: {latest_build['filename']}"
            )

            if latest_build["objective"]:

                lines.append("")
                lines.append("Mục tiêu:")

                for item in latest_build["objective"]:

                    lines.append(f"- {item}")
            if latest_build["completed"]:

                lines.append("")
                lines.append("Đã hoàn thành:")

                for item in latest_build["completed"]:

                    lines.append(f"- {item}")

            if latest_build["tests"]:

                lines.append("")
                lines.append("Kiểm thử:")

                for item in latest_build["tests"]:

                    lines.append(f"- {item}")


            if latest_build["result"]:

                lines.append("")
                lines.append("Kết quả:")

                for item in latest_build["result"]:

                    lines.append(f"- {item}")

            if latest_build["next_build"]:

                lines.append("")
                lines.append("BUILD tiếp theo:")

                for item in latest_build["next_build"]:

                    lines.append(f"- {item}")
        return "\n".join(lines)