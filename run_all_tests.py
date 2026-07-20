import subprocess

tests = [

    "tests.test_diary_loader",

    "tests.test_document_classifier",

    "tests.test_document_manager",

    "tests.test_knowledge_repository",

    "tests.test_knowledge_manager",

    "tests.test_roadmap_manager",

    "tests.test_adr_manager",

    "tests.test_memory_reasoning",
    
    "tests.test_memory_api"

]

for test in tests:

    print("=" * 60)

    print(test)

    print("=" * 60)

    subprocess.run(

        ["python", "-m", test]

    )
