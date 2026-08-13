"""
=========================================
CHAT SERVICE

BUILD-62

Executive Operations Center

Vai trò:
Điều phối yêu cầu của người chủ.

ChatService không trực tiếp:
- lưu Memory
- truy cập Storage
- thực hiện Graph
- gọi AI Provider

ChatService chỉ điều phối các thành phần
chịu trách nhiệm tương ứng.
=========================================
"""
from service.operations_center import execute

def process(message):

    # ----------------------------------
    # 0. Validate Input
    # ----------------------------------

    if message is None:
        return ""

    message = str(message).strip()

    if not message:
        return "Anh chưa nhập nội dung."

    return execute(message)