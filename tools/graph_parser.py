from pathlib import Path


def parse_metadata(file_path):

    file_path = Path(file_path)

    node_type = "DOCUMENT"

    date = None
    project = None

    path_text = str(file_path).lower()

    if "11_diary_summary" in path_text:

        project = "MemoryAI"

    elif "\\docs\\" in path_text:

        project = "MemoryGraph"

    if "_summary.md" in file_path.name.lower():

        node_type = "SUMMARY"

    parts = file_path.stem.split("_")

    if len(parts) > 0:

        first = parts[0]

        if (
            len(first) == 10
            and first[4] == "-"
            and first[7] == "-"
        ):
            date = first
    build = None

    parts = file_path.stem.split("_")

    for part in parts:

        upper = part.upper()

        if upper.startswith("BUILD-"):

            build = upper

            break

    updated = None
    status = None
    version = None

    if file_path.suffix.lower() == ".md":

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            for line in f:

                line = line.strip()

                if line.startswith("Updated:"):

                    updated = line.replace(
                        "Updated:",
                        ""
                    ).strip()

                elif line.startswith("Status:"):

                    status = line.replace(
                        "Status:",
                        ""
                    ).strip()

                elif line.startswith("Version:"):

                    version = line.replace(
                        "Version:",
                        ""
                    ).strip()

    return {

        "id": file_path.stem,

        "type": node_type,

        "name": file_path.name,

        "extension": file_path.suffix,

        "path": str(file_path),

        "project": project,

        "build": build,

        "date": date,

        "updated": updated,

        "status": status,

        "version": version,

        "tags": [],

        "links": []

    }