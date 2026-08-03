# KNOWLEDGE_STANDARD_V1.md

# SYSTEM FREEZE -- KNOWLEDGE STANDARD V1

Ngày khởi tạo: 29/07/2026

## Mục tiêu ưu tiên

Khôi phục khả năng upload ổn định cho 4 kênh YouTube trước khi tối ưu hệ
thống.

------------------------------------------------------------------------

# Quy ước làm việc

## 1. ChatGPT = Trung tâm chỉ huy

-   Duy trì một phiên ChatGPT chính.
-   Mọi quyết định kỹ thuật được thống nhất tại đây.

## 2. MemoryAI = Bộ nhớ dài hạn

-   Ghi lại các quyết định đã được chốt.
-   Không chỉ lưu nhật ký mà lưu cả quy ước và kiến trúc.

## 3. KnowledgeBase = Nguồn sự thật

Thư mục đề xuất:

KnowledgeBase/ ├── 00_Project_Rules.md ├── 01_OAuth_Standard.md ├──
02_Channel_Registry.md ├── 03_System_Architecture.md ├──
04_Debug_History.md ├── 05_System_Freeze.md └── CHANGELOG.md

------------------------------------------------------------------------

# Quy ước OAuth

-   Một Folder = Một Kênh YouTube.
-   Một token chỉ thuộc một Channel ID.
-   Sau khi tạo token phải xác minh:
    -   Channel Name
    -   Channel ID
    -   Đúng thư mục.
-   Nếu sai phải xóa token và tạo lại.
-   Không sửa code khi OAuth chưa ổn định.

------------------------------------------------------------------------

# Kế hoạch ưu tiên

Giai đoạn A: - Khôi phục token cho 4 kênh. - Kiểm tra bằng
check_all_channels.py. - Upload thử. - Freeze OAuth.

Giai đoạn B: - Chuẩn hóa Channel Registry. - Tự động kiểm tra token
trước khi upload.

Giai đoạn C: - Tối ưu AutoYouTube và MemoryAI.

------------------------------------------------------------------------

# Cam kết

Mọi thay đổi lớn của dự án sẽ được cập nhật vào KnowledgeBase trước khi
triển khai. KnowledgeBase là tài liệu gốc để MemoryAI học và sử dụng lâu
dài.
