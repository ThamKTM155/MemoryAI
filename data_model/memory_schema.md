# MEMORY RECORD SCHEMA

Document ID: DM-001

Version: Draft 1.0

Status: Draft

---

# Purpose

Memory Record là đơn vị dữ liệu chuẩn (Canonical Data Model) của MemoryAI.

Tất cả module phải đọc và ghi theo schema này.

---

# Required Fields

| Field | Type | Description |
|--------|------|-------------|
| id | string | Unique ID |
| type | string | Memory type |
| title | string | Short title |
| content | string | Main content |
| project | string | Project name |
| source | string | Original source |
| created_at | datetime | Creation time |
| updated_at | datetime | Last update |

---

# Optional Fields

| Field | Type | Description |
|--------|------|-------------|
| reason | string | Why this record exists |
| tags | list | Search tags |
| relations | list | Related memory IDs |
| confidence | float | Confidence score |
| status | string | active / archived / frozen |
| metadata | dict | Future extension |

---

# Design Principles

- Stable schema
- Backward compatible
- Extensible
- Easy to serialize
- Human readable
- Machine friendly

---

# Status

Draft