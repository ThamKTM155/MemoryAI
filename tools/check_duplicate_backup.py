import json

with open(
    "data/duplicate_backup.json",
    encoding="utf-8"
) as f:

    data = json.load(f)

indexes = []

for item in data:

    indexes.append(
        item["index"]
    )

print(
    "BACKUP:",
    len(indexes)
)

print(
    "UNIQUE:",
    len(set(indexes))
)