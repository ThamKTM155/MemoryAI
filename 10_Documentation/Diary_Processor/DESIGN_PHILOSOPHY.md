# DESIGN PHILOSOPHY

Diary Processor được xây dựng theo nguyên tắc đơn nhiệm (Single Responsibility).

Module chỉ chịu trách nhiệm đọc nhật ký.

Không xử lý trí nhớ.

Không cập nhật dữ liệu.

Không đưa ra quyết định.

---

## Triết lý thiết kế

Nhật ký là nguồn dữ liệu gốc (Single Source of Truth).

Mọi thay đổi của hệ thống đều bắt đầu từ nhật ký.

MemoryAI chỉ lưu trữ và truy xuất.

ThamAI chỉ sử dụng dữ liệu từ MemoryAI.

---

## Kiến trúc

Người dùng

↓

Nhật ký

↓

Diary Processor

↓

Diary Parser

↓

MemoryAI

↓

ThamAI

---

## Nguyên tắc

- Không phá Production
- Test sau mỗi thay đổi
- Mỗi module chỉ làm một việc
- Có thể mở rộng
- Có thể bảo trì
- Có thể thay thế từng module độc lập

---

## Mục tiêu cuối cùng

Xây dựng trợ lý AI đồng hành có khả năng:

- ghi nhớ lịch sử làm việc
- ghi nhớ quyết định
- hỗ trợ dự án
- hỗ trợ gia đình
- lưu giữ tri thức lâu dài

cho nhiều năm sau.