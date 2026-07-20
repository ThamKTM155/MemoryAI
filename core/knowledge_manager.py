class KnowledgeManager:

    def __init__(self, repository):

        self.repository = repository

    def load(self):

        # Repository đã load rồi
        return

    def get_documents(self):

        return self.repository.documents

    def get_documents_by_type(self, doc_type):

        return self.repository.by_type.get(doc_type, [])

    def search(self, keyword):

        keyword = keyword.lower()

        results = []

        for doc in self.get_documents():

            if keyword in doc["content"].lower():

                results.append(doc)

        return results

    def summary(self):

        docs = self.get_documents()

        roadmap = len(
            self.get_documents_by_type("ROADMAP")
        )

        adr = len(
            self.get_documents_by_type("ADR")
        )

        daily = len(
            self.get_documents_by_type("DAILY_LOG")
        )

        note = len(
            self.get_documents_by_type("NOTE")
        )

        return {
            "documents": len(docs),
            "roadmaps": roadmap,
            "adrs": adr,
            "daily_logs": daily,
            "notes": note
        }