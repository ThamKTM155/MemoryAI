import json
import uuid

from pathlib import Path

from data_model.memory_record import MemoryRecord
from service.memory_service import MemoryService
MemoryService.save_memory(
    memory
)

AI_STATS_FOLDER = Path(
    r"D:\AutoYouTube\autoyoutube_v22\data"
)


def import_ai_stats():

    files = list(
        AI_STATS_FOLDER.glob(
            "ai_stats_*.json"
        )
    )

    print(
        f"FOUND FILES: {len(files)}"
    )

    imported = 0

    for file in files:

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

        except Exception as e:

            print(
                "ERROR:",
                file.name,
                e
            )

            continue

        for item in data:

            title = item.get(
                "title",
                ""
            )

            topic = item.get(
                "topic",
                ""
            )

            views = item.get(
                "views",
                0
            )

            retention = item.get(
                "retention",
                0
            )

            content = (
                f"TOPIC={topic}\n"
                f"VIEWS={views}\n"
                f"RETENTION={retention}"
            )
            
            memory = MemoryRecord(
                id=str(uuid.uuid4()),
                memory_type="note",
                title=title,
                content=content,
                project="AutoYouTube",
                source="WinnerAI"
            )

            MemoryService.save_memory(
                memory
            )

            imported += 1

    print(
        f"IMPORTED: {imported}"
    )