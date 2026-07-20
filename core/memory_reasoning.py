class MemoryReasoning:

    def __init__(self, repository):

        self.repository = repository

    def latest_build(self):

        return self.repository.latest_build

    def current_roadmap(self):

        return self.repository.current_roadmap

    def latest_adr(self):

        return self.repository.latest_adr

    def project_summary(self):

        stats = self.repository.statistics

        return {

            "documents": stats.get("documents", 0),

            "daily_logs": stats.get("DAILY_LOG", 0),

            "roadmaps": stats.get("ROADMAP", 0),

            "adrs": stats.get("ADR", 0),

            "notes": stats.get("NOTE", 0),

            "latest_build":

                self.repository.latest_build["filename"]

                if self.repository.latest_build

                else None,

            "current_roadmap":

                self.repository.current_roadmap["filename"]

                if self.repository.current_roadmap

                else None,

            "latest_adr":

                self.repository.latest_adr["filename"]

                if self.repository.latest_adr

                else None,

        }