from core.memory_api import Memory

memory = Memory("05_Diary")

memory.load()

state = memory.get_project_state()

print("=" * 60)
print("PROJECT STATE")
print("=" * 60)

print()

for key, value in state.items():

    print(f"{key} : {value}")