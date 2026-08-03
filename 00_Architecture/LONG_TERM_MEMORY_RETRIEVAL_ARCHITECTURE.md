LONG_TERM_MEMORY_RETRIEVAL_ARCHITECTURE.md

Version: 1.0

Status: BUILD-38 Draft

Author: MemoryAI Ecosystem

LONG-TERM MEMORY RETRIEVAL ARCHITECTURE
1. Mục đích

Tài liệu này mô tả kiến trúc truy vấn của Long-Term Memory trong hệ sinh thái MemoryAI.

Mục tiêu của kiến trúc là giúp mọi thành phần trong hệ sinh thái có thể truy cập tri thức đã được lưu trữ mà không cần truy cập trực tiếp vào dữ liệu gốc.

Kiến trúc ưu tiên:

kế thừa;
ổn định;
khả năng mở rộng;
không phá vỡ các thành phần đang hoạt động.
2. Triết lý thiết kế

Long-Term Memory không chỉ là nơi lưu dữ liệu.

Long-Term Memory là trung tâm tri thức của toàn bộ hệ sinh thái.

Mọi thành phần đều sử dụng chung một hệ thống truy vấn.

Không tạo nhiều bộ nhớ.

Không tạo nhiều Search Engine.

Không tạo nhiều API.

Chỉ có một nguồn tri thức thống nhất.

3. Kiến trúc hiện tại
                User
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
 tools/memory_api.py   tools/memory_server.py
        │                   │
        └─────────┬─────────┘
                  │
                  ▼
        tools/memory_answer.py
                  │
                  ▼
        tools/memory_search.py
                  │
                  ▼
 tools/summary_index_search.py
                  │
                  ▼
        summary_index.json
                  │
                  ▼
        Diary Summary
                  │
                  ▼
        memory_context.txt
4. Vai trò của từng thành phần
tools/memory_api.py

Giao diện truy vấn dòng lệnh (CLI).

Cho phép người dùng đặt câu hỏi trực tiếp với MemoryAI.

Không xử lý dữ liệu.

Chỉ chuyển câu hỏi đến Memory Engine.

tools/memory_server.py

REST API của MemoryAI.

Cung cấp khả năng truy vấn thông qua HTTP.

Đây là điểm kết nối chính để các hệ thống khác như ThamAI hoặc ProjectOS sử dụng Long-Term Memory.

tools/memory_answer.py

Đây là trung tâm của Long-Term Memory Retrieval.

Nhiệm vụ:

nhận câu hỏi;
gọi Search Engine;
đánh giá kết quả;
lựa chọn đoạn thông tin phù hợp nhất;
trả lời người dùng.

Trong BUILD tiếp theo, module này sẽ tiếp tục được mở rộng để tích hợp khả năng Reasoning mà không thay đổi các thành phần phía dưới.

tools/memory_search.py

Search Engine của MemoryAI.

Nhiệm vụ:

truy vấn Summary Index;
truy vấn Memory Context;
chấm điểm kết quả;
trả về các đoạn thông tin liên quan.

Module này đã hoạt động ổn định và được giữ nguyên.

tools/summary_index_search.py

Index Engine.

Nhiệm vụ:

đọc summary_index.json;
tìm theo ngày;
tìm theo Project;
tìm theo Keyword.

Đây là lớp Index đầu tiên của hệ thống.

summary_index.json

Cơ sở dữ liệu chỉ mục.

Lưu các thông tin:

ngày;
project;
keyword.

Giúp tăng tốc truy vấn.

Diary Summary

Lưu tóm tắt từng ngày phát triển.

Là nguồn tri thức chính của Search Engine.

memory_context.txt

Lớp dữ liệu dự phòng (Fallback).

Được sử dụng khi Summary không tìm thấy kết quả phù hợp.

5. Luồng truy vấn
Người dùng

↓

CLI hoặc REST API

↓

Memory Answer

↓

Memory Search

↓

Summary Index

↓

Diary Summary

↓

Memory Context (Fallback)

↓

Memory Answer

↓

Người dùng
6. Nguyên tắc phát triển

Long-Term Memory Retrieval đã hoạt động ổn định.

Trong các BUILD tiếp theo:

không viết lại Search Engine;
không viết lại Summary Index;
không thay đổi cấu trúc dữ liệu;
không tạo Search Engine mới.

Mọi nâng cấp sẽ được thực hiện tại tầng memory_answer.py hoặc bằng cách kết nối thêm các thành phần mới ở phía trên.

7. Hướng phát triển

Giai đoạn tiếp theo không tập trung xây dựng lại Long-Term Memory.

Mục tiêu là kết nối các thành phần của hệ sinh thái với hệ thống truy vấn hiện có.

Thứ tự kết nối:

ProjectOS
        │
        ▼
MemoryAI
        │
        ▼
ThamAI
        │
        ▼
AutoYouTube

Trong kiến trúc này:

MemoryAI giữ vai trò trí nhớ dài hạn.
ThamAI giữ vai trò bộ não phân tích và ra quyết định.
AutoYouTube giữ vai trò hệ thống sản xuất.
ProjectOS giữ vai trò quản lý toàn bộ quá trình phát triển.
8. Kết luận

Long-Term Memory Retrieval là nền tảng của toàn bộ hệ sinh thái AI.

Kiến trúc hiện tại đã đáp ứng đầy đủ các chức năng:

truy vấn;
lập chỉ mục;
tìm kiếm;
lựa chọn kết quả;
cung cấp API.

Các BUILD tiếp theo sẽ tập trung vào kết nối và mở rộng, không thay thế hay viết lại các thành phần đang hoạt động ổn định.

"Mọi BUILD mới phải kế thừa Long-Term Memory Retrieval hiện có; mọi cải tiến phải được thực hiện bằng cách mở rộng hoặc kết nối, không bằng cách thay thế những thành phần đã được kiểm chứng trong thực tế."