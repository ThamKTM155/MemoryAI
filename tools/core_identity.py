import json
from pathlib import Path

CORE_FILE = Path(
    r"D:\MemoryAI\00_Core\personality_core.json"
)


def load_identity():
    """
    Đọc Personality Core.
    """

    if not CORE_FILE.exists():
        return {}

    with open(
        CORE_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def get_identity_value(key):

    data = load_identity()

    return data.get(key)

def answer_identity(question):
    """
    Trả lời các câu hỏi về bản thân ThamAI.
    """

    question = question.lower().strip()

    data = load_identity()

    # Tên
    if "tên" in question:
        return f"Tôi là {data.get('name', '')}."

    # Biệt danh
    if "biệt danh" in question:
        return f"Biệt danh của tôi là {data.get('nickname', '')}."

    # Phiên bản
    if "phiên bản" in question:
        return f"Tôi đang ở phiên bản {data.get('version', '')}."

    # Người sáng tạo
    if (
        "ai tạo" in question
        or "người tạo" in question
        or "người sáng tạo" in question
    ):
        return (
            "Tôi được anh "
            + data.get("creator", "")
            + " xây dựng."
        )

    # Gia đình
    if (
        "anh em" in question
        or "gia đình" in question
    ):

        family = "\n".join(
            data.get("family", [])
        )

        return (
            "Tôi thuộc hệ sinh thái gồm:\n"
            + family
        )

    # Sứ mệnh
    if (
        "sứ mệnh" in question
        or "làm gì" in question
        or "sinh ra để" in question
    ):

        mission = "\n".join(
            data.get("mission", [])
        )

        return mission

    return None

if __name__ == "__main__":

    core = load_identity()

    print("\n===== PERSONALITY CORE =====\n")

    for k, v in core.items():

        print(k)

        print(v)

        print()

        while True:

            q = input(
                "\nHỏi ThamAI: "
            ).strip()

            if q.lower() in [
                "exit",
                "quit"
            ]:
                break

            print()

            print(
                answer_identity(q)
            )