# SYSTEM CONSTITUTION

Version: 1.0

Status: ACTIVE

=========================================
ĐIỀU 1
MỤC ĐÍCH
=========================================

System Constitution là tài liệu có hiệu lực cao nhất của MemoryAI.

Mọi thiết kế, BUILD, module và trợ lý AI đều phải tuân thủ tài liệu này.

=========================================
ĐIỀU 2
KIẾN TRÚC
=========================================

MemoryAI được tổ chức theo các tầng sau:

Presentation Layer

↓

Application Layer

↓

Knowledge Gate

↓

Core Domain

↓

Infrastructure Layer

Không được bỏ qua tầng.

=========================================
ĐIỀU 3
KNOWLEDGE GATE
=========================================

Knowledge Gate là cổng chính của toàn bộ hệ sinh thái.

Mọi truy vấn từ bên ngoài đều phải đi qua Knowledge Gate.

Không module nào được phép tự ý truy cập trực tiếp vào các tầng phía dưới.

=========================================
ĐIỀU 4
MEMORY SERVICE
=========================================

MemoryService là cổng chính của Core Domain.

Mọi thao tác với trí nhớ đều phải đi qua MemoryService.

Không module nào được truy cập Repository trực tiếp.

Người chủ không giao việc trực tiếp cho bất kỳ đơn vị chuyên môn nào. Mọi yêu cầu đều phải đi qua Operations Center. Operations Center là đầu mối duy nhất được quyền điều phối, phân công, tổng hợp và báo cáo.

=========================================
ĐIỀU 5
MEMORY RECORD
=========================================

MemoryRecord là mô hình dữ liệu chuẩn.

Mọi dữ liệu trí nhớ đều phải quy về MemoryRecord hoặc mô hình kế thừa từ MemoryRecord.

Mỗi Intent chỉ được giao cho đúng đơn vị chuyên môn. Nếu một Intent được điều phối sai phòng ban, phải sửa logic điều phối tại Chief Operations Officer, không vá lỗi ở các đơn vị thực thi.

=========================================
# Điều 6 - Thống nhất trong đa dạng
========================================
MemoryAI được xây dựng theo nguyên tắc:

> Thống nhất trong đa dạng.
> Một người biết nhiều việc, nhưng chỉ giỏi một việc.

## 1. Thống nhất

Toàn bộ hệ thống sử dụng:

- Một kiến trúc chung.
- Một mô hình dữ liệu chung.
- Một hệ thống quản trị chung.
- Một bộ quy chế chung.

Không tạo nhiều hệ thống độc lập khi có thể mở rộng trên nền tảng thống nhất.

## 2. Đa dạng

Mỗi đơn vị có chuyên môn riêng.

Ví dụ:

- Knowledge Center chuyên về tri thức.
- Planner Center chuyên về kế hoạch và điều hành.
- Memory Center chuyên về trí nhớ.
- AI Center chuyên về suy luận.
- Action Center chuyên về thực thi.

Các đơn vị có thể hiểu lĩnh vực của nhau để phối hợp, nhưng chỉ chịu trách nhiệm chuyên sâu đối với lĩnh vực của mình.

## 3. Một mô hình dữ liệu

MemoryAI ưu tiên sử dụng một mô hình dữ liệu thống nhất.

Ví dụ:

MemoryRecord

được sử dụng để lưu nhiều loại thông tin khác nhau thông qua phân loại bằng `memory_type`, thay vì tạo nhiều kiểu bản ghi riêng biệt khi chưa thực sự cần thiết.

## 4. Phân công chuyên môn

Mỗi yêu cầu phải được điều phối đến đúng đơn vị chuyên môn.

Chief Operations Officer không trực tiếp thực hiện nghiệp vụ chuyên môn mà chỉ:

- tiếp nhận yêu cầu;
- điều phối đúng đơn vị;
- theo dõi tiến độ;
- tổng hợp kết quả;
- báo cáo Giám đốc.

## 5. Mở rộng

Khi phát triển hệ thống:

- ưu tiên mở rộng bằng chuyên môn hóa;
- hạn chế tạo mô hình dữ liệu mới;
- hạn chế tạo đơn vị có chức năng trùng lặp;
- giữ kiến trúc thống nhất và ổn định lâu dài.
=========================================
ĐIỀU 7
PRODUCTION
=========================================

Production luôn được ưu tiên hơn tính năng mới.

Không đánh đổi sự ổn định để lấy sự phức tạp.

=========================================
ĐIỀU 8
TÀI LIỆU GỐC
=========================================

Bốn tài liệu sau là nền tảng của MemoryAI:

- SYSTEM_CONSTITUTION.md
- MEMORYAI_MISSION.md
- MEMORYAI_VALUES.md
- MEMORYAI_PRINCIPLES.md
- OWNER_VISION.md

Nếu code mâu thuẫn với các tài liệu này thì phải sửa code, không sửa tài liệu.

MemoryAI không tự đào tạo khi bên ngoài đã có đơn vị làm tốt hơn.

Ưu tiên học hỏi từ các hệ thống tiên tiến.

Sau khi tiếp thu phải:

- áp dụng vào công việc thực tế;
- đánh giá bằng hiệu quả thực tế;
- giữ lại những gì mang lại giá trị;
- loại bỏ những gì không phù hợp.

Không giữ một phương pháp chỉ vì đã từng sử dụng.
=========================================