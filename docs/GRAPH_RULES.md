# GRAPH_RULES.md

# THAM ECOSYSTEM
## Memory Graph Rules V1.0

Updated:
2026-08-02

Status:
BUILD-41A

---

# MỤC ĐÍCH

Định nghĩa các quy tắc nghiệp vụ (Business Rules) của Memory Graph.

Graph Builder và Graph Query phải tuân thủ các quy tắc này.

Không được tự ý tạo quan hệ trái với tài liệu này.

---

# PROJECT RULES

Một PROJECT có thể chứa nhiều BUILD.

Một BUILD chỉ thuộc một PROJECT.

Một PROJECT có thể có nhiều DOCUMENT.

Một PROJECT có thể có nhiều FILE.

---

# BUILD RULES

Mỗi BUILD phải có ID duy nhất.

Một BUILD phải thuộc đúng một PROJECT.

Một BUILD có thể cập nhật nhiều FILE.

Một BUILD có thể tạo nhiều FILE.

Một BUILD phải có ít nhất một DOCUMENT mô tả.

Một BUILD có thể liên quan nhiều SUMMARY.

Một BUILD có thể được triển khai nhiều lần.

---

# FILE RULES

Một FILE có thể được nhiều BUILD cập nhật.

Một FILE chỉ tồn tại một bản ghi trong Graph.

Một FILE có thể được nhiều DOCUMENT tham chiếu.

---

# DOCUMENT RULES

Một DOCUMENT có thể tham chiếu nhiều BUILD.

Một DOCUMENT có thể thuộc nhiều PROJECT nếu là tài liệu dùng chung.

README, ADR, CHANGELOG, DESIGN đều là DOCUMENT.

---

# DIARY RULES

Một DIARY có thể sinh nhiều SUMMARY.

Một SUMMARY chỉ được tạo từ một DIARY.

---

# COMMIT RULES

Một COMMIT có thể triển khai nhiều BUILD.

Một BUILD có thể có nhiều COMMIT trong quá trình phát triển.

---

# DEPLOYMENT RULES

Một DEPLOYMENT có thể triển khai nhiều COMMIT.

Một COMMIT có thể được triển khai nhiều môi trường.

Ví dụ:

Development

Testing

Production

---

# GRAPH RULES

Không tạo Node trùng.

Không tạo Edge trùng.

Không lưu cùng một tri thức ở nhiều nơi.

Mọi quan hệ đều phải đi qua Edge.

Node không chứa Node khác.

---

# MEMORY RULES

Memory Graph là nguồn tri thức chung của toàn hệ sinh thái.

Không module nào được tạo kho dữ liệu riêng nếu thông tin đã tồn tại trong Memory Graph.

Khi có xung đột dữ liệu, ưu tiên dữ liệu mới hơn nhưng vẫn lưu lịch sử thay đổi.

---

# FUTURE RULES

Mọi BUILD mới phải xác định:

Node mới.

Edge mới.

Nguồn dữ liệu.

Ảnh hưởng đến Graph.

Chỉ sau khi hoàn thành các bước trên mới được triển khai vào Production.
---

# RELATED DOCUMENTS

- GRAPH_SCHEMA
- GRAPH_DATA_MODEL
- GRAPH_CHANGELOG
- GRAPH_SOURCE_MAP