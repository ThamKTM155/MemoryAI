import os

BASE_DIR = r"D:\MemoryAI"

FILES_TO_LOAD = [

    r"09_AI_Memory\CURRENT_MISSION.md",
    r"09_AI_Memory\system_state.txt",

    r"03_Projects\PROJECT_INDEX.md",
    r"03_Projects\AutoYouTube.md",
    r"03_Projects\ThamAI.md",
    r"03_Projects\TalkingAI_Kids.md",

    r"01_Founder\founder_profile.md",
    r"01_Founder\WORKING_PRINCIPLES.md",

    r"02_Roadmap\ROADMAP_NEXT_PHASE.md",
    r"01_Founder\LIFE_TIMELINE.md",
]
SUMMARY_DIR = os.path.join(
    BASE_DIR,
    "11_Diary_Summary",
    "summaries"
)
OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "09_AI_Memory",
    "memory_context.txt"
)


def load_file(path):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()

    except Exception as e:

        return f"[ERROR] {path}: {e}"


def build_memory():

    sections = []

    for rel_path in FILES_TO_LOAD:

        full_path = os.path.join(
            BASE_DIR,
            rel_path
        )

        content = load_file(
            full_path
        )

        sections.append(
            "\n"
            + "=" * 80
            + "\nFILE: "
            + rel_path
            + "\n"
            + "=" * 80
            + "\n"
            + content
            + "\n"
        )
    # ==================================================
    # LOAD DIARY SUMMARIES
    # ==================================================

    if os.path.exists(SUMMARY_DIR):

        summaries = sorted(

            os.listdir(SUMMARY_DIR)

        )

        for filename in summaries:

            if not filename.endswith(".md"):

                continue

            full_path = os.path.join(

                SUMMARY_DIR,

                filename

            )

            content = load_file(full_path)

            sections.append(

                "\n"
                + "=" * 80
                + "\nDIARY SUMMARY: "
                + filename
                + "\n"
                + "=" * 80
                + "\n"
                + content
                + "\n"

            )
    final_context = "\n".join(
        sections
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            final_context
        )

    print(
        "✅ MEMORY BUILT"
    )

    print(
        OUTPUT_FILE
    )


if __name__ == "__main__":

    build_memory()