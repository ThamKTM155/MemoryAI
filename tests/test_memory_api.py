from core.memory_api import Memory


memory = Memory("05_Diary")

memory.load()

print("=" * 60)
print("MEMORY API")
print("=" * 60)

#
# Summary
#

print()
print("SUMMARY")
print(memory.summary())

#
# Statistics
#

print()
print("STATS")
print(memory.stats())

#
# Latest Build
#

print()
print("LATEST BUILD")
print(memory.get_latest_build()["filename"])

#
# Current Roadmap
#

print()
print("CURRENT ROADMAP")
print(memory.get_current_roadmap()["filename"])

#
# Latest ADR
#

print()
print("LATEST ADR")
print(memory.get_latest_adr()["filename"])

#
# Find by Type
#

print()
print("=" * 60)
print("FIND BY TYPE : ADR")
print("=" * 60)

for doc in memory.find_by_type("ADR"):

    print(doc["filename"])

#
# Find by Date
#

print()
print("=" * 60)
print("FIND BY DATE : 2026-07-19")
print("=" * 60)

date_results = memory.find_by_date("2026-07-19")

print("COUNT =", len(date_results))

for doc in date_results:

    print(doc["filename"])

#
# Search
#

print()
print("=" * 60)
print("SEARCH : Builder")
print("=" * 60)

search_results = memory.search("Builder")

print("COUNT =", len(search_results))

for doc in search_results:

    print(doc["filename"])