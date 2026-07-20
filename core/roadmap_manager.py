from core.diary_loader import DiaryLoader
from core.roadmap_parser import RoadmapParser


class RoadmapManager:

    def __init__(self, diary_path):

        self.loader = DiaryLoader(diary_path)

        self.parser = RoadmapParser()

        self.roadmap = None

    def load(self):

        docs = self.loader.load_all()

        for doc in docs:

            if "ROADMAP" in doc["filename"].upper():

                self.roadmap = self.parser.parse(
                    doc["content"]
                )

                return True

        return False

    def status(self):

        if self.roadmap is None:

            print("Roadmap not loaded")

            return

        print("=" * 60)

        print("MemoryAI Roadmap Loaded")

        print("=" * 60)

        print()

        for section in self.roadmap:

            print(f"✓ {section}")