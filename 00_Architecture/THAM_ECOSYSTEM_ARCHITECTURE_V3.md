# THAM ECOSYSTEM ARCHITECTURE V3

Ngày: 2026-08-05

=========================================
                USER
=========================================

                  │
                  ▼

          ThamAI Frontend
       (Presentation Layer)

                  │
                  ▼

          ThamAI Backend
       (Application Layer)

                  │
                  ▼

           Knowledge Gate
         (Unified Gateway)

     ┌──────────┼──────────┬──────────┐
     ▼          ▼          ▼          ▼

 Identity   Repository  MemoryGraph   AI

                │
                ▼

       Shared Knowledge Base

=========================================
## Vai trò từng tầng

### 1. Frontend

- Giao diện người dùng.
- Hiển thị kết quả.
- Không chứa tri thức.

---

### 2. Backend

- Tiếp nhận API.
- Xử lý phiên làm việc.
- Chuyển yêu cầu đến Knowledge Gate.

---

### 3. Knowledge Gate

Cổng truy cập duy nhất.

Chịu trách nhiệm điều phối:

- Identity
- Repository
- Memory Graph
- AI

---

### 4. Repository

Kho lưu trữ tri thức dùng chung.

Ưu tiên trả lời từ đây.

---

### 5. Memory Graph

Phân tích quan hệ.

Suy luận.

Kết nối dữ liệu.

---

### 6. AI

Chỉ sử dụng khi các tầng trước không trả lời được.
=======================================
## Luồng xử lý chuẩn

User

↓

Frontend

↓

Backend

↓

Knowledge Gate

↓

Identity ?

↓

Repository ?

↓

Memory Graph ?

↓

AI ?

↓

Trả kết quả
===============================
## Quy tắc

Knowledge Gate là cổng chính.

Không module nào được phép truy cập trực tiếp:

- Repository
- Memory Graph
- AI

nếu chưa đi qua Knowledge Gate.