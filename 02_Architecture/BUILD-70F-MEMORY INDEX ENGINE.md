1. Index để làm gì?

Tìm memory nhanh hơn

Không cần quét toàn bộ memory_records.json

Hỗ trợ Query Engine

Hỗ trợ Knowledge Builder

Hỗ trợ Long-Term Memory

2. Index những gì?

Giai đoạn V1 nên rất đơn giản:

title_index
source_index
memory_type_index
classification_index

Ví dụ:

{
  "SYSTEM_CONSTITUTION": [54],
  "MEMORYAI_MISSION": [55]
}
3. Lưu ở đâu?

Đề xuất:

D:\MemoryAI\data\indexes\

Bên trong:

title_index.json
source_index.json
type_index.json
classification_index.json
4. Ai được tạo Index?

Theo BUILD-70C:

MemoryRepository
        ↓
Memory Classification Engine
        ↓
Memory Index Engine

Index Engine không tự đọc Diary.

Không tự đọc WinnerAI.

Không tự đọc 00_Core.

Nó chỉ nhận MemoryRecord đã được ghi vào kho chung.

Điều này phù hợp với Hiến pháp:

Mọi đơn vị dùng chung kho trí nhớ.

Không giữ trí nhớ riêng.
Bước 2: Viết V1 thật nhỏ

Sau khi lưu tài liệu xong mới viết:

D:\MemoryAI\service\memory_index_engine.py

Chỉ cần 1 hàm đầu tiên:

build_title_index()

Đọc:

MemoryRepository.load_all()

và sinh:

title_index.json

là đủ.

Nếu đi đúng roadmap hiện tại thì chưa nên nhảy sang Graph, Relationship hay AI.

Chuỗi hợp lý là:

70E  Classification  ✅

70F  Index Engine    ← đang làm

70G  Relationship Engine

70H  Long-Term Memory Graph

Xuất phát từ BUILD-70F trước, xây nhỏ, test nhỏ, rồi mới mở rộng.

So sánh với Claude Opus 4.8