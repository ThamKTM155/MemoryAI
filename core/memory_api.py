from core.knowledge_repository import KnowledgeRepository
from core.knowledge_manager import KnowledgeManager
from core.memory_reasoning import MemoryReasoning
from core.build_parser import BuildParser

class Memory:

    def __init__(self, diary_path):

        self.diary_path = diary_path

        self.repository = KnowledgeRepository(diary_path)

        self.knowledge = KnowledgeManager(self.repository)

        self.reasoning = MemoryReasoning(self.repository)

    def load(self):

        self.repository.load()

    def summary(self):

        return self.reasoning.project_summary()

    def build_context(self):

        context = {

            "summary": self.summary(),

            "stats": self.stats(),

            "latest_build": self.get_latest_build(),

            "current_roadmap": self.get_current_roadmap(),

            "latest_adr": self.get_latest_adr()

        }

        return context

    def stats(self):

        return self.repository.statistics

    def search(self, keyword):

        return self.knowledge.search(keyword)


    def find_by_type(self, doc_type):

        return self.repository.by_type.get(
            doc_type,
            []
        )

    def find_by_date(self, date):

        results = []

        for filename, doc in self.repository.documents_by_date.items():

            if filename.startswith(date):

                results.append(doc)

        return results

    def get_latest_build(self):

        return self.reasoning.latest_build()

    def get_latest_build_info(self):

        build = self.get_latest_build()

        if build is None:
            return None

        parser = BuildParser()

        return parser.parse(build)

    def get_latest_adr(self):

        return self.reasoning.latest_adr()

    def get_current_roadmap(self):

        return self.reasoning.current_roadmap()

    def get_project_state(self):

        context = self.build_context()

        state = {

            "latest_build":
                context["latest_build"]["filename"],

            "current_roadmap":
                context["current_roadmap"]["filename"],

            "latest_adr":
                context["latest_adr"]["filename"],

            "documents":
                context["summary"]["documents"],

            "daily_logs":
                context["summary"]["daily_logs"],

            "status":
                "ACTIVE"

        }

        return state
        
    def get_build_history(self):

        return self.find_by_type("BUILD")

    def get_first_build(self):

        builds = self.get_build_history()

        if not builds:

            return None

        return sorted(

            builds,

            key=lambda d: d["filename"]

        )[0]

    def get_build_count(self):

        return len(

            self.get_build_history()

        )