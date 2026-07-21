"""
planner_engine.py
=================

Planner Engine
"""


class PlannerEngine:

    def plan(self, reflection):

        if reflection is None:
            return None

        plan = {

            "goal": f"Review {reflection['node_id']}",

            "steps": [

                f"Open {reflection['node_id']}",

            ]

        }

        for node in reflection["related_nodes"]:

            plan["steps"].append(

                f"Review {node}"

            )

        return plan