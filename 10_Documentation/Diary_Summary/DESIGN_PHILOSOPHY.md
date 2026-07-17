# DESIGN PHILOSOPHY

## Triết lý

Diary là dữ liệu gốc.

Diary Summary là tri thức đã được chuẩn hóa.

MemoryAI học từ Summary.

Assistant chỉ truy xuất từ MemoryAI.

---

## Nguyên tắc

- Không sửa nhật ký gốc.
- Summary luôn có Metadata.
- Summary phải ngắn gọn.
- Summary phải có Version.
- Summary phải có khả năng tái tạo.

---

## Quy trình

Diary

↓

Diary Processor

↓

Diary Summary

↓

Memory Loader

↓

Memory Context

↓

Memory Search

↓

Assistant

---

## Mục tiêu

Giảm thời gian AI phải đọc toàn bộ nhật ký.

Tăng tốc truy xuất tri thức.

Chuẩn hóa dữ liệu trước khi AI học.