"""
Memory Logger
========================

Bridge giữa AutoYouTube và MemoryAI.

Pipeline chỉ cần gọi:

    log_experience(...)

Mọi logic lưu Experience đều nằm trong file này.
"""

from core.memory_ai import MemoryAI
from data_model.memory_factory import MemoryFactory


memory = MemoryAI()


def log_experience(
    channel="",
    topic="",
    title="",
    hook="",
    video="",
    youtube_id="",
    status="SUCCESS",
    reason="Upload thành công",
    lessons=None,
    next_action=""
):

    experience = MemoryFactory.create_experience(

        channel=channel,

        topic=topic,

        title=title,

        hook=hook,

        status=status,

        reason=reason,

        lessons=lessons or [],

        next_action=next_action

    )

    memory.save_experience(experience)

    print("💾 MEMORY SAVED")