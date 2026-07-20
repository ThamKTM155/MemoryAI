from core.memory_api import Memory
from core.build_parser import BuildParser

memory = Memory("05_Diary")

memory.load()

build = memory.get_latest_build()

parser = BuildParser()

result = parser.parse(build)

print(result)