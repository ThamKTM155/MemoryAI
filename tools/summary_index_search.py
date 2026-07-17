import json
from pathlib import Path

INDEX_FILE = Path(
    r"D:\MemoryAI\11_Diary_Summary\summary_index.json"
)


def load_index():

    if not INDEX_FILE.exists():

        return []

    with open(
        INDEX_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def search_index(query):

    query = (
    query
    .replace(":", "")
    .strip()
    .lower()
)

    database = load_index()

  
    results = []

    for item in database:

        if query == item["date"].lower():

            results.append(item)

            continue

        if any(
            query == p.lower()
            for p in item["projects"]
        ):

            results.append(item)

            continue

        if any(
            query == k.lower()
            for k in item["keywords"]
        ):

            results.append(item)

            continue

    return results


if __name__ == "__main__":

    while True:

        q = input(
            "\nSearch : "
        ).strip()

        if q.lower() in [

            "exit",

            "quit"

        ]:

            break

        result = search_index(q)

        print()

        if not result:

            print("Không tìm thấy.")

            continue

        for r in result:

            print("=" * 60)

            print("ID      :", r["id"])

            print("Date    :", r["date"])

            print("Source  :", r["source"])

            print("Projects:", ", ".join(r["projects"]))

            print("Keywords:", ", ".join(r["keywords"]))