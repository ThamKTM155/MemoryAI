"""
Memory Repository
BUILD-36.3

Nhiệm vụ:
- Lưu Memory Database
- Đọc Memory Database
"""

import json
from pathlib import Path


def save_memory_database(memory_db, output_file):
    """
    Save memory database.

    Parameters
    ----------
    memory_db : dict
    output_file : str | Path
    """

    output_file = Path(output_file)

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memory_db,
            f,
            ensure_ascii=False,
            indent=4
        )


def load_memory_database(input_file):
    """
    Load memory database.

    Parameters
    ----------
    input_file : str | Path

    Returns
    -------
    dict
    """

    input_file = Path(input_file)

    with open(
        input_file,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)