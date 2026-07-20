from pathlib import Path


class DocumentClassifier:

    def classify(self, document):

        name = Path(
            document["filename"]
        ).stem.upper()

        if "ROADMAP" in name:

            document["type"] = "ROADMAP"

        elif name.startswith("ADR"):

            document["type"] = "ADR"

        elif "BUILD" in name:

            document["type"] = "BUILD"

        elif name.startswith("2026-"):

            document["type"] = "DAILY_LOG"

        else:

            document["type"] = "NOTE"

        return document