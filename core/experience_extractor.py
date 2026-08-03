"""
Experience Extractor
====================

Chuyển dữ liệu từ AutoYouTube (Event)
thành Experience chuẩn của MemoryAI.
"""

from data_model.memory_factory import MemoryFactory


class ExperienceExtractor:

    def extract(self, event: dict):

        return MemoryFactory.create_experience(

            channel=event.get("channel", ""),

            topic=event.get("topic", ""),

            title=event.get("title", ""),

            hook=event.get("hook", ""),

            status=event.get("status", ""),

            reason=event.get("reason", ""),

            lessons=event.get("lessons", []),

            next_action=event.get("next_action", "")

        )