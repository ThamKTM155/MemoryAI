from pathlib import Path


class DiaryLoader:
    def __init__(self, diary_path):
        self.diary_path = Path(diary_path)

    def load_all(self):
        documents = []

        if not self.diary_path.exists():
            print(f"[ERROR] Folder not found: {self.diary_path}")
            return documents

        for file in sorted(self.diary_path.glob("*.md")):

            try:
                content = file.read_text(
                    encoding="utf-8"
                )

                documents.append({
                    "filename": file.name,
                    "path": str(file),
                    "content": content
                })

            except Exception as e:

                print(f"[ERROR] {file.name}: {e}")

        return documents

    def save_markdown(self, filename, content):

        file_path = self.diary_path / filename

        file_path.write_text(
            content,
            encoding="utf-8"
        )