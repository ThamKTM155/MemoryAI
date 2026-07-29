"""
Knowledge Repository
BUILD-35.2

Nhiệm vụ:
- Lưu Knowledge Record.
- Đọc Knowledge Record.
- Không xử lý Business Logic.
- Không Validation.
- Không Build Relationships.
"""

import json
from pathlib import Path


def save_knowledge(knowledge, output_file):
    """
    Lưu Knowledge Record ra file JSON.

    Parameters
    ----------
    knowledge : dict

    output_file : str | Path

    Returns
    -------
    Path
        Đường dẫn file đã lưu.
    """

    output_file = Path(output_file)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:

        json.dump(
            knowledge,
            f,
            ensure_ascii=False,
            indent=4
        )

    return output_file


def load_knowledge(input_file):
    """
    Đọc Knowledge Record từ file JSON.

    Parameters
    ----------
    input_file : str | Path

    Returns
    -------
    dict
    """

    input_file = Path(input_file)

    with open(input_file, "r", encoding="utf-8") as f:

        knowledge = json.load(f)

    return knowledge
def load_all_knowledge(directory):
    """
    Đọc toàn bộ Knowledge Record trong một thư mục.

    Parameters
    ----------
    directory : str | Path

    Returns
    -------
    list[dict]
        Danh sách Knowledge Record.
    """

    directory = Path(directory)

    knowledge_records = []

    for json_file in sorted(directory.glob("*.json")):

        knowledge = load_knowledge(json_file)

        knowledge_records.append(knowledge)

    return knowledge_records