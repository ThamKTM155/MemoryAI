"""
Memory Classification Engine
BUILD-70E

Classify memories into:

- core
- knowledge
- operational
"""

CORE_TITLES = {
    "SYSTEM CONSTITUTION",
    "MEMORYAI MISSION",
    "MEMORYAI VALUES",
    "MEMORYAI PRINCIPLES",
    "OWNER VISION",
}

KNOWLEDGE_TITLES = {
    "THAMAI ROLE",
    "THAMAI COMPETENCY MATRIX",
    "AUTOYOUTUBE FACTORY",
}


def classify_memory(title):

    title = (
        title.strip()
        .upper()
    )

    if title in CORE_TITLES:
        return "core"

    if title in KNOWLEDGE_TITLES:
        return "knowledge"

    return "operational"