import subprocess

tests = [

    # ==================================================
    # DOCUMENT
    # ==================================================

    "tests.test_diary_loader",
    "tests.test_document_classifier",
    "tests.test_document_manager",

    # ==================================================
    # KNOWLEDGE
    # ==================================================

    "tests.test_knowledge_repository",
    "tests.test_knowledge_manager",
    "tests.test_roadmap_manager",
    "tests.test_adr_manager",
    "tests.test_memory_reasoning",
    "tests.test_memory_api",

    # ==================================================
    # TIMELINE
    # ==================================================

    "tests.test_timeline_builder",
    "tests.test_timeline_engine",

    # ==================================================
    # RELATIONSHIP
    # ==================================================

    "tests.test_relationship_builder",
    "tests.test_relationship_engine",

    # ==================================================
    # GRAPH
    # ==================================================

    "tests.test_graph_builder",
    "tests.test_graph_engine",
    "tests.test_knowledge_graph",

    # ==================================================
    # MEMORY QUERY
    # ==================================================

    "tests.test_memory_query",

    # ==================================================
    # REASONING PIPELINE
    # ==================================================

    "tests.test_reasoning_engine",
    "tests.test_context_builder",
    "tests.test_reflection_engine",
    "tests.test_planner_engine",
    "tests.test_memory_assistant",

]

passed = 0
failed = 0

for test in tests:

    print("=" * 60)
    print(test)
    print("=" * 60)

    result = subprocess.run(
        ["python", "-m", test]
    )

    if result.returncode == 0:
        passed += 1
    else:
        failed += 1

print()
print("=" * 60)
print("MEMORYAI REGRESSION SUMMARY")
print("=" * 60)
print(f"TOTAL TESTS : {len(tests)}")
print(f"PASSED      : {passed}")
print(f"FAILED      : {failed}")

if failed == 0:
    print()
    print("🎉 MEMORYAI CORE V3 : ALL TESTS PASSED")
else:
    print()
    print("❌ SOME TESTS FAILED")

print("=" * 60)