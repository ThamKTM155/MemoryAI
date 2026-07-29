# KNOWLEDGE MEMORY SPEC

Document ID: LTM-003

Version: Draft 1.0

Status: Draft

---

# 1. Purpose

Define the standard structure of Knowledge Memory used by MemoryAI.

---

# 2. Input

Validated Summary Metadata

Source:
- summary_parser.py
- Validation Engine

---

# 3. Output

Knowledge Record

Each record must preserve:

- id
- date
- source
- title
- summary
- tags

---

# 4. Principles

- Never modify original Summary.
- Every record must be traceable.
- Every record must have a unique id.
- Validation must complete before importing.

---

# 5. Consumer

Knowledge Memory is used by:

- Timeline Memory
- Decision Memory
- Experience Memory
- Cross Project Memory
- Project Router

---

Status

Draft