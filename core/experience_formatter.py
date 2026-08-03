class ExperienceFormatter:

    def format(self, experience):

        lines = []

        lines.append("# Experience")
        lines.append("")

        lines.append("## Metadata")
        lines.append(f"Experience ID: {getattr(experience, 'id', '')}")
        lines.append(f"Date: {getattr(experience, 'date', '')}")
        lines.append(f"Source: {getattr(experience, 'source', '')}")
        
        lines.append(f"Version: {getattr(experience, 'version', 'V1')}")
        lines.append("")

        lines.append("## Input")
        lines.append(f"Channel: {getattr(experience, 'channel', '')}")
        lines.append(f"Topic: {getattr(experience, 'topic', '')}")
        lines.append(f"Title: {getattr(experience, 'title', '')}")
        lines.append(f"Hook: {getattr(experience, 'hook', '')}")
        lines.append("")

        lines.append("## Output")
        lines.append(f"Views: {getattr(experience, 'views', 0)}")
        lines.append(f"CTR: {getattr(experience, 'ctr', 0.0)}")
        lines.append(f"Retention: {getattr(experience, 'retention', 0.0)}")
        lines.append("")

        lines.append("## Analysis")
        lines.append(f"Status: {getattr(experience, 'status', '')}")
        lines.append(f"Reason: {getattr(experience, 'reason', '')}")
        lines.append("")

        lines.append("## Lessons")

        lessons = getattr(experience, "lessons", [])

        if lessons:
            for lesson in lessons:
                lines.append(f"- {lesson}")
        else:
            lines.append("-")

        lines.append("")
        lines.append("## Next Action")
        lines.append(getattr(experience, "next_action", ""))

        return "\n".join(lines)