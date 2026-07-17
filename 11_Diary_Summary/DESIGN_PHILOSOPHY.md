# DESIGN PHILOSOPHY

## Triết lý

Diary là dữ liệu gốc.

Diary Summary là tri thức.

MemoryAI học từ Summary.

Assistant đọc từ MemoryAI.

## Nguyên tắc

Không sửa nhật ký gốc.

Summary phải ngắn gọn.

Summary phải có Metadata.

Summary phải có Version.

Summary có thể xây dựng lại từ nhật ký.

## Pipeline

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

Assistant