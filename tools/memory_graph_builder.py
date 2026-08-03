from pathlib import Path
import json
from pathlib import Path

from tools.graph_parser import parse_metadata
from tools.graph_document_metadata import parse_document_metadata
from tools.graph_edge_builder import create_edges
from tools.graph_node_builder import create_node
from tools.graph_entity_builder import create_entities
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config" / "graph_sources.json"
OUTPUT_GRAPH = BASE_DIR / "memory_graph.json"

def load_sources():

    with open(
        CONFIG_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        config = json.load(f)

    return config["sources"]

def scan_source(source):

    src = BASE_DIR / source["path"]

    pattern = source["pattern"]

    files = list(src.rglob(pattern))

    print()

    print(f"[SOURCE] {source['name']}")

    print(f"Pattern : {pattern}")

    print(f"Files   : {len(files)}")

    return files

print("=" * 60)
print("MEMORY GRAPH BUILDER")
print("=" * 60)

sources = load_sources()
nodes = []
edges = []
for source in sources:

    files = scan_source(source)

    for file in files:

        metadata = parse_metadata(file)

        document_metadata = parse_document_metadata(file)

        metadata.update(document_metadata)

        node = create_node(metadata)

        nodes.append(node)

        node_edges = create_edges(node)

        edges.extend(node_edges)
project_nodes = create_entities(
    nodes,
    field="project",
    entity_type="PROJECT"
)

nodes.extend(project_nodes)

build_nodes = create_entities(
    nodes,
    field="build",
    entity_type="BUILD"
)

nodes.extend(build_nodes)

print()

print("=" * 60)
print(f"TOTAL NODES : {len(nodes)}")
print(f"TOTAL EDGES : {len(edges)}")
print("=" * 60)

with open(
    OUTPUT_GRAPH,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        {
            "nodes": nodes,
            "edges": edges
        },
        f,
        ensure_ascii=False,
        indent=2
    )

print()
print(f"Saved : {OUTPUT_GRAPH}")