import re
from datetime import datetime


class TimelineEngine:

    def __init__(self):

        self.timeline = []

    def build(self, documents):

        self.timeline = []

        for doc in documents:

            date = self.extract_date(doc["filename"])

            if date:

                self.timeline.append({

                    "date": date,

                    "document": doc

                })

        self.timeline.sort(

            key=lambda x: x["date"]

        )

    def extract_date(self, text):

        match = re.search(

            r"\d{4}-\d{2}-\d{2}",

            text

        )

        if not match:

            return None

        return datetime.strptime(

            match.group(),

            "%Y-%m-%d"

        ).date()

    def latest(self):

        if not self.timeline:

            return None

        return self.timeline[-1]

    def earliest(self):

        if not self.timeline:

            return None

        return self.timeline[0]