# BUILD-59

# UNIFICATION MAP

Ngày: 2026-08-05

---
## Nguyên tắc

Không chuyển code.

Chỉ chuyển vai trò.

Sau khi vai trò ổn định mới chuyển code.
---
# I. CORE DOMAIN (BUILD-21)

| Module | Vai trò | Trạng thái |
|---------|----------|------------|
| MemoryRecord | Canonical Data Model | KEEP |
| MemoryFactory | Object Factory | KEEP |
| MemoryValidator | Validation | KEEP |
| MemoryRepository | Repository Layer | KEEP |
| MemoryService | Business Layer | KEEP |

---

# II. APPLICATION LAYER (MemoryAI)

| Module | Vai trò | Trạng thái |
|---------|----------|------------|
| Knowledge Gate | Dispatcher | KEEP |
| Identity Gateway | Gateway | KEEP |
| Repository Gateway | Gateway | KEEP |
| Graph Gateway | Gateway | KEEP |
| AI Gateway | Gateway | KEEP |

---

# III. TOOLS

Chưa kiểm kê.

---

# IV. SERVICES

Đang kiểm kê.

---

# V. KẾT LUẬN

Core Domain sẽ không bị thay thế.

Application Layer sẽ mở rộng dựa trên Core Domain.

## Kiến trúc hợp nhất

Frontend

↓

Backend

↓

Knowledge Gate

↓

MemoryService

↓

MemoryRepository

↓

MemoryRecord