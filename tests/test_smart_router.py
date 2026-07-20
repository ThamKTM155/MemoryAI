from core.routing.smart_router import SmartRouter

router = SmartRouter()

test_questions = [
    "build mới nhất",
    "knowledge repository",
    "adr gần nhất",
    "roadmap",
    "hello"
]

for q in test_questions:
    print()
    print("=" * 60)
    print("QUESTION :", q)
    print("ROUTE    :", router.route(q))