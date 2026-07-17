"""
==========================================
MEMORY INDEX BUILDER
BUILD-19
==========================================
"""

import os
import json

# ==========================================
# MEMORY ROOT
# ==========================================

MEMORY = r"D:\MemoryAI\09_AI_Memory"

# ==========================================
# INDEX FILE
# ==========================================

INDEX_FILE = os.path.join(
    MEMORY,
    "memory_index.json"
)

# ==========================================
# DOCUMENT TYPES
# ==========================================

DOCUMENT_TYPES = [

    "README.md",
    "CHANGELOG.md",
    "PROJECT_HISTORY.md",
    "SYSTEM_FREEZE.md",
    "DESIGN_PHILOSOPHY.md"

]

# ==========================================
# BUILD INDEX
# ==========================================

index = {}

for root, dirs, files in os.walk(MEMORY):

    for file in files:

        if not any(

            file.endswith(doc)

            for doc in DOCUMENT_TYPES

        ):

            continue

        filepath = os.path.join(

            root,

            file

        )

        name = os.path.splitext(file)[0]

        if name not in index:

            index[name] = []

        index[name].append({

            "file": file,

            "path": filepath,

            "folder": os.path.basename(root)

        })

# ==========================================
# SAVE
# ==========================================

with open(

    INDEX_FILE,

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        index,

        f,

        indent=4,

        ensure_ascii=False

    )

print("=" * 40)

print("TOTAL INDEX :", len(index))

print("INDEX FILE :", INDEX_FILE)

print("DONE")