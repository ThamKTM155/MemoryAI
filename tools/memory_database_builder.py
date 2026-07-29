"""
Memory Database Builder
BUILD-36.1

Nhiệm vụ:
- Chuyển Knowledge Records thành memory_db.
- Không Build Relationships.
- Không Parse Summary.
- Không Save Database.
"""

from copy import deepcopy


def build_memory_database(knowledge_records):
    """
    Build memory_db từ Knowledge Records.

    Parameters
    ----------
    knowledge_records : list[dict]

    Returns
    -------
    dict
        memory_db
    """

    memory_db = {
        "keywords": [],
        "projects": [],
        "decisions": [],
        "lessons": [],
        "tasks": [],
        "relationships": []
    }

    for record in knowledge_records:

        diary_id = record.get("id", "")

        # ===============================
        # Keywords
        # ===============================

        for keyword in record.get("keywords", []):

            memory_db["keywords"].append({
                "diary_id": diary_id,
                "keyword": keyword
            })

        # ===============================
        # Projects
        # ===============================

        for project in record.get("projects", []):

            memory_db["projects"].append({
                "diary_id": diary_id,
                "project": project
            })

        # ===============================
        # Decisions
        # ===============================

        for decision in record.get("decisions", []):

            memory_db["decisions"].append({
                "diary_id": diary_id,
                "decision": decision
            })

        # ===============================
        # Lessons
        # ===============================

        for lesson in record.get("lessons", []):

            memory_db["lessons"].append({
                "diary_id": diary_id,
                "lesson": lesson
            })

        # ===============================
        # Tasks
        # ===============================

        for task in record.get("tasks", []):

            memory_db["tasks"].append({
                "diary_id": diary_id,
                "task": task
            })

    return deepcopy(memory_db)