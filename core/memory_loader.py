"""
Memory Loader
BUILD-24.3
"""

import json


def save_memory_db(memory, output_file):

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            memory,
            f,
            indent=4,
            ensure_ascii=False
        )

    print()
    print("💾 Memory Database Saved")
    print(output_file)
    
def load_memory_db(input_file):

    with open(input_file, "r", encoding="utf-8") as f:
        memory = json.load(f)

    return memory