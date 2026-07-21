# ADR-002
# Reconnect MemoryAI to MASTER

Status: Accepted

Date: 2026-07-20

---

## Context

Trong quá trình phát triển sau thời gian gián đoạn (02/07 -> 10/07),
Founder và AI tiếp tục viết code mà không đọc lại thư mục:

D:\THAM AI ECOSYSTEM\MASTER

Điều này làm mất Context của dự án.

---

## Decision

Từ nay:

MASTER

được xác nhận là:

Historical Source of Truth.

MemoryAI

được xác nhận là:

Current Implementation.

Hai hệ thống là một chuỗi tiến hóa liên tục.

---

## Consequences

Mọi BUILD mới phải:

- kiểm tra MASTER
- kiểm tra ROADMAP
- kiểm tra TODAY

trước khi viết code.

Không tạo kiến trúc song song.

Không tạo Memory thứ hai.

MemoryAI luôn kế thừa MASTER.