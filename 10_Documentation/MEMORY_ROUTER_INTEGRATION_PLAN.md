# MEMORY_ROUTER_INTEGRATION_PLAN

Version: BUILD-38

Status: Planning

---

# 1. Mục tiêu

Khôi phục Memory Router vào ThamAI Production.

Không xây mới.

Không thay thế.

Không phá Production.

Chỉ kết nối MemoryAI với ThamAI.

---

# 2. Kiến trúc hiện tại

Frontend

↓

ThamAI Backend

↓

OpenRouter

↓

Trả lời

Trong kiến trúc hiện tại, ThamAI chưa sử dụng Long-Term Memory.

---

# 3. Kiến trúc mục tiêu

Frontend

↓

ThamAI Backend

↓

Memory Router

↓

MemoryAI

↓

Nếu Memory biết

↓

Trả lời ngay

Nếu Memory chưa biết

↓

OpenRouter

↓

Trả lời

---

# 4. Thành phần sẽ tích hợp

Không thay đổi:

- app.py
- OpenRouter
- Frontend
- Logger
- Health API

Bổ sung:

- MEMORY_URL
- Memory Query
- Memory Context
- Memory First Logic
- /memory_test

---

# 5. Thành phần giữ nguyên

MemoryAI:

- memory_api.py
- memory_server.py
- memory_answer.py
- memory_search.py
- summary_index_search.py

Không sửa trong BUILD-38.

---

# 6. Quy trình tích hợp

Bước 1

Thêm MEMORY_URL.

Bước 2

Thêm Memory Query.

Bước 3

Thêm Memory First Logic.

Bước 4

Giữ OpenRouter làm Fallback.

Bước 5

Kiểm thử.

---

# 7. Nguyên tắc

Production luôn là trung tâm.

Backup chỉ dùng làm tài liệu tham khảo.

Không copy toàn bộ app_memory_router_v1.py.

Chỉ tích hợp các thành phần đã được kiểm chứng.

---

# 8. Kết quả mong muốn

MemoryAI trở thành trí nhớ dài hạn.

ThamAI trở thành bộ não.

AutoYouTube trở thành hệ thống sản xuất.

Ba thành phần kết nối thành một hệ sinh thái thống nhất.

---

# Kết luận

BUILD-38 không tạo ra một hệ thống mới.

BUILD-38 khôi phục cây cầu giữa MemoryAI và ThamAI.

Đây là bước đầu tiên để hình thành vòng học tập:

Experience

↓

MemoryAI

↓

Knowledge

↓

ThamAI

↓

AutoYouTube

↓

Experience