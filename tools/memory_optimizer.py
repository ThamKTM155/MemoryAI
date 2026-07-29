"""
========================================================

MemoryAI

BUILD-037B

memory_optimizer.py

========================================================
"""

print(">>> memory_optimizer.py LOADED <<<")
def optimize_memories(memories):
    """
    Optimize memories before
    building context.
    """

    memories = deduplicate_content(memories)

    memories = filter_relationships(memories)

    return memories


def deduplicate_content(memories):
    """
    Remove duplicated content.
    """

    unique = []

    seen = set()
    print("DEBUG memories:", len(memories))

    for memory in memories:
        print(type(memory))
        print(memory)
        key = get_memory_key(memory)

        if key in seen:

            continue

        seen.add(key)

        unique.append(memory)

    return unique


def filter_relationships(memories):
    """
    Remove unnecessary relationships.
    """
    filtered = []

    seen = set()

    for memory in memories:

        if memory.get("_category") != "relationships":
            filtered.append(memory)
            continue

        key = (
            memory.get("type"),
            memory.get("to")
        )

        if key in seen:
            continue

        seen.add(key)
        filtered.append(memory)

    return filtered


def prune_context(memories):
    """
    Limit context size.
    """

    return memories


def validate_memories(memories):
    """
    Validate optimized memories.
    """

    return memories

def get_memory_key(memory):
    """
    Create a key used for
    duplicate detection.
    """

    if "decision" in memory:

        return (
            "decision",
            memory["decision"].strip().lower()
        )

    return str(memory)