TalkingAI_Kids_Final_Offline
🎯 Giới thiệu

TalkingAI_Kids_Final_Offline là ứng dụng web chạy hoàn toàn offline, hỗ trợ:

👶 Bé nói chuyện với robot (tiếng Việt)

🧠 Hội thoại nhiều lượt, không bị lặp

📖 Kể chuyện ru ngủ tự động nhiều câu

🎵 Nhạc ru nền bật / tắt

❌ Không cần Internet, không cần server

Phù hợp cho:

Trẻ em

Gia đình

Sử dụng trên máy tính cá nhân (Windows)

📂 Cấu trúc thư mục (CHUẨN)
TalkingAI_Kids_Final_Offline/
│
├─ index.html
├─ script.js
├─ README.md
│
├─ audio/
│   └─ kids-music.mp3
│
├─ images/
│   └─ avatar.png   (tuỳ chọn)
│
├─ Videos/          (tuỳ chọn – sau này mở rộng)
├─ Thumbnails/     (tuỳ chọn)


⚠️ Lưu ý quan trọng

File nhạc phải nằm trong thư mục audio/

Đường dẫn trong HTML:

<audio id="bgm" src="audio/kids-music.mp3" loop></audio>

▶️ Cách chạy (OFFLINE)

Mở thư mục TalkingAI_Kids_Final_Offline

Click đúp index.html

Trình duyệt hỏi quyền micro → Cho phép

Bấm:

🎤 BÉ NÓI → bắt đầu hội thoại

⏹ DỪNG → robot ngừng nghe

📖 KỂ CHUYỆN → đọc truyện ru ngủ

🎵 NHẠC RU → bật / tắt nhạc

✅ Không cần cài thêm gì.

🎤 Cách sử dụng hội thoại

Bấm 🎤 BÉ NÓI

Bé nói tự nhiên:

“Chào robot”

“Con buồn”

“Kể chuyện cho con”

Robot:

Lắng nghe liên tục

Trả lời từng câu

Không cần bấm lại

📖 Kể chuyện ru ngủ

Bấm 📖 KỂ CHUYỆN

Robot tự kể nhiều câu liên tiếp

Không cần mic

Phù hợp trước giờ ngủ

🧠 Nguyên lý kỹ thuật (tóm tắt)

Web Speech API:

SpeechRecognition (nghe)

SpeechSynthesis (nói)

Có trạng thái điều khiển:

talk – hội thoại

story – kể chuyện

idle – nghỉ

Có bộ chống lỗi:

Không start mic khi đang chạy

Không nói chồng tiếng

Không lỗi recognition already started

⚠️ Lưu ý trình duyệt

Khuyến nghị:

✅ Google Chrome (Windows)

⚠️ Edge: dùng được nhưng nên test mic

Không hỗ trợ:

Safari offline

Firefox (SpeechRecognition hạn chế)

🚀 Mở rộng tương lai (tuỳ chọn)

Truyện tương tác (bé trả lời → truyện rẽ nhánh)

Nhớ cảm xúc bé

Xuất video kể chuyện để đăng YouTube

Giao diện thiếu nhi nâng cao

👨‍👩‍👧‍👦 Mục tiêu

Ứng dụng hướng tới:

“Một người bạn nhỏ an toàn, nhẹ nhàng và luôn lắng nghe trẻ em.”