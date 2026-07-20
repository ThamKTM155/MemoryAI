from core.diary_loader import DiaryLoader
from core.roadmap_parser import RoadmapParser

loader = DiaryLoader(r"D:\MemoryAI\05_Diary")
docs = loader.load_all()

parser = RoadmapParser()

for doc in docs:

    if "ROADMAP" in doc["filename"].upper():

        roadmap = parser.parse(doc["content"])

        print("=" * 60)

        print("Roadmap Sections")

        print("=" * 60)

        for key in roadmap:

            print(key)