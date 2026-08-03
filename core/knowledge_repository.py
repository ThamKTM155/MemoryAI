from core.document_manager import DocumentManager
from core.timeline_engine import TimelineEngine

class KnowledgeRepository:

    def __init__(self, diary_path):

        self.document_manager = DocumentManager(
            diary_path
        )

        self.documents = []

        self.by_type = {}

        self.by_filename = {}

        self.statistics = {}

        self.latest_daily_log = None

        self.latest_adr = None

        self.current_roadmap = None

        self.latest_build = None

        self.documents_by_date = {}

        self.timeline = TimelineEngine()

    def load(self):

        self.document_manager.load()

        self.documents = self.document_manager.get_all()

        self._build_filename_index()

        self._build_type_index()

        self._build_statistics()

        self._build_special_indexes()

        self.timeline.build(
            self.documents
        )

    def _build_filename_index(self):

        self.by_filename = {}

        for doc in self.documents:

            self.by_filename[
                doc["filename"]
            ] = doc

    def _build_type_index(self):

        self.by_type = {}

        for doc in self.documents:

            doc_type = doc["type"]

            if doc_type not in self.by_type:

                self.by_type[doc_type] = []

            self.by_type[
                doc_type
            ].append(doc)

    def _build_statistics(self):

        self.statistics = {

            "documents": len(self.documents)

        }

        for doc_type in self.by_type:

            self.statistics[
                doc_type
            ] = len(
                self.by_type[doc_type]
            )

    def _build_special_indexes(self):
        #
        # BUILD
        #

        builds = self.by_type.get("BUILD", [])

        if builds:

            self.latest_build = sorted(

                builds,

                key=lambda d: d["filename"]

            )[-1]
        #
        # Roadmap
        #

        roadmaps = self.by_type.get("ROADMAP", [])

        if roadmaps:

            self.current_roadmap = roadmaps[0]

        #
        # ADR
        #

        adrs = self.by_type.get("ADR", [])

        if adrs:

            self.latest_adr = sorted(

                adrs,

                key=lambda d: d["filename"]

            )[-1]

        #
        # Daily Logs
        #

        daily_logs = self.by_type.get("DAILY_LOG", [])

        if daily_logs:

            self.latest_daily_log = sorted(

                daily_logs,

                key=lambda d: d["filename"]

            )[-1]

        #
        # Index by filename
        #

        self.documents_by_date = {}

        for doc in daily_logs:

            self.documents_by_date[

                doc["filename"]

            ] = doc

    def save_document(self, filename, content):

        self.document_manager.save_document(
            filename,
            content
        )