# GRAPH_SOURCE_MAP.md

# THAM ECOSYSTEM
## Memory Graph Source Map V1.0

Updated:
2026-08-02

Status:
BUILD-41A

---

# Mục tiêu

Định nghĩa toàn bộ nguồn dữ liệu được phép đưa vào Memory Graph.

Graph Builder chỉ đọc dữ liệu từ các nguồn được khai báo trong tài liệu này.

Không tự ý quét các thư mục khác.

---

# SOURCE 01

Name:
Diary Summary

Path:

11_Diary_Summary/summaries/

File Pattern:

*_summary.md

Node tạo ra:

- SUMMARY

Thông tin lấy:

- ID
- Date
- Version
- Source
- Keywords
- Related Projects

---

# SOURCE 02

Name:
Diary Index

Path:

11_Diary_Summary/summary_index.json

Node:

SUMMARY

Mục đích:

Tra cứu nhanh.

---

# SOURCE 03

Name:
Project Documents

Path:

11_Diary_Summary/

Bao gồm:

README.md

CHANGELOG.md

DESIGN_PHILOSOPHY.md

ADR-*.md

FREEZE*.md

BUILD*.md

Node:

DOCUMENT

---

# SOURCE 04

Name:
Memory Database

Path:

11_Diary_Summary/memory_db.json

Node:

MEMORY

Mục đích:

Lưu tri thức đã chuẩn hóa.

---

# SOURCE 05

Name:
MemoryAI

Path:

MemoryAI/

Node:

PROJECT

Quan hệ:

PROJECT

contains

DOCUMENT

---

# SOURCE 06

Name:
ThamAI Backend

Path:

ThamAI_Backend_new/

Node:

PROJECT

FILE

Quan hệ:

PROJECT

contains

FILE

---

# SOURCE 07

Name:
AutoYouTube

Path:

AutoYouTube/

Node:

PROJECT

FILE

BUILD

---

# SOURCE 08

Name:
Dashboard

Path:

Dashboard/

Node:

PROJECT

---

# SOURCE 09

Name:
VoiceAI

Path:

VoiceAI/

Node:

PROJECT

---

# SOURCE 10

Name:
Git

Nguồn:

Git Repository

Node:

COMMIT

Quan hệ:

COMMIT

implements

BUILD

---

# SOURCE 11

Name:
Production

Nguồn:

Render

Node:

DEPLOYMENT

Quan hệ:

DEPLOYMENT

deploys

COMMIT

---

# SOURCE 12

Name:
Personality Core

Nguồn:

core_identity.json

Node:

PERSON

MISSION

Quan hệ:

PERSON

owns

MISSION

---

# SOURCE 13

Name:
Rule Engine

Nguồn:

rule_engine.py

Node:

RULE

Quan hệ:

RULE

controls

PROJECT

---

# GRAPH BUILDER POLICY

Graph Builder chỉ đọc các SOURCE được khai báo.

Không tự ý quét toàn bộ ổ đĩa.

Nếu có nguồn dữ liệu mới:

1. Khai báo trong GRAPH_SOURCE_MAP.md.
2. Xác định Node.
3. Xác định Edge.
4. Kiểm thử.
5. Mới đưa vào Production.

---

# FUTURE SOURCES

Có thể bổ sung:

- GitHub Issues
- GitHub Releases
- YouTube Analytics
- Google Drive
- Google Calendar
- Render Logs
- Vercel
- Redis
- PostgreSQL
- Vector Database

Không cần sửa Graph Builder.

Chỉ cần cập nhật SOURCE MAP.