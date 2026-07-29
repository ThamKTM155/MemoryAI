"""
Memory Database Pipeline
BUILD-36.2

Pipeline:

Knowledge Directory
        │
        ▼
load_all_knowledge()
        │
        ▼
build_memory_database()
        │
        ▼
build_relationships()
        │
        ▼
verify_relationships()

Output:
    memory_db
"""

from pathlib import Path

from tools.knowledge_repository import load_all_knowledge
from tools.memory_database_builder import build_memory_database
from tools.memory_repository import (
    save_memory_database,
)
from core.memory_builder import (
    build_relationships,
    verify_relationships,
    update_memory_relationships,
)

def build_memory_database_pipeline(
    knowledge_dir,
    output_file=None
):
    """
    Build memory_db từ Knowledge Database.

    Parameters
    ----------
    knowledge_dir : str | Path

    Returns
    -------
    dict
        memory_db
    """

    knowledge_dir = Path(knowledge_dir)

    # =====================================
    # Load Knowledge Records
    # =====================================

    knowledge_records = load_all_knowledge(knowledge_dir)

    # =====================================
    # Build Memory Database
    # =====================================

    memory_db = build_memory_database(knowledge_records)

    # =====================================
    # Build Relationships
    # =====================================

    relationships = build_relationships(memory_db)

    # =====================================
    # Update Database
    # =====================================

    memory_db = update_memory_relationships(
        memory_db,
        relationships
    )

    # =====================================
    # Verify
    # =====================================

    result = verify_relationships(memory_db)
    # =====================================
    # Save Memory Database (Optional)
    # =====================================

    if output_file is not None:

        save_memory_database(
            memory_db,
            output_file
        )
    # Có thể bật khi debug
    # print_verify_report(result)

    return memory_db


if __name__ == "__main__":

    memory_db = build_memory_database_pipeline(
        "10_LongTermMemory/knowledge"
    )

    print("=" * 60)
    print("BUILD-36 COMPLETED")
    print("=" * 60)

    print()

    print("Keywords      :", len(memory_db["keywords"]))
    print("Projects      :", len(memory_db["projects"]))
    print("Decisions     :", len(memory_db["decisions"]))
    print("Lessons       :", len(memory_db["lessons"]))
    print("Tasks         :", len(memory_db["tasks"]))
    print("Relationships :", len(memory_db["relationships"]))