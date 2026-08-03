# GRAPH_SCHEMA.md

# THAM ECOSYSTEM
## Memory Graph Schema V1.0

Updated:
2026-08-02

Status:
BUILD-41A

---

# Mục tiêu

Memory Graph là bộ não chung của toàn bộ hệ sinh thái.

Mọi module đều đọc và ghi tri thức thông qua Memory Graph.

Không tạo các kho dữ liệu riêng biệt.

---

# NODE TYPES

PROJECT

Ví dụ

- MemoryAI
- ThamAI
- AutoYouTube
- Dashboard
- VoiceAI

---

BUILD

Ví dụ

- BUILD-40A
- BUILD-41A

---

DOCUMENT

Ví dụ

- README
- CHANGELOG
- ADR
- DESIGN

---

DIARY

Ví dụ

- Nhật ký
- Daily Journal

---

SUMMARY

Ví dụ

- 2026-08-02_summary.md

---

FILE

Ví dụ

- app.py
- memory_search.py

---

COMMIT

Ví dụ

- Git Commit

---

DEPLOYMENT

Ví dụ

- Render Production

---

PERSON

Ví dụ

- Founder
- Developer

---

MISSION

Ví dụ

- Phát triển hệ sinh thái AI
- Tạo giá trị thực

---

# EDGE TYPES

contains

belongs_to

creates

updates

documents

summarizes

implements

deploys

references

depends_on

learns_from

related_to

---

# CORE PRINCIPLES

1. Một nguồn tri thức chung.

2. Không lưu trùng dữ liệu.

3. Mọi module sử dụng Memory Graph.

4. Không phụ thuộc trực tiếp giữa các module.

5. Production luôn được ưu tiên.

6. Kiến trúc phải mở rộng được trong nhiều năm.

---

# DEVELOPMENT RULE

Thiết kế

↓

Test

↓

Git

↓

Deploy

↓

Freeze

---

# FUTURE

Memory Graph sẽ trở thành trung tâm của:

- MemoryAI
- ThamAI
- AutoYouTube
- Dashboard
- VoiceAI

và toàn bộ hệ sinh thái AI.