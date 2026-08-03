def create_project_nodes(nodes):

    projects = {}

    for node in nodes:

        project = node.get("project")

        if not project:

            continue

        if project not in projects:

            projects[project] = {

                "id": project,

                "type": "PROJECT",

                "name": project

            }

    return list(projects.values())