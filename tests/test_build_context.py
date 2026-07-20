from core.memory_api import Memory


memory = Memory("05_Diary")

memory.load()

context = memory.build_context()

print("=" * 60)
print("BUILD CONTEXT")
print("=" * 60)

print()

for key, value in context.items():

    print(key)

    if isinstance(value, dict):

        if "filename" in value:

            print(" ", value["filename"])

        else:

            print(" ", value)

    else:

        print(" ", value)

    print()