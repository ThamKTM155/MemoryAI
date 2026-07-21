from dataclasses import dataclass


@dataclass
class Relationship:
    """
    Relationship between two memory records.
    """

    source_id: str
    target_id: str
    relation_type: str
    confidence: float = 1.0