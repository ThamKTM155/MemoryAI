from dataclasses import dataclass, field


@dataclass
class GraphNode:

    node_id: str

    node_type: str

    label: str

    metadata: dict = field(default_factory=dict)