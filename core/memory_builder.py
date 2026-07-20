"""
Memory Builder
BUILD-34.4

Nhiệm vụ:
- Sinh relationships
- Verify relationships
- In báo cáo
- Chuẩn bị lưu Database
"""


def build_relationships(memory_db):

    relationships = []

    # ===============================
    # Keywords
    # ===============================

    for item in memory_db.get("keywords", []):

        relationships.append({
            "from": item["diary_id"],
            "to": item["keyword"],
            "type": "HAS_KEYWORD"
        })

    # ===============================
    # Decisions
    # ===============================

    for item in memory_db.get("decisions", []):

        relationships.append({
            "from": item["diary_id"],
            "to": item["decision"],
            "type": "HAS_DECISION"
        })

    # ===============================
    # Lessons
    # ===============================

    for item in memory_db.get("lessons", []):

        relationships.append({
            "from": item["diary_id"],
            "to": item["lesson"],
            "type": "HAS_LESSON"
        })

    # ===============================
    # Tasks
    # ===============================

    for item in memory_db.get("tasks", []):

        relationships.append({
            "from": item["diary_id"],
            "to": item["task"],
            "type": "HAS_TASK"
        })

    return relationships


def verify_relationships(memory_db):

    old_relationships = memory_db.get("relationships", [])

    new_relationships = build_relationships(memory_db)

    old_set = {
        (r["from"], r["to"], r["type"])
        for r in old_relationships
    }

    new_set = {
        (r["from"], r["to"], r["type"])
        for r in new_relationships
    }

    return {
        "old_count": len(old_set),
        "new_count": len(new_set),
        "added": sorted(new_set - old_set),
        "removed": sorted(old_set - new_set),
        "relationships": new_relationships
    }


def print_verify_report(result):

    print()
    print("=" * 50)
    print("MEMORY BUILDER VERIFY")
    print("=" * 50)

    print()

    print("Old Relationships :", result["old_count"])
    print("New Relationships :", result["new_count"])

    print()

    print("Added   :", len(result["added"]))
    print("Removed :", len(result["removed"]))

    print()

    if not result["added"] and not result["removed"]:

        print("STATUS : PASS")

    else:

        print("STATUS : CHANGED")

        if result["added"]:

            print()
            print("Added:")

            for item in result["added"]:
                print(item)

        if result["removed"]:

            print()
            print("Removed:")

            for item in result["removed"]:
                print(item)


def update_memory_relationships(memory_db, relationships):

    memory_db["relationships"] = relationships

    return memory_db