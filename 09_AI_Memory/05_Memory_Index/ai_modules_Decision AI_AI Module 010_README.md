# ==========================================
# AI MODULE 010
# Decision AI
# ==========================================

## Giới thiệu

Decision AI là AI Module chịu trách nhiệm phân tích toàn bộ Knowledge đã được
AI Module 009 xây dựng để đưa ra quyết định (Decision) cho nội dung sẽ được
sản xuất tiếp theo.

Module này là tầng ra quyết định (Decision Layer) của AutoYouTube AI Framework.

Decision AI không tạo Script, không Render Video và không Upload.

Nhiệm vụ chính của Module là lựa chọn chiến lược nội dung tối ưu dựa trên
Knowledge mà hệ thống đã học được.

---
## Đầu vào

Knowledge Database

Learning Summary

Knowledge Object

---

## Đầu ra

Decision Object

Strategy Object

Decision Database
---

## Chức năng

### Decision Coordinator

✓ Đọc Knowledge Database

✓ Điều phối toàn bộ Decision Pipeline

✓ Sinh Decision

✓ Lưu Decision Database

---

### Decision Engine

✓ Phân tích Knowledge

✓ Đánh giá Confidence

✓ Xếp hạng Pattern

✓ Trả Decision Result

---

### Pattern Selector

✓ Chọn Topic

✓ Chọn Hook

✓ Chọn Story

✓ Chọn Ending

✓ Tính Priority

---

### Strategy Builder

✓ Xây dựng Strategy

✓ Sinh Recommendation

✓ Chuẩn hóa Strategy Object

✓ Chuẩn bị dữ liệu cho Script Engine

---

## Kiến trúc

AI Module 009

Knowledge Base

        │

        ▼

Decision Coordinator

(decision.py)

        │

        ▼

Decision Engine

(decision_engine.py)

        │

 ┌──────┴────────┐

 ▼               ▼

Pattern Selector

(pattern_selector.py)

Strategy Builder

(strategy_builder.py)

        │

        ▼

decision_database.json

---
## sơ đồ AI Framework

AI Module 001
Scene Memory
        │
        ▼
AI Module 002
Scene Scoring
        │
        ▼
AI Module 003
Scene Learning
        │
        ▼
AI Module 004
Video Memory
        │
        ▼
AI Module 005
Analytics Database
        │
        ▼
AI Module 006
YouTube Analytics
        │
        ▼
AI Module 007
Performance Engine
        │
        ▼
AI Module 008
Winner AI
        │
        ▼
AI Module 009
Learning Engine
        │
        ▼
AI Module 010
Decision AI

(BUILD-17 Freeze)
---
## API

### Decision Coordinator

- system_info()

- make_decision()

- decision_summary()

- export_decision()

---

### Decision Engine

- evaluate_knowledge()

---

### Pattern Selector

- select_pattern()

---

### Strategy Builder

- build_strategy()

---

## Database

decision_database.json

Lưu toàn bộ kết quả Decision của AI.

Ví dụ:

[
    {
        "decision_version":"1.0",
        "topic":"Healing",
        "hook_type":"Emotion",
        "story_type":"Reflection",
        "ending_type":"Hope",
        "confidence":91,
        "reason":"Highest Knowledge Score",
        "strategy":"Continue this pattern"
    }
]

---

## Kết quả kiểm thử

✓ decision_test.py PASS

✓ decision_engine_test.py PASS

✓ pattern_selector_test.py PASS

✓ strategy_builder_test.py PASS

✓ Integration PASS

✓ Production PASS

---

## BUILD

BUILD-17

Decision AI Version 1.0

Development

---

## Tác dụng

Decision AI chịu trách nhiệm:

- Phân tích Knowledge.

- Lựa chọn Pattern.

- Xây dựng Strategy.

- Sinh Decision.

- Chuẩn bị dữ liệu cho Script Engine.

Module 010 không lựa chọn Winner.

Module 010 không tạo Lesson.

Module 010 không xây dựng Knowledge.

Module 010 là tầng ra quyết định của AutoYouTube AI Framework.

---

## Phiên bản

Version 1.0

BUILD-17

Ngày bắt đầu:

14-07-2026

---

## Trạng thái

Status

Development

Current BUILD

BUILD-17

---
Known Limitation

BUILD-17 chưa hỗ trợ Feature Profile.

Decision AI hiện chỉ học được:

- Topic
- Winner
- Lesson
- Knowledge

Chưa học được:

- Hook Type
- Story Type
- Ending Type
- Template
- Script Pattern

Các trường này sẽ được bổ sung trong BUILD-18
(Feature Profile Memory).
---
## Ghi chú

Decision AI tiếp nhận toàn bộ Knowledge đã được AI Module 009 tổng hợp.

Module chịu trách nhiệm phân tích các mẫu nội dung thành công và xây dựng
Decision Object để hỗ trợ các AI Module ở các BUILD tiếp theo.

Kiến trúc này giúp tách biệt rõ:

- AI Module 008: Winner.

- AI Module 009: Knowledge.

- AI Module 010: Decision.

Qua đó AutoYouTube chuyển từ khả năng "học từ dữ liệu" sang khả năng
"ra quyết định dựa trên tri thức".