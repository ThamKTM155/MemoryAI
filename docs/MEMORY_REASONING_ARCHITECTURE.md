# Memory Reasoning Architecture

Status: BUILD-50C
Updated: 2026-08-04

---

## Vision

Memory Graph không chỉ lưu trữ tri thức.

Memory Graph phải có khả năng:

- hiểu
- kết nối
- suy luận
- giải thích

---

## Data Flow

Memory Graph
        │
        ▼
Collect Facts
        │
        ▼
Reason Engine
        │
        ▼
Insight Generator
        │
        ▼
Summary Generator
        │
        ▼
Query Output

---

## Layer 1

Collect Facts

Nhiệm vụ:

- đọc node
- đọc edges
- đọc metadata

Output:

facts

---

## Layer 2

Reason Engine

Input:

facts

Output:

reasoning

Ví dụ:

connected_document

important_document

architecture_document

...

---

## Layer 3

Insight Generator

Input:

reasoning

Output:

insight text

---

## Layer 4

Summary Generator

Input:

facts

Output:

summary text

---

## Layer 5

Query Renderer

Input

summary

insight

relationships

Output

CLI

API

Web
---

## Design Principles

- Architecture First
- Separation of Responsibilities
- Loose Coupling
- Stable Interfaces
- Test Before Freeze