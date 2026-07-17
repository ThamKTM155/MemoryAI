"""
==========================================
SEMANTIC MEMORY INDEX V2
BUILD-19
==========================================
"""

import os
import json

# ==========================================
# MEMORY ROOT
# ==========================================

MEMORY = r"D:\MemoryAI\09_AI_Memory"

# Chỉ index các thư mục đồng bộ
SYNC_FOLDERS = [

    "00_Foundation",
    "01_History",
    "04_System",
    "05_Memory_Index"

]

INDEX_FILE = os.path.join(
    MEMORY,
    "memory_index_v2.json"
)

# ==========================================
# DATABASE
# ==========================================

database = {}

# ==========================================
# WALK
# ==========================================

for folder in SYNC_FOLDERS:

    folder_path = os.path.join(
        MEMORY,
        folder
    )

    if not os.path.exists(folder_path):
        continue

    for file in os.listdir(folder_path):

        if not file.endswith(".md"):
            continue

        filename = file[:-3]

        #
        # ROOT
        #

        if filename.startswith("ROOT_"):

            module = "ROOT"

            doc = filename.replace(
                "ROOT_",
                ""
            )

        else:

            parts = filename.split("_")

            if len(parts) < 2:
                continue

            doc = parts[-1]

            module = "_".join(parts[:-1])

        if module not in database:

            database[module] = {

                "README": None,
                "CHANGELOG": None,
                "PROJECT_HISTORY": None,
                "SYSTEM_FREEZE": None,
                "DESIGN_PHILOSOPHY": None

            }

        if doc in database[module]:

            database[module][doc] = os.path.join(
                folder_path,
                file
            )

# ==========================================
# SAVE
# ==========================================

with open(

    INDEX_FILE,

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        database,

        f,

        indent=4,

        ensure_ascii=False

    )

print("=" * 40)

print("MODULE :", len(database))

print("INDEX :", INDEX_FILE)

print("DONE")