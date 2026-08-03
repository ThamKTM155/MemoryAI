from pathlib import Path


def parse_document_metadata(file_path):

    file_path = Path(file_path)

    updated = None
    status = None
    version = None

    if file_path.suffix.lower() != ".md":

        return {}

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        lines = [line.strip() for line in f]

    for i, line in enumerate(lines):

        if line == "Updated:" and i + 1 < len(lines):

            updated = lines[i + 1]

        elif line == "Status:" and i + 1 < len(lines):

            status = lines[i + 1]

        elif line == "Version:" and i + 1 < len(lines):

            version = lines[i + 1]

    return {

        "updated": updated,

        "status": status,

        "version": version

    }