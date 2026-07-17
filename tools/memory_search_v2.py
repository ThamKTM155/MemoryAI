"""
==========================================
MEMORY SEARCH V2
Semantic Memory Search
BUILD-19
==========================================
"""

import os
import json

# ==========================================
# MEMORY
# ==========================================

MEMORY_ROOT = r"D:\MemoryAI\09_AI_Memory"

INDEX_FILE = os.path.join(

    MEMORY_ROOT,

    "memory_index_v2.json"

)
# ==========================================
# LOAD INDEX
# ==========================================

def load_index():

    if not os.path.exists(INDEX_FILE):

        return {}

    with open(

        INDEX_FILE,

        "r",

        encoding="utf-8"

    ) as f:

        return json.load(f)
# ==========================================
# READ DOCUMENT
# ==========================================

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
# ==========================================
# FIND MODULE
# ==========================================

def find_module(

    keyword,

    database

):

    keyword = keyword.lower()

    for module in database:

        if keyword in module.lower():

            return module

    return None
# ==========================================
# BUILD CONTEXT
# ==========================================

def build_context(

    module,

    database

):

    docs = database[module]

    context = []

    for name in [

        "README",

        "CHANGELOG",

        "PROJECT_HISTORY",

        "SYSTEM_FREEZE",

        "DESIGN_PHILOSOPHY"

    ]:

        path = docs.get(name)

        if not path:

            continue

        text = read_document(path)

        if not text:

            continue

        context.append(

            f"\n========== {name} ==========\n"

        )

        context.append(text)

    return "\n".join(context)
# ==========================================
# SEARCH MEMORY
# ==========================================

def search_memory(keyword):

    database = load_index()

    if not database:

        return "Memory Index chưa tồn tại."

    module = find_module(

        keyword,

        database

    )

    if not module:

        return "Không tìm thấy tri thức."

    return build_context(

        module,

        database

    )
# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    while True:

        keyword = input(

            "\nKeyword : "

        )

        print()

        print(

            search_memory(

                keyword

            )

        )