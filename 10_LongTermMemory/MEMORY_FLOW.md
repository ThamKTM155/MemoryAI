# MEMORY FLOW

**Document ID:** LTM-002

**Version:** Draft 1.0

**Status:** Draft

---

# 1. Mục đích

Mô tả luồng hình thành, lưu trữ, truy xuất và cập nhật trí nhớ dài hạn của MemoryAI.

---

# 2. Luồng hình thành trí nhớ

Nguồn dữ liệu

↓

Memory Builder

↓

Validation Engine

↓

Knowledge Memory

↓

Timeline Memory

↓

Decision Memory

↓

Experience Memory

↓

Cross Project Memory

↓

Project Router

↓

AI Assistant

---

# 3. Luồng truy xuất

Người dùng đặt câu hỏi

↓

Project Router

↓

Knowledge Memory

↓

Timeline Memory

↓

Decision Memory

↓

Experience Memory

↓

Tổng hợp ngữ cảnh

↓

AI trả lời

---

# 4. Nguyên tắc

- Không sử dụng dữ liệu chưa được Validation.
- Mọi câu trả lời phải có nguồn tham chiếu.
- Ưu tiên dữ liệu mới nhất nếu có xung đột.
- Luôn giữ khả năng truy vết ngược về dữ liệu gốc.

---

# 5. Trạng thái

Draft