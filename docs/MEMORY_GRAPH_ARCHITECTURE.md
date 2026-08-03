# MEMORY_GRAPH_ARCHITECTURE.md

# THAM ECOSYSTEM

## Memory Graph Architecture V1.0

Updated:
2026-08-03

Status:
BUILD-47A

---

# MỤC TIÊU

Memory Graph là trung tâm tri thức của toàn bộ hệ sinh thái.

Mọi module đều sử dụng chung Memory Graph để lưu trữ và truy vấn tri thức.

Không module nào được xây dựng kho tri thức riêng nếu dữ liệu đã tồn tại trong Memory Graph.

---

# KIẾN TRÚC TỔNG THỂ

Document
        │
        ▼
Graph Parser
        │
        ▼
Metadata
        │
        ▼
Entity Builder
        │
        ▼
Relationship Parser
        │
        ▼
Edge Builder
        │
        ▼
Memory Graph
        │
        ▼
Query Engine
        │
        ▼
AI Assistant

---

# CÁC MODULE

graph_parser.py

Đọc dữ liệu nguồn.

Sinh Metadata.

---

graph_entity_builder.py

Sinh Entity.

Không đọc File.

---

graph_relationship_parser.py

Sinh Relationship.

Không tạo Entity.

---

graph_edge_builder.py

Sinh Edge.

Không đọc File.

---

memory_graph_builder.py

Điều phối toàn bộ Pipeline.

Không chứa Business Logic.

---

# PIPELINE

Source

↓

Parser

↓

Metadata

↓

Entity

↓

Relationship

↓

Edge

↓

Knowledge Graph

---

# NGUYÊN TẮC

Parser chỉ Parse.

Entity Builder chỉ tạo Entity.

Relationship Parser chỉ tạo Relationship.

Edge Builder chỉ tạo Edge.

Memory Builder chỉ điều phối.

---

# MỤC TIÊU PHÁT TRIỂN

Tăng Entity.

Tăng Relationship.

Tăng chất lượng Metadata.

Tăng khả năng Query.

Không tăng độ phức tạp của Engine.

---

# FREEZE

Kiến trúc này được Freeze từ BUILD-47A.

Mọi BUILD tiếp theo phải tuân thủ tài liệu này.
