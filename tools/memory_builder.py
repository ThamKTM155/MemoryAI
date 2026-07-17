import json
from pathlib import Path
from datetime import datetime
from core.memory_query import (
    query_project,
    query_keyword
)
from core.memory_router import memory_query
from core.memory_loader import (
    save_memory_db,
    load_memory_db
)
SUMMARY_INDEX = Path(
    r"D:\MemoryAI\11_Diary_Summary\summary_index.json"
)

MEMORY_DB = Path(
    r"D:\MemoryAI\11_Diary_Summary\memory_db.json"
)
SUMMARY_FOLDER = Path(
    r"D:\MemoryAI\11_Diary_Summary\summaries"
)

def load_summary_index():

    if not SUMMARY_INDEX.exists():

        print("Không tìm thấy summary_index.json")

        return []

    with open(

        SUMMARY_INDEX,

        "r",

        encoding="utf-8"

    ) as f:

        return json.load(f)

def build_metadata():

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )

    metadata = {

        "database": "Memory Core",

        "version": "BUILD-21.1",

        "schema_version": "1.0",

        "status": "Development",

        "created": today,

        "updated": today,

        "generated_by": "Memory Builder"

    }

    return metadata

def build_systems():

    systems = [

        {
            "id": "SYS-001",
            "name": "MemoryAI",
            "type": "Memory Platform",
            "status": "Development",
            "version": "BUILD-21.1",
            "priority": 1,
            "connected": True,
            "root": r"D:\MemoryAI",
            "description": "Long-Term Memory Platform"
        },

        {
            "id": "SYS-002",
            "name": "AutoYouTube",
            "type": "YouTube Automation",
            "status": "Production",
            "version": "V22",
            "priority": 2,
            "connected": True,
            "root": r"D:\AutoYouTube",
            "description": "YouTube Automation System"
        },

        {
            "id": "SYS-003",
            "name": "ThamAI",
            "type": "AI Assistant",
            "status": "Development",
            "version": "V1",
            "priority": 3,
            "connected": True,
            "root": r"D:\ThamAI_Backend_new",
            "description": "Personal AI Assistant"
        },

        {
            "id": "SYS-004",
            "name": "TalkingAI Kids",
            "type": "Education AI",
            "status": "Hibernated",
            "version": "V1",
            "priority": 4,
            "connected": False,
            "root": r"D:\TalkingAI_Kids",
            "description": "Interactive AI for Children"
        }

    ]

    return systems

def build_memory(

    metadata,

    systems,

    projects,

    diaries,

    decisions,

    lessons,

    tasks,
    
    keywords,

    relationships,

    project_intelligence
):

    memory = {

        "metadata": metadata,

        "systems": systems,

        "projects": projects,

        "diaries": diaries,

        "decisions": decisions,

        "lessons": lessons,

        "tasks": tasks,

        "keywords": keywords,

        "relationships": relationships,

        "project_intelligence": project_intelligence

    }

    return memory

def show_metadata(metadata):

    print()

    print("Metadata")

    print("-" * 30)

    for key, value in metadata.items():

        print(f"{key:18}: {value}")
        
def show_systems(systems):

    print()

    print("Systems")

    print("-" * 30)

    for system in systems:

        print(

            f"{system['id']}  "

            f"{system['name']}"

            f"  ({system['status']})"

        )

def show_projects(projects):

    print()

    print("Projects")

    print("-" * 30)

    for project in projects:

        print(

            f"{project['id']}  "

            f"{project['name']}"

            f"  ({project['status']})"

        )

def show_diaries(diaries):

    print()

    print("Diaries")

    print("-" * 30)

    for diary in diaries:

        print(

            f"{diary['date']}"

            f" | "

            f"{diary['id']}"

        )

def show_memory(memory):

    print()

    print("Memory Core")

    print("-" * 30)

    for section in memory:

        print(section)

def show_summary_ids(data):

    print()

    print("Summary IDs")

    print("-" * 30)

    for item in data:

        print(item["id"])

def show_decisions(decisions):

    print()

    print("Decisions")

    print("-" * 30)

    print(f"Total : {len(decisions)}")

    print()

    for item in decisions:

        print(

            f"[{item['diary_id']}] "

            f"{item['decision']}"

        )

def show_lessons(lessons):

    print()

    print("Lessons")

    print("-" * 30)

    print(f"Total : {len(lessons)}")

    print()

    for item in lessons:

        print(

            f"[{item['diary_id']}] "

            f"{item['lesson']}"

        )

def show_tasks(tasks):

    print()

    print("Tasks")

    print("-" * 30)

    print(f"Total : {len(tasks)}")

def show_keywords(keywords):

    print()

    print("Keywords")

    print("-" * 30)

    print(f"Total : {len(keywords)}")

