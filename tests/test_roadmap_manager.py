from core.roadmap_manager import RoadmapManager

manager = RoadmapManager(
    r"D:\MemoryAI\05_Diary"
)

if manager.load():

    manager.status()

else:

    print("Roadmap not found")