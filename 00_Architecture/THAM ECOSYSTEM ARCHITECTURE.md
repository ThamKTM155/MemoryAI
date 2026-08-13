THAM ECOSYSTEM ARCHITECTURE
Điều lệ số 01 – Kho Tri Thức Dùng Chung (Unified Knowledge Repository)

Ngày thông qua: 05/08/2026

Mục đích

Xây dựng một kho tri thức thống nhất cho toàn bộ hệ sinh thái ThamAI.

Mọi dữ liệu, tri thức, kinh nghiệm, nhật ký, quy trình, quyết định và quan hệ đều được quản lý tập trung, tránh tình trạng phân tán dữ liệu và phát triển thành các "ốc đảo tri thức".

Điều 1. Một cổng chính

Mọi thành phần của hệ sinh thái phải truy cập tri thức thông qua Knowledge Gate.

Không được phép truy cập trực tiếp vào các nguồn dữ liệu khi hệ thống đang hoạt động bình thường.

Điều 2. Một nguồn chân lý

Mỗi tri thức chỉ có một nguồn chính thức (Single Source of Truth).

Các tài liệu khác chỉ là:

liên kết
chỉ mục
bản tóm tắt
bản sao phục vụ sao lưu

Không được tạo nhiều bản dữ liệu độc lập có nội dung mâu thuẫn nhau.

Điều 3. Không tồn tại "ốc đảo dữ liệu"

Không một module nào được phép tự quản lý tri thức riêng.

Bao gồm:

MemoryAI
ThamAI
AutoYouTube
Dashboard
VoiceAI
các BUILD tương lai

Tất cả đều phải sử dụng chung Kho Tri Thức.

Điều 4. Memory Graph là trung tâm liên kết

Memory Graph chịu trách nhiệm:

quản lý Node
quản lý Relationship
quản lý Metadata
quản lý Chỉ mục
xác định vị trí lưu trữ dữ liệu

Memory Graph không thay thế tài liệu gốc mà đóng vai trò bản đồ của toàn bộ tri thức.

Điều 5. Cổng phụ

Các đường truy cập trực tiếp chỉ được sử dụng trong các trường hợp:

Recovery
Backup
Migration
Debug
Khẩn cấp khi cổng chính không hoạt động

Sau khi hoàn thành phải quay trở lại sử dụng cổng chính.

Điều 6. Nguyên tắc phát triển

Mọi BUILD mới phải trả lời được các câu hỏi:

Có đi qua Knowledge Gate không?
Có sử dụng Kho Tri Thức Dùng Chung không?
Có tạo dữ liệu trùng lặp không?
Có phá vỡ Single Source of Truth không?
Có giữ được khả năng mở rộng trong tương lai không?

Nếu bất kỳ câu trả lời nào là Không, BUILD chưa được phép đưa vào Production.

Điều 7. Kỷ luật kiến trúc

Đây là điều lệ bắt buộc.

Mọi thành viên tham gia phát triển hệ sinh thái, bao gồm cả AI và con người, đều phải tuân thủ.

Việc tự ý tạo đường truy cập riêng, tự ý xây dựng kho dữ liệu riêng hoặc bỏ qua Knowledge Gate được xem là vi phạm kiến trúc hệ thống và phải được sửa trước khi tiếp tục phát triển.

Quyết định

Kể từ BUILD-57:

Kho Tri Thức Dùng Chung (Unified Knowledge Repository) trở thành nền tảng chính thức của toàn bộ hệ sinh thái ThamAI.

Mọi thiết kế, mọi BUILD và mọi quyết định kỹ thuật sau này đều phải tuân thủ điều lệ này.

Từ hôm nay, nếu đề xuất một giải pháp mà:

tạo thêm một "ốc đảo dữ liệu",
bỏ qua Knowledge Gate,
hoặc làm xuất hiện nhiều nguồn chân lý,

thì đó là vi phạm Hiến pháp kiến trúc và phải bị bác bỏ, không được tiếp tục triển khai. Đây sẽ là nguyên tắc tuân thủ trong các phiên làm việc tiếp theo.