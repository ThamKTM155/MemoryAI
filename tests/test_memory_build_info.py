from core.memory_api import Memory

memory = Memory("05_Diary")

memory.load()

info = memory.get_latest_build_info()

print(info)