"""
==========================================
MEMORY SYNC V2
BUILD-19
==========================================
"""

import os
import shutil

# ==========================================
# PATH
# ==========================================

AUTOYOUTUBE = r"D:\AutoYouTube\autoyoutube_v22"

MEMORY = r"D:\MemoryAI\09_AI_Memory"

# ==========================================
# DESTINATION MAP
# ==========================================

DESTINATION = {

    "README.md":
        "05_Memory_Index",

    "CHANGELOG.md":
        "01_History",

    "PROJECT_HISTORY.md":
        "01_History",

    "SYSTEM_FREEZE.md":
        "04_System",

    "DESIGN_PHILOSOPHY.md":
        "00_Foundation"

}

# ==========================================
# COUNTER
# ==========================================

total = 0

# ==========================================
# WALK PROJECT
# ==========================================

for root, dirs, files in os.walk(AUTOYOUTUBE):

    for file in files:

        if file not in DESTINATION:

            continue

        source = os.path.join(
            root,
            file
        )

        folder = DESTINATION[file]

        destination_folder = os.path.join(
            MEMORY,
            folder
        )

        os.makedirs(
            destination_folder,
            exist_ok=True
        )

        #
        # tránh ghi đè cùng tên
        #

        relative = os.path.relpath(
            root,
            AUTOYOUTUBE
        )

        #
        # ROOT FOLDER
        #

        if relative == ".":

            safe_name = "ROOT"

        else:

            safe_name = relative.replace(
                "\\",
                "_"
            )

        destination = os.path.join(

            destination_folder,

            f"{safe_name}_{file}"

        )

        shutil.copy2(
            source,
            destination
        )

        total += 1

        print("SYNC")

        print("FROM :", source)

        print("TO   :", destination)

        print()

print("=" * 40)

print("TOTAL FILE :", total)

print("MEMORY SYNC COMPLETED")