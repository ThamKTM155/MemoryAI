"""
=========================================
MEMORY CENTER

BUILD-65A

Memory Center

Phụ trách:

- Ghi nhớ
- Truy xuất trí nhớ
- Cập nhật trí nhớ
- Xóa trí nhớ

Không phụ trách:

- Knowledge
- Planner
- AI

=========================================
"""

from service.memory_service import MemoryService


class MemoryCenter:

    def save_memory(
        self,
        memory_type,
        title,
        content,
        project,
        source=""
    ):

        return MemoryService.create_memory(
            memory_type=memory_type,
            title=title,
            content=content,
            project=project,
            source=source,
        )
    def remember(
        self,
        title,
        content,
    ):

        return self.save_memory(
            memory_type="note",
            title=title,
            content=content,
            project="MemoryAI",
            source="ChiefOperationsOfficer",
        )

_memory = MemoryCenter()


def save_memory(
    memory_type,
    title,
    content,
    project,
    source=""
):

    return _memory.save_memory(
        memory_type,
        title,
        content,
        project,
        source,
    )

def remember(
    title,
    content,
):

    return _memory.remember(
        title,
        content,
    )