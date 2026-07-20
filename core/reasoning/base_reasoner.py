class BaseReasoner:

    def __init__(self, memory):
        self.memory = memory

    def get_project_state(self):
        return self.memory.get_project_state()