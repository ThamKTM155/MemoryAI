"""
=========================================

DOCUMENT LEARNING ENGINE

BUILD-67

Document Learning Engine V1

Nhiệm vụ:

- Đọc tài liệu.
- Trả về nội dung.
- Chưa phân tích.
- Chưa ghi Memory.
- Chưa dùng AI.

=========================================
"""

from pathlib import Path


def load_document(file_path):

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(file_path)

    return path.read_text(
        encoding="utf-8"
    )

def split_sections(text):

    sections = []

    current_title = "Document"

    current_content = []

    for line in text.splitlines():

        if line.startswith("#"):

            if current_content:

                sections.append({
                    "title": current_title,
                    "content": "\n".join(current_content).strip()
                })

            current_title = line.lstrip("#").strip()

            current_content = []

        else:

            current_content.append(line)

    if current_content:

        sections.append({
            "title": current_title,
            "content": "\n".join(current_content).strip()
        })

    return sections

def build_memory_records(sections):

    memories = []

    for section in sections:

        memory = {
            "title": section["title"],
            "content": section["content"],
            "learned": False
        }

        memories.append(memory)

    return memories

def learn_document(file_path):

    from service.memory_center import remember

    text = load_document(file_path)

    sections = split_sections(text)

    memories = build_memory_records(sections)

    learned_count = 0

    for memory in memories:

        if not memory["content"].strip():
            continue

        remember(
            memory["title"],
            memory["content"]
        )

        learned_count += 1

    return learned_count