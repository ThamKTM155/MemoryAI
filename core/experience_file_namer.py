from datetime import datetime
from pathlib import Path


class ExperienceFileNamer:

    def next_filename(self, diary_path):

        today = datetime.now().strftime("%Y-%m-%d")

        diary = Path(diary_path)

        pattern = f"EXP-{today}-*.md"

        files = list(diary.glob(pattern))

        number = len(files) + 1

        experience_id = f"EXP-{today}-{number:04d}"

        filename = f"{experience_id}.md"

        return experience_id, filename