# MemoryAI Architecture

## core/
- memory_loader.py : Đọc/Ghi memory_db.json
- memory_query.py : Query dữ liệu
- memory_router.py : Điều hướng truy vấn

## tools/
- memory_builder.py : Build memory_db.json
- memory_loader.py : Build memory_context.txt
- memory_runtime.py : Runtime sử dụng memory_db.json
## Quy ước chạy

Luôn chạy từ thư mục gốc:

D:\MemoryAI

Ví dụ:

python -m tools.memory_builder
python -m tools.memory_runtime
python -m tools.memory_search