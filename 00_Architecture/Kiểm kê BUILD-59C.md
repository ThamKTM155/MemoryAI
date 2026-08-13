1. GATEWAY LAYER:
knowledge_gate.py                KEEP

gateways/
    identity_gateway.py          KEEP
    repository_gateway.py        KEEP
    graph_gateway.py             KEEP
    ai_gateway.py                KEEP

Chủ sở hữu

Knowledge Gate
---
2. IDENTITY:
core_identity.py                 KEEP

---
3. CHAT
memory_chat.py                   KEEP
---
4. REPOSITORY
memory_search.py                 KEEP

memory_repository.py             MERGE

knowledge_repository.py          MERGE

memory_database_builder.py       BUILD

memory_index.py                  MERGE

memory_index_v2.py               ARCHIVE

memory_search_v2.py              ARCHIVE

memory_search_v3.py              ARCHIVE
---
5. GRAPH
graph_loader.py                  KEEP

graph_query.py                   KEEP

graph_parser.py                  KEEP

graph_relationship_parser.py     KEEP

graph_edge_builder.py            KEEP

graph_entity_builder.py          KEEP

graph_project_builder.py         KEEP

graph_document_metadata.py       KEEP

graph_explorer.py                KEEP

memory_graph_builder.py          KEEP

memory_graph_lookup.py           KEEP
---
6. PIPELINE
memory_pipeline.py               KEEP

collect_facts.py                 KEEP

reason_engine.py                 KEEP

inference_engine.py              KEEP

impact_analysis.py               KEEP

decision_engine.py               KEEP

action_planner.py                KEEP
---
7. ANSWER
answer_generator.py              KEEP

intent_router.py                 KEEP

intent_answer_generator.py       KEEP

question_parser.py               KEEP

question_classifier.py           KEEP

query_renderer.py                KEEP
---
8. SERVER
memory_server.py                 KEEP

memory_api.py                    KEEP

memory_query_service.py          KEEP

memory_ask.py                    MERGE
---
9. BUILD TOOLS
batch_import.py

build_memory_database.py

build_knowledge_database.py

rebuild_summary_index.py

summary_parser.py

summary_generator.py

summary_migration.py

summary_audit.py

diary_processor.py

diary_audit.py

Đây là Build Tools.

Không nằm trong Runtime.

Điều em vừa phát hiện

Bây giờ em thấy MemoryAI đang có 5 tầng.

Presentation

↓

Application

↓

Gateway

↓

Core Domain

↓

Infrastructure

Đây là lần đầu tiên em có thể nhìn toàn bộ hệ thống bằng kiến trúc thay vì bằng danh sách file.

Nhưng em muốn dừng ở đây một chút

Em phát hiện một việc còn quan trọng hơn.

Trong tools đang tồn tại hai kiểu file:

Kiểu 1

Runtime

Ví dụ:

knowledge_gate.py

memory_chat.py

memory_search.py

Những file này được gọi khi người dùng hỏi.

Kiểu 2

Builder

Ví dụ:

build_memory_database.py

batch_import.py

summary_migration.py

Những file này chỉ chạy khi xây dựng dữ liệu.

Em đề xuất một thay đổi lớn (BUILD-60)

Sau khi hoàn thành kiểm kê, chúng ta sẽ tách Runtime và Builder thành hai khu vực riêng.

Ví dụ:

MemoryAI
│
├── runtime/
│   ├── knowledge_gate.py
│   ├── memory_chat.py
│   ├── memory_search.py
│   └── ...
│
├── builders/
│   ├── build_memory_database.py
│   ├── batch_import.py
│   ├── rebuild_summary_index.py
│   └── ...
│
├── domain/
│   ├── MemoryService
│   ├── MemoryRepository
│   ├── MemoryRecord
│   └── ...
│
└── gateways/
Lý do

Hiện nay thư mục tools đang chứa:

File chạy hàng ngày.
File chỉ chạy khi build.
File chỉ dùng để chuyển đổi dữ liệu.

Tất cả để chung một chỗ nên càng về sau càng khó quản lý.

Tuy nhiên, em chưa đề nghị làm ngay. Đây chỉ là mục tiêu của BUILD-60 sau khi BUILD-59 hoàn tất và chúng ta đã hiểu rõ toàn bộ kiến trúc.

Theo đúng nguyên tắc đã thống nhất, trước mắt chỉ phân loại và đánh dấu, chưa di chuyển hay đổi tên bất kỳ file nào. Điều đó sẽ giúp quá trình hợp nhất diễn ra an toàn và có thể kiểm thử từng bước.