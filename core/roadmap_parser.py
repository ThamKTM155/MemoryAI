import re


class RoadmapParser:

    def parse(self, text):

        roadmap = {}

        current_section = None

        buffer = []

        for line in text.splitlines():

            line = line.rstrip()

            # Tiêu đề dạng:
            # # MISSION

            if re.match(r"^#\s+", line):

                if current_section:

                    roadmap[current_section] = "\n".join(buffer).strip()

                current_section = line.replace("#", "").strip()

                buffer = []

            else:

                buffer.append(line)

        if current_section:

            roadmap[current_section] = "\n".join(buffer).strip()

        return roadmap