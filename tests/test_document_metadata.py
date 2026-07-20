from core.diary_loader import DiaryLoader
from core.document_classifier import DocumentClassifier

loader = DiaryLoader(
    r"D:\MemoryAI\05_Diary"
)

classifier = DocumentClassifier()

docs = loader.load_all()

print("=" * 60)

for doc in docs:

    doc = classifier.classify(doc)

    print(doc["filename"])

    print("TYPE :", doc["type"])

    print()