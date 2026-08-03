from datetime import datetime

from core.memory_ai import MemoryAI
from data_model.memory_factory import MemoryFactory

ai = MemoryAI()

experience = MemoryFactory.create_experience(
    title="Test Memory Pipeline",
    topic="MemoryAI",
    status="SUCCESS",
    reason="Pipeline OK",
    lessons=[
        "MemoryAI có thể lưu Experience."
    ],
    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    source="MemoryAI",
    version="V1",
    next_action="Tiếp tục tích hợp AutoYouTube."
)

ai.save_experience(experience)

print("Done!")