# GRAPH_DATA_MODEL.md

# Memory Graph Data Model

Version:
1.0

Status:
BUILD-41A

---

# NODE

Mỗi Node phải có cấu trúc thống nhất.

Ví dụ

{
    "id": "",
    "type": "",
    "name": "",
    "description": "",
    "created": "",
    "updated": "",
    "tags": [],
    "properties": {}
}

---

# EDGE

Mỗi Edge phải có cấu trúc thống nhất.

{
    "from": "",
    "relation": "",
    "to": "",
    "created": ""
}

---

# GRAPH

Graph gồm hai phần

{
    "nodes": [],
    "edges": []
}

---

# Quy tắc

ID là duy nhất.

Không có Node trùng.

Không có Edge trùng.

Node không biết Node khác.

Quan hệ được lưu trong Edge.

---

Ví dụ

PROJECT

↓

BUILD

↓

FILE

↓

COMMIT

↓

DEPLOYMENT

được nối hoàn toàn bằng Edge.