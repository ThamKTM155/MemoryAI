# memory_search.py
from tools.summary_index_search import search_index
import os
from pathlib import Path
from datetime import datetime

MEMORY_FILE = (
    r"D:\MemoryAI\09_AI_Memory\memory_context.txt"
)

SUMMARY_DIR = Path(
    r"D:\MemoryAI\11_Diary_Summary\summaries"
)


def read_summary(summary_date):

    summary_file = SUMMARY_DIR / (
        summary_date + "_summary.md"
    )

    if not summary_file.exists():

        return None

    with open(

        summary_file,

        "r",

        encoding="utf-8"

    ) as f:

        return f.read()

def search_memory(keyword):
    summary_results = search_index(keyword)

    if summary_results:

        result = []

        for item in summary_results:

            text = read_summary(
                item["date"]
            )

            if text:

                result.append(text)

            else:

                result.append(

                    f"Không tìm thấy Summary của "

                    f"{item['date']}"

                )

        return "\n\n" + "="*80 + "\n\n".join(result)
    if not os.path.exists(MEMORY_FILE):

        print(
            "❌ Không tìm thấy memory_context.txt"
        )

        return

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        lines = f.readlines()

    keyword = keyword.lower()

    results = []

    for i, line in enumerate(lines):

        if keyword not in line.lower():
            continue

        start = max(
            0,
            i - 3
        )

        end = min(
            len(lines),
            i + 6
        )

        block = "".join(
            lines[start:end]
        ).strip()

        score = 0

        score += (
            block.lower()
            .count(keyword)
        )

        if "FILE:" in block:
            score += 5

        if keyword in block.lower():
            score += 2

        results.append(
            (
                score,
                block
            )
        )

    if not results:

        return "❌ Không tìm thấy"

    # bỏ trùng
    unique = {}

    for score, block in results:

        if block not in unique:

            unique[block] = score

    results = list(
        unique.items()
    )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    results = results[:5]

    output = []

    output.append(
        f"\n🔍 Top {len(results)} kết quả\n"
    )

    for idx, (
        block,
        score
    ) in enumerate(
        results,
        1
    ):

        output.append("=" * 80)

        output.append(
            f"KẾT QUẢ {idx} "
            f"(Score={score})"
        )

        output.append("=" * 80)

        output.append(block)

        output.append("")

    return "\n".join(output)

def search_memory_raw(query: str, memory_db: dict):
    """
    BUILD-037

    Raw Search API.

    Trả về dữ liệu thô để Ranking xử lý.

    Không format.

    Không print.

    Không ghép chuỗi.
    """

    if not memory_db:
        return []

    query = query.lower().strip()

    candidates = []

    # Duyệt toàn bộ database
    for category, items in memory_db.items():

        # Bỏ qua nếu không phải danh sách
        if not isinstance(items, list):
            continue

        for item in items:

            if not isinstance(item, dict):
                continue

            score = 0

            # Tìm trong tất cả giá trị của object
            for value in item.values():

                if isinstance(value, str):

                    score += value.lower().count(query)

                elif isinstance(value, list):

                    for x in value:

                        if isinstance(x, str):

                            score += x.lower().count(query)

            if score > 0:

                candidate = item.copy()

                candidate["_score"] = score

                candidate["_category"] = category

                candidates.append(candidate)

    return candidates

if __name__ == "__main__":

    while True:

        keyword = input(
            "\nNhập từ khóa: "
        ).strip()

        if keyword.lower() in [

            "exit",

            "quit"

        ]:

            break

        result = search_memory(keyword)

        if result:

            print(result)