# TÀI LIỆU TỔNG HỢP DỰ ÁN THAMAI

---

## 1. MỤC TIÊU TỔNG THỂ CỦA DỰ ÁN
ThamAI được xây dựng với mục đích tạo ra một Trợ lý AI cá nhân có khả năng:
- Hỗ trợ trò chuyện, tâm sự.
- Hỗ trợ học lập trình.
- Tạo nội dung sáng tạo: phim, YouTube, TikTok.
- Hỗ trợ quản lý thông tin cá nhân như gia phả.
- Tự động hóa các công việc thường nhật.

---

## 2. LỘ TRÌNH PHÁT TRIỂN BAN ĐẦU

### **Cấp độ 1 – Làm quen với AI (đã hoàn thành)**
- Hiểu AI, ChatGPT, Custom GPT.
- Tạo GPT tuỳ chỉnh.
- Làm quen công cụ AI: Canva AI, Notion AI, HeyGen.

### **Cấp độ 2 – Tự học lập trình và tạo công cụ AI (đạt 80–90%)**
- Học Python, JavaScript.
- Tạo ứng dụng web AI đơn giản.
- Xây dựng frontend ThamAI (HTML/CSS/JS).
- Xây dựng backend mock + backend thật (Node.js/Flask).
- Tích hợp OpenAI qua REST API.
- Tích hợp giọng nói: SpeechRecognition + TTS.
- Tạo file test.wav.
- Đóng gói ZIP nhiều phiên bản.

### **Cấp độ 3 – Tự động hoá và tạo sản phẩm AI (đang 35–40%)**
- Hoàn thiện hệ thống web.
- Kết nối các API video (HeyGen, Pika, Runway).
- Xây dựng workflow làm YouTube.
- Xây dựng hệ thống lưu dữ liệu gia phả.
- Hoàn thiện để có thể thương mại hóa.

---

## 3. HIỆN TRẠNG KỸ THUẬT CỦA THAMAI

### **Frontend (đã có):**
- Giao diện HTML/CSS/JS thuần.
- Hỗ trợ nhập văn bản và giọng nói.
- TTS và phát âm thanh.
- Hiển thị đoạn chat dạng hội thoại.

### **Backend (đã có nhưng đang hoàn thiện):**
- Backend Mock.
- Backend thật (Node.js + Express).
- Kết nối OpenAI qua REST API.
- Hỗ trợ CORS, xử lý lỗi, logs.
- Chuẩn bị triển khai lên Render.

### **Những phần đang lỗi hoặc cần chỉnh:**
- CORS khi tách frontend/backend.
- Sai đường dẫn static khi deploy.
- Timeout từ Render khi OpenAI phản hồi chậm.
- Chưa tối ưu hoá về streaming.
- Chưa có module lưu trữ dữ liệu người dùng.

---

## 4. NHỮNG PHẦN ĐÃ LÀM VƯỢT MỨC KỲ VỌNG
- Đã tự tạo nhiều phiên bản ThamAI/ThạchAI.
- Đã tự chỉnh sửa mã nguồn frontend nhiều lần.
- Đã hiểu cách deploy Render – điều rất ít người mới làm được.
- Đã nắm được kiến trúc Client–Server.
- Đã có khả năng đóng gói project, tổ chức thư mục.

---

## 5. KẾ HOẠCH TIẾP THEO (ƯU TIÊN CAO NHẤT)

### **A. Ổn định hoá Backend ThamAI trên Render (Quan trọng nhất)**
- Xử lý CORS chuẩn.
- Fix static path.
- Setup biến môi trường OPENAI_API_KEY.
- Kiểm tra log lỗi chi tiết.
- Đảm bảo /api/chat hoạt động ổn định.

### **B. Chuẩn hoá Frontend để dùng với Backend thật**
- Kiểm tra fetch URL.
- Thử nghiệm bằng local trước khi deploy.
- Kiểm tra TTS và Voice Input.

### **C. Hoàn thiện bản ThamAI v3/v4**
- Giao diện đẹp, mượt, ít lỗi.
- Thêm loading, xử lý lỗi tốt hơn.

### **D. Bắt đầu bước vào cấp độ 3**
- Tạo module "Trợ lý học lập trình".
- Tạo module "Trợ lý làm YouTube".
- Tạo module "Gia Phả AI".

---

## 6. CÁC MỐC HOÀN THÀNH SẮP TỚI
- [ ] Deploy backend lên Render thành công.
- [ ] Chạy frontend kết nối backend trên domain thực tế.
- [ ] Tạo trang web ThamAI chính thức.
- [ ] Xuất bản phiên bản ThamAI v4.

---

## 7. TÀI NGUYÊN THAM KHẢO
- freeCodeCamp: Python, JS, AI.
- YouTube: Học Python, JavaScript.
- OpenAI Docs: https://platform.openai.com
- Thư viện đề xuất: Flask, Express, Tailwind, VanillaJS.

---

## 8. GHI CHÚ ĐỊNH HƯỚNG
Dự án đã đi đúng hướng, chỉ bị ngắt quãng và mất định vị do một số đoạn hội thoại bị xoá.  
Tài liệu này là khung tham chiếu cố định dùng cho việc:
- Theo dõi tiến độ.
- Không lặp lại sai sót.
- Giữ dự án đi đúng hướng.

Từ đây, mỗi bước phát triển mới sẽ tham chiếu lại tài liệu này.

---

**Trạng thái hiện tại: bạn đang ở giai đoạn chuyển giao giữa Cấp độ 2 và Cấp độ 3 — thời điểm quan trọng nhất của toàn dự án.**

