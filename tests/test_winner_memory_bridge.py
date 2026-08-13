from data_model.memory_record import (
    MemoryRecord,
)

from service.memory_service import (
    MemoryService,
)


memory = MemoryRecord(
    id="TEST-70I3",
    memory_type="note",
    title="TEST WINNERAI SERVICE GATE",
    content="BUILD-70I.3 test",
    project="AutoYouTube",
    source="WinnerAI",
)

result = MemoryService.save_memory(
    memory
)

print(
    "SAVED:",
    result.title
)