from pathlib import Path


def parse_summary(summary_file):
    """
    Đọc metadata từ một file Summary.

    Parameters
    ----------
    summary_file : str | Path

    Returns
    -------
    dict
    """

    summary_file = Path(summary_file)

    metadata = {
        "id": "",
        "date": "",
        "source": "",
        "version": "",
        "keywords": [],
        "projects": []
    }

    current_section = None

    with open(summary_file, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip()

            if line.startswith("ID:"):
                metadata["id"] = line[3:].strip()

            elif line.startswith("Date:"):
                metadata["date"] = line[5:].strip()

            elif line.startswith("Source:"):
                metadata["source"] = line[7:].strip()

            elif line.startswith("Version:"):
                metadata["version"] = line[8:].strip()

            elif line == "## Keywords":
                current_section = "keywords"

            elif line == "## Related Projects":
                current_section = "projects"

            elif line.startswith("##"):
                current_section = None

            elif line.startswith("- "):

                value = line[2:].strip()

                if current_section == "keywords":
                    metadata["keywords"].append(value)

                elif current_section == "projects":
                    metadata["projects"].append(value)

    return metadata