def show_relationships(relationships):

    print()

    print("Relationships")

    print("-" * 30)

    print(f"Total : {len(relationships)}")

    print()

    for rel in relationships:

        print(

            f"{rel['from']}"

            f" --{rel['type']}--> "

            f"{rel['to']}"

        )

def show_project_intelligence(data):

    print()

    print("Project Intelligence")

    print("-" * 30)

    for diary_id, info in data.items():

        print(diary_id)

        print(

            f"  Decisions : {len(info['decisions'])}"

        )

        print(

            f"  Lessons   : {len(info['lessons'])}"

        )

        print(

            f"  Tasks     : {len(info['tasks'])}"

        )

        print(

            f"  Keywords  : {len(info['keywords'])}"

        )

        print()

def show_query_result(result):

    print()

    print("Query Result")

    print("-" * 30)

    if result is None:

        print("Không tìm thấy.")

        return

    print("Decisions")

    for item in result["decisions"]:

        print(" -", item)

    print()

    print("Lessons")

    for item in result["lessons"]:

        print(" -", item)

    print()

    print("Tasks")

    for item in result["tasks"]:

        print(" -", item)

    print()

    print("Keywords")

    for item in result["keywords"]:

        print(" -", item)

def show_keyword_query(keyword, results):

    print()

    print("Keyword Query")

    print("-" * 30)

    print("Keyword :", keyword)

    print()

    if not results:

        print("Không tìm thấy.")

        return

    for diary_id in results:

        print(" -", diary_id)

def validate_memory(memory):

    print()

    print("Validation")

    print("-" * 30)

    required_sections = [

        "metadata",

        "systems",

        "projects",

        "diaries",

        "decisions",

        "lessons",

        "tasks",

        "keywords",

        "relationships"

    ]

    success = True

    for section in required_sections:

        if section in memory:

            print(f"✅ {section}")

        else:

            print(f"❌ {section}")

            success = False

    return success

def build_projects():

    projects = [

        {
            "id": "PRJ-001",
            "system": "MemoryAI",
            "name": "Diary Summary",
            "status": "Production",
            "version": "BUILD-20.3"
        },

        {
            "id": "PRJ-002",
            "system": "MemoryAI",
            "name": "Memory Search",
            "status": "Production",
            "version": "BUILD-20.5.1"
        },

        {
            "id": "PRJ-003",
            "system": "MemoryAI",
            "name": "Memory Builder",
            "status": "Development",
            "version": "BUILD-21.1"
        },

        {
            "id": "PRJ-004",
            "system": "MemoryAI",
            "name": "Summary Index",
            "status": "Production",
            "version": "BUILD-20.3"
        }

    ]

    return projects

def build_diaries():

    diaries = []

    files = sorted(
        SUMMARY_FOLDER.glob("*_summary.md")
    )

    for file in files:

        text = read_summary_file(file)

        diaries.append({

            "id": extract_field(text, "ID:"),

            "date": extract_field(text, "Date:"),

            "version": extract_field(text, "Version:"),

            "source": extract_field(text, "Source:"),

            "file": file.name,

            "path": str(file)

        })

    return diaries

def build_decisions():

    decisions = []

    seen = set()

    files = sorted(

        SUMMARY_FOLDER.glob("*_summary.md")

    )

    for file in files:

        text = read_summary_file(file)

        diary_id = extract_field(

            text,

            "ID:"

        )

        items = extract_list(

            text,

            "## Decisions"

        )

        for item in items:

            key = (diary_id, item)

            if key in seen:

                continue

            seen.add(key)

            decisions.append({

                "diary_id": diary_id,

                "decision": item

            })

    return decisions

def build_lessons():

    lessons = []

    seen = set()

    files = sorted(

        SUMMARY_FOLDER.glob("*_summary.md")

    )

    for file in files:

        text = read_summary_file(file)

        diary_id = extract_field(

            text,

            "ID:"

        )

        items = extract_list(

            text,

            "## Lessons"

        )

        for item in items:

            key = (diary_id, item)

            if key in seen:

                continue

            seen.add(key)

            lessons.append({

                "diary_id": diary_id,

                "lesson": item

            })

    return lessons

def build_tasks():

    tasks = []

    seen = set()

    files = sorted(

        SUMMARY_FOLDER.glob("*_summary.md")

    )

    for file in files:

        text = read_summary_file(file)

        diary_id = extract_field(

            text,

            "ID:"

        )

        items = extract_list(

            text,

            "## Tasks"

        )

        for item in items:

            key = (diary_id, item)

            if key in seen:

                continue

            seen.add(key)

            tasks.append({

                "diary_id": diary_id,

                "task": item

            })

    return tasks

def build_keywords():

    keywords = []

    seen = set()

    files = sorted(

        SUMMARY_FOLDER.glob("*_summary.md")

    )

    for file in files:

        text = read_summary_file(file)

        diary_id = extract_field(

            text,

            "ID:"

        )

        items = extract_list(

            text,

            "## Keywords"

        )

        for item in items:

            key = (diary_id, item)

            if key in seen:

                continue

            seen.add(key)

            keywords.append({

                "diary_id": diary_id,

                "keyword": item

            })

    return keywords

def build_relationships(

    diaries,

    decisions,

    lessons,

    tasks,

    keywords

):

    relationships = []

    for item in decisions:

        relationships.append({

            "from": item["diary_id"],

            "to": item["decision"],

            "type": "HAS_DECISION"

        })

    for item in lessons:

        relationships.append({

            "from": item["diary_id"],

            "to": item["lesson"],

            "type": "HAS_LESSON"

        })

    for item in tasks:

        relationships.append({

            "from": item["diary_id"],

            "to": item["task"],

            "type": "HAS_TASK"

        })

    for item in keywords:

        relationships.append({

            "from": item["diary_id"],

            "to": item["keyword"],

            "type": "HAS_KEYWORD"

        })

    return relationships

def build_project_intelligence(

    decisions,

    lessons,

    tasks,

    keywords

):

    intelligence = {}

    def ensure(diary_id):

        if diary_id not in intelligence:

            intelligence[diary_id] = {

                "decisions": [],

                "lessons": [],

                "tasks": [],

                "keywords": []

            }

    for item in decisions:

        ensure(item["diary_id"])

        intelligence[item["diary_id"]]["decisions"].append(

            item["decision"]

        )

    for item in lessons:

        ensure(item["diary_id"])

        intelligence[item["diary_id"]]["lessons"].append(

            item["lesson"]

        )

    for item in tasks:

        ensure(item["diary_id"])

        intelligence[item["diary_id"]]["tasks"].append(

            item["task"]

        )

    for item in keywords:

        ensure(item["diary_id"])

        intelligence[item["diary_id"]]["keywords"].append(

            item["keyword"]

        )

    return intelligence

def extract_list(text, section):

    lines = text.splitlines()

    results = []

    inside = False

    for line in lines:

        if line.strip() == section:

            inside = True

            continue

        if inside:

            if line.startswith("## "):

                break

            line = line.strip()

            if line.startswith("- "):

                results.append(

                    line[2:].strip()

                )

    return results

def read_summary_file(file):

    with open(

        file,

        "r",

        encoding="utf-8"

    ) as f:

        return f.read()

def extract_field(text, field):

    start = text.find(field)

    if start == -1:

        return ""

    start += len(field)

    end = text.find("\n", start)

    if end == -1:

        end = len(text)

    return text[start:end].strip()

def main():

    # ==========================
    # Load dữ liệu
    # ==========================

    data = load_summary_index()

    # ==========================
    # Build Memory Core
    # ==========================

    metadata = build_metadata()

    systems = build_systems()

    projects = build_projects()

    diaries = build_diaries()

    decisions = build_decisions()

    lessons = build_lessons()

    tasks = build_tasks()

    keywords = build_keywords()

    relationships = build_relationships(

        diaries,

        decisions,

        lessons,

        tasks,

        keywords

    )

    project_intelligence = build_project_intelligence(

        decisions,

        lessons,

        tasks,

        keywords

    )

    memory = build_memory(

        metadata,

        systems,

        projects,

        diaries,

        decisions,

        lessons,

        tasks,

        keywords,

        relationships,

        project_intelligence

    )
    print()

    print("=" * 60)

    print("SUMMARY INDEX")

    print("=" * 60)

    print()

    print(f"Tổng số Summary : {len(data)}")

    show_metadata(metadata)

    show_systems(systems)

    show_projects(projects)

    show_diaries(diaries)

    show_decisions(decisions)

    show_lessons(lessons)

    show_tasks(tasks)

    show_keywords(keywords)

    show_relationships(relationships)

    show_project_intelligence(project_intelligence)

    result = query_project(

        project_intelligence,

        "DS-2026-06-16"

    )

    show_query_result(result)

    keyword_results = query_keyword(

        project_intelligence,

        "MemoryAI"

    )

    show_keyword_query(

        "MemoryAI",

        keyword_results

    )    
    print()
    print("Memory Router")
    print("-" * 30)

    router_result = memory_query(

        project_intelligence,

        "keyword",

        "MemoryAI"

    )

    print(router_result)
    show_memory(memory)

    ok = validate_memory(memory)

    show_summary_ids(data)

    print()
    if ok:

        print("✅ Memory Core Validation PASSED")

        save_memory_db(
            memory,
            MEMORY_DB
        )

        loaded_memory = load_memory_db(MEMORY_DB)
        print(type(loaded_memory))
        print(loaded_memory.keys())
        print()
        print("Memory Loader")
        print("------------------------------")

        for key in loaded_memory.keys():
            print(key)

    else:

        print("❌ Memory Core Validation FAILED")
        
if __name__ == "__main__":

    main()