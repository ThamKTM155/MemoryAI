from pathlib import Path


def extract_relationships(file_path):

    file_path = Path(file_path)

    relationships = []

    inside_section = False

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            line = line.strip()
            print(repr(line))
            normalized = line.upper().replace("_", " ")

            if "RELATED DOCUMENTS" in normalized:

                inside_section = True

                continue

                inside_section = True

                continue

            if inside_section:

                if (
                    line.startswith("#")
                    and "RELATED_DOCUMENTS" not in line.upper()
                ):

                    normalized = line.upper().replace("_", " ")

                    if (
                        line.startswith("#")
                        and "RELATED DOCUMENTS" not in normalized
                    ):
                        break

                if line.startswith("-"):

                    target = line[1:].strip()

                    relationships.append(

                        {

                            "relation": "RELATED_TO",

                            "target": target

                        }

                    )

    return relationships