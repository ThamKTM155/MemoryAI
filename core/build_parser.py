class BuildParser:

    SECTION_MAP = {

        "# OBJECTIVE": "objective",
        "## Mục tiêu": "objective",

        "# COMPLETED": "completed",
        "## Hoàn thành": "completed",

        "# NEXT BUILD": "next_build",
        "## BUILD tiếp theo": "next_build",

        "## Kiểm thử": "tests",

        "## Kết quả": "result",

        "# NOTES": "notes",
        "## Ghi chú": "notes"
    }

    def parse(self, document):

        content = document["content"]

        result = {

            "filename": document["filename"],

            "objective": [],
            "completed": [],
            "tests": [],
            "result": [],
            "next_build": [],
            "notes": []

        }

        section = None

        for line in content.splitlines():

            line = line.strip()

            if not line:
                continue

            #
            # Đổi section
            #

            if line in self.SECTION_MAP:

                section = self.SECTION_MAP[line]

                continue

            #
            # Chưa ở section nào
            #

            if section is None:

                continue

            #
            # Bỏ dấu "-"
            #

            if line.startswith("-"):

                line = line[1:].strip()

            #
            # Bỏ heading nhỏ
            #

            if line.startswith("#"):

                continue

            #
            # Lưu nội dung
            #

            result[section].append(line)

        return result