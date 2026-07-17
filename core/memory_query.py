"""
Memory Query Engine
BUILD-24.1
"""

def query_project(project_intelligence, diary_id):

    if diary_id not in project_intelligence:
        return None

    return project_intelligence[diary_id]


def query_keyword(project_intelligence, keyword):

    results = []

    keyword = keyword.lower()

    for diary_id, info in project_intelligence.items():

        for item in info["keywords"]:

            if keyword in item.lower():

                results.append(diary_id)

                break

    return results