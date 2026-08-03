from core.diary_loader import DiaryLoader

loader = DiaryLoader("05_Diary")

loader.save_markdown(

    "TEST_MEMORY.md",

    "# Test\n\nMemoryAI Write OK"

)

print("Done!")