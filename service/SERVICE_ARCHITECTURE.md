# SERVICE ARCHITECTURE

## Goal

Provide a service layer for managing MemoryRecord objects.

## Components

- MemoryService
- MemoryValidator
- MemoryRepository

## Responsibilities

### MemoryService

- Create memory
- Update memory
- Delete memory
- Search memory

### MemoryValidator

- Validate input data
- Check required fields
- Verify memory type

### MemoryRepository

- Save memory
- Load memory
- Update memory
- Delete memory

## Data Flow

MemoryFactory
        ↓
MemoryService
        ↓
MemoryRepository
        ↓
Storage