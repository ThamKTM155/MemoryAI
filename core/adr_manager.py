from core.diary_loader import DiaryLoader
from core.document_classifier import DocumentClassifier


class ADRManager:

    def __init__(self, diary_path):

        self.loader = DiaryLoader(diary_path)

        self.classifier = DocumentClassifier()

        self.decisions = []

    def load(self):

        docs = self.loader.load_all()

        self.decisions = []

        for doc in docs:

            doc = self.classifier.classify(doc)

            if doc["type"] == "ADR":
            
                self.decisions.append(doc)

    def status(self):

        print("=" * 60)

        print("ADR MANAGER")

        print("=" * 60)

        print()

        print(f"Total ADR : {len(self.decisions)}")

        print()

        for adr in self.decisions:

            print("✓", adr["filename"])