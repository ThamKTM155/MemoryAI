from core.document_classifier import DocumentClassifier

classifier = DocumentClassifier()

documents = [

    {
        "filename": "2026-07-18.md",
        "path": "",
        "content": ""
    },

    {
        "filename": "2026-07-18_AI_ECOSYSTEM_ROADMAP_V1.md",
        "path": "",
        "content": ""
    },

    {
        "filename": "ADR-001_MEMORY.md",
        "path": "",
        "content": ""
    },

    {
        "filename": "Thu muc nhat ky.md",
        "path": "",
        "content": ""
    }

]

for document in documents:

    result = classifier.classify(document)

    print(result["filename"])

    print("TYPE :", result["type"])

    print()