SYSTEM FREEZE – KNOWLEDGE STANDARD V1

Ngày khởi tạo: 29/07/2026

Mục tiêu số 1 (Ưu tiên tuyệt đối)

Khôi phục khả năng upload ổn định cho cả 4 kênh YouTube trước khi tối ưu hay thay đổi mã nguồn.

Trong giai đoạn này:

❌ Không refactor lớn.
❌ Không thêm tính năng mới nếu không cần thiết.
✅ Chỉ xử lý OAuth, Token và Mapping.
✅ Đưa hệ thống trở lại trạng thái production.
Quy ước 01 – Một nguồn sự thật (Single Source of Truth)

Mọi quyết định quan trọng sẽ được lưu ở Knowledge Base.

Cấu trúc đề xuất:

KnowledgeBase/
│
├── 00_Project_Rules.md
├── 01_OAuth_Standard.md
├── 02_Channel_Registry.md
├── 03_System_Architecture.md
├── 04_Debug_History.md
├── 05_System_Freeze.md
└── CHANGELOG.md

Đây là tài liệu gốc của dự án.

Quy ước 02 – Một Folder = Một Kênh

Ví dụ:

channels/kenh2

luôn phải tương ứng với:

đúng Gmail
đúng Channel ID
đúng token
đúng client_secret

Không được phép dùng lẫn.

Quy ước 03 – Mỗi Token phải được xác minh

Sau khi chạy:

python get_token.py

bắt buộc phải kiểm tra:

✅ Channel Name
✅ Channel ID
✅ Đúng thư mục

Nếu sai:

→ Xóa token và tạo lại.

Quy ước 04 – ChatGPT là Trung tâm chỉ huy

Anh chỉ cần duy trì một phiên ChatGPT chính để làm việc.

Còn Gmail, Chrome Profile hay OAuth chỉ là công cụ vận hành, không phải nơi lưu tri thức.

Quy ước 05 – MemoryAI ghi nhớ quyết định

MemoryAI không chỉ lưu nhật ký.

MemoryAI sẽ lưu:

Quy ước
Kiến trúc
Mapping
Quy trình
Freeze
Các quyết định quan trọng
Quy ước 06 – Freeze sau mỗi mốc lớn

Ví dụ:

SYSTEM_FREEZE/

2026-07-29/

README.md

CHANNEL_REGISTRY.json

OAUTH_STANDARD.md

CHANGELOG.md

Đó sẽ là "điểm khôi phục" của hệ thống.

Lộ trình ngay sau hôm nay
Giai đoạn A (đang thực hiện)

🎯 Mục tiêu:

Khôi phục OAuth.

Checklist:

⏳ Kenh1
✅ Kenh2
⏳ Kenh3 (đúng Gmail)
⏳ Kenh4
Giai đoạn B

Sau khi đủ 4 token:

Test upload.
Test pipeline.
Freeze OAuth.
Giai đoạn C

Mới bắt đầu:

tối ưu code,
nâng cấp AI,
cải thiện hệ thống.
Cam kết của em

Từ bây giờ, mỗi khi anh nói:

"Tiếp tục hệ sinh thái AI"

hoặc

"Làm tiếp AutoYouTube"

em sẽ ưu tiên làm theo Knowledge Standard V1 này:

Dựa trên các quy ước đã chốt.
Không tự ý thay đổi kiến trúc đã đóng băng nếu chưa thống nhất.
Luôn ưu tiên tính ổn định của hệ thống trước khi thêm tính năng.
Mọi quyết định lớn sẽ được đề xuất để đưa vào Knowledge Base thay vì chỉ tồn tại trong một phiên chat.

Em nghĩ đây sẽ là nền tảng rất tốt để AutoYouTube, MemoryAI và các dự án khác phát triển lâu dài mà không bị phụ thuộc vào việc đổi máy, đổi Gmail hay mất một phiên trò chuyện.

So sánh với Claude Opus 4.8