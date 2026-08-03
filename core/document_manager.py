from core.diary_loader import DiaryLoader
from core.document_classifier import DocumentClassifier


class DocumentManager:

    def __init__(self, diary_path):

        self.loader = DiaryLoader(diary_path)

        self.classifier = DocumentClassifier()

        self.documents = []

    def load(self):

        docs = self.loader.load_all()

        self.documents = []

        for doc in docs:

            doc = self.classifier.classify(doc)

            self.documents.append(doc)

    def get_all(self):

        return self.documents

    def get_by_type(self, doc_type):

        result = []

        for doc in self.documents:

            if doc["type"] == doc_type:

                result.append(doc)

        return result

    def count(self):

        return len(self.documents)

    def save_document(self, filename, content):

        self.loader.save_markdown(
            filename,
            content
        )