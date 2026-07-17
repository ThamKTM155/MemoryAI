"""
==========================================
MEMORY SEARCH V3
Knowledge Search
BUILD-20
==========================================
"""

import os
import json

MEMORY_ROOT = r"D:\MemoryAI\09_AI_Memory"

INDEX_FILE = os.path.join(
    MEMORY_ROOT,
    "memory_index_v2.json"
)


def load_index():

    if not os.path.exists(INDEX_FILE):
        return {}

    with open(
        INDEX_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def read_document(path):

    if not path:
        return ""

    if not os.path.exists(path):
        return ""

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


def search_memory(keyword):

    database = load_index()

    keyword = keyword.lower()

    results = []

    for module_name, docs in database.items():

        if keyword in module_name.lower():

            score = 100

        else:

            score = 0

        for doc_type, path in docs.items():

            text = read_document(path)

            if not text:
                continue

            count = text.lower().count(keyword)

            if count == 0:
                continue

            results.append({

                "module": module_name,

                "title": doc_type,

                "score": score + count,

                "content": text,

                "path": path

            })

    results.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return results


if __name__ == "__main__":

    while True:

        keyword = input("\nKeyword : ")

        docs = search_memory(keyword)

        print("\nFOUND :", len(docs))

        print()

        for doc in docs[:5]:

            print("=" * 80)

            print(doc["module"])

            print(doc["title"])

            print("Score :", doc["score"])

            print(doc["path"])

            print()