# SYSTEM CONSTITUTION

Version: V1

Date: 2026-08-05

============================================

THAM ECOSYSTEM

SYSTEM CONSTITUTION

============================================

## Điều 01

Mỗi chức năng chỉ có một nơi chịu trách nhiệm.

Không được tồn tại hai module cùng đảm nhiệm một chức năng.

---

## Điều 02

Toàn bộ hệ sinh thái chỉ có một Cổng chính.

Tên:

Knowledge Gate

Mọi truy vấn đều phải đi qua cổng này.

---

## Điều 03

Knowledge Gate là Dispatcher duy nhất.

Knowledge Gate có quyền điều phối:

- Identity
- Repository
- Memory Graph
- AI

Không module nào khác được phép điều phối thay.

---

## Điều 04

Repository là Kho tri thức dùng chung.

Mọi module muốn đọc tri thức đều phải thông qua Knowledge Gate.

Không truy cập trực tiếp.

Người chủ không giao việc trực tiếp cho bất kỳ đơn vị chuyên môn nào. Mọi yêu cầu đều phải đi qua Operations Center. Operations Center là đầu mối duy nhất được quyền điều phối, phân công, tổng hợp và báo cáo.

---

## Điều 05

Memory Graph chỉ chịu trách nhiệm:

- Quan hệ
- Suy luận
- Liên kết

Không làm nhiệm vụ lưu trữ.

Mỗi Intent chỉ được giao cho đúng đơn vị chuyên môn. Nếu một Intent được điều phối sai phòng ban, phải sửa logic điều phối tại Chief Operations Officer, không vá lỗi ở các đơn vị thực thi.
---

## Điều 06

Backend chỉ là Application Layer.

Backend không quyết định.

Backend không suy luận.

Backend chỉ tiếp nhận yêu cầu và chuyển cho Knowledge Gate.

---

## Điều 07

Frontend chỉ là Presentation Layer.

Frontend chỉ gọi API.

Frontend không biết:

- Repository
- Memory Graph
- AI
- Identity

---

## Điều 08

AI luôn là lựa chọn cuối cùng.

Thứ tự xử lý:

Identity

↓

Repository

↓

Memory Graph

↓

AI

---

## Điều 09

Mọi project trong hệ sinh thái đều phải được đăng ký trong:

SYSTEM_ASSET_REGISTER.md

Không tồn tại project ngoài danh mục quản lý.

---

## Điều 10

Không phá hệ thống để xây lại.

Mọi phát triển đều theo hình xoắn ốc.

Mỗi BUILD:

- Có mục tiêu.
- Có phạm vi.
- Có kiểm thử.
- Có nhật ký.
- Có khả năng quay lui.
---

## Điều 11

Ưu tiên hợp nhất trước khi tạo mới.

Trước khi tạo:

- Project mới
- Module mới
- Service mới
- Repository mới

phải trả lời được ba câu hỏi:

1. Có thể mở rộng hệ thống hiện tại không?

2. Có thể hợp nhất với module đang có không?

3. Có thật sự cần tạo mới không?

Nếu câu trả lời là "Có thể mở rộng" hoặc "Có thể hợp nhất"

→ Không được tạo mới.
============================================

Mục tiêu cuối cùng

Một Frontend.

Một Backend.

Một Knowledge Gate.

Một Repository.

Một Memory Graph.

Một hệ sinh thái thống nhất.
==========================================
