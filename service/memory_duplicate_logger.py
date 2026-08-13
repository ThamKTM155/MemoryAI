from pathlib import Path
from datetime import datetime


LOG_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "duplicate_log.txt"
)


def log_duplicate(
    title,
    source,
):
    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"{datetime.now()}\n"
        )

        f.write(
            f"SOURCE: {source}\n"
        )

        f.write(
            f"TITLE: {title}\n"
        )

        f.write(
            "ACTION: DUPLICATE_BLOCKED\n"
        )

        f.write(
            "-" * 50
            + "\n"
        )