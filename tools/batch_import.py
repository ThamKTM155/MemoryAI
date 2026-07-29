import re
from pathlib import Path
from tools.diary_processor import process_diary
from tools import memory_builder
DIARY_ROOT = Path(r"D:\MemoryAI\05_Diary")
from collections import OrderedDict

def find_diaries(root):
    """
    Tìm toàn bộ file nhật ký trong 05_Diary.
    """

    results = []

    for ext in ("*.txt", "*.md"):

        results.extend(root.rglob(ext))

    results = sorted(results)

    return results


def is_diary_file(path: Path):
    """
    Chỉ chấp nhận file nhật ký.

    Các tài liệu khác sẽ được importer riêng xử lý.
    """

    name = path.name.lower()

    # nhat-ky-2026-...
    if name.startswith("nhat-ky-"):
        return True

    # 2026-07-22.md
    
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.(md|txt)", name):
        return True

    return False

SOURCE_PRIORITY = {
    "NHATKYHANGNGAY": 1,
    "daily_logs": 2,
}

def normalize_diary_list(files):
    """
    Chuẩn hóa danh sách nhật ký.

    Rules:
    - Loại các bản copy: (1), (2), (3)...
    - Nếu trùng, ưu tiên file gốc.
    - Sắp xếp theo tên.
    """

    normalized = OrderedDict()

    for file in sorted(files):

        name = file.name

        # bỏ hậu tố (1), (2), (3)...
        canonical = re.sub(
            r"\s*\(\d+\)(?=\.[^.]+$)",
            "",
            name,
            flags=re.IGNORECASE
        )

        # chỉ giữ bản đầu tiên
        if canonical not in normalized:
            normalized[canonical] = file

        else:

            old_file = normalized[canonical]

            old_priority = 99
            new_priority = 99

            for folder, priority in SOURCE_PRIORITY.items():

                if folder in str(old_file):
                    old_priority = priority

                if folder in str(file):
                    new_priority = priority

            if new_priority < old_priority:
                normalized[canonical] = file

    return list(normalized.values())

def main():

    print()
    print("=" * 60)
    print("BATCH IMPORT - SCAN")
    print("=" * 60)
    print()

    files = [
        file
        for file in find_diaries(DIARY_ROOT)
        if is_diary_file(file)
    ]

    files = normalize_diary_list(files)

    print()
    print("=" * 60)
    print("NORMALIZED")
    print("=" * 60)

    print(f"Số diary hợp lệ : {len(files)}")
    print()

    for i, file in enumerate(files, 1):

        print(f"{i:03d}. {file}")
    print()
    print("=" * 60)
    print("IMPORT")
    print("=" * 60)

    success = 0
    failed = 0
    for i, file in enumerate(files, 1):

        print()
        print(f"[{i}/{len(files)}] {file.name}")

        try:
            process_diary(str(file))
            success += 1

        except Exception as e:
            print(f"❌ Lỗi: {e}")
            failed += 1
    print()
    print("=" * 60)
    print("KẾT QUẢ")
    print("=" * 60)

    print(f"Thành công : {success}")
    print(f"Thất bại   : {failed}")
    print()

    if failed == 0:
        print("=" * 60)
        print("BUILD MEMORY")
        print("=" * 60)

        memory_builder.main()
if __name__ == "__main__":
    main()