# Hospitality Management System

A comprehensive hotel operations management system designed to streamline front desk operations, room inventory management, booking processing, and housekeeping coordination for small to medium-sized hotels.

## Project Description

The Hospitality Management System digitizes and automates core hotel operations, enabling hotel staff to manage room inventory, process reservations, handle check-ins/check-outs, and provide better guest experiences through integrated services. This platform eliminates manual processes, reduces errors, and improves operational efficiency.

## Documentation

- [System Specification](./SPECIFICATION.md) - Detailed requirements, functional and non-functional specifications
- [Architecture Documentation](./ARCHITECTURE.md) - C4 architectural diagrams and system design

---

## Assignment 4: Stakeholder and System Requirements

Builds on the Hospitality Management System with detailed stakeholder analysis and requirements documentation.

### Documentation for Assignment 4

- [Stakeholder Analysis](./stakeholder-analysis.md) - 8 stakeholders with roles, concerns, pain points, and success metrics
- [Functional Requirements](./FUNCTIONAL-REQUIREMENTS.md) - 16 functional requirements with acceptance criteria
- [Non-Functional Requirements](./NON-FUNCTIONAL-REQUIREMENTS.md) - 17 requirements across usability, security, scalability, and more
- [Reflection](./REFLECTION.md) - Challenges and trade-offs in requirements engineering

---

## Assignment 5: Use Case Modeling and Test Case Development

- [Use Case Diagram](./USECASE_DIAGRAM.md)
- [Use Case Specifications](./USECASE_SPECIFICATIONS.md)
- [Test Cases](./TEST_CASES.md)
- [Assignment 5 Reflection](./REFLECTION_ASSIGNMENT5_.md)

---

## Assignment 6: Agile User Stories, Backlog, and Sprint Planning

- [Agile Planning Document](./ASSIGNMENT6_AGILE.md)
- [Assignment 6 Reflection](./REFLECTION_ASSIGNMENT6.md)

---

## Assignment 7: GitHub Project Templates and Kanban Board Implementation

- [Template Analysis and Justification](./template_analysis.md)
- [Kanban Board Explanation](./kanban_explanation.md)
- [Assignment 7 Reflection](./REFLECTION_ASSIGNMENT7.md)
- [Kanban Board Screenshot](./kanban-board.png.png)
- [Workflows Screenshot](./workflows-enabled.png.png)
- [Issues + Labels](./issues.png)

---

## Assignment 8: Object State and Activity Workflow Modeling

- [State Transition Diagrams](./state_transition_diagrams.md)
- [Activity Diagrams](./activity_diagrams.md)
- [Reflection](./REFLECTION_ASSIGNMENT8.md)

---

## Assignment 9: Domain Model and Class Diagram

- [Domain Model Documentation](./domain_model.md)
- [Class Diagram](./class_diagram.md)
- [Reflection](./REFLECTION_ASSIGNMENT9.md)

---

## Assignment 10: From Class Diagrams to Code with Creational Patterns

### Language Choice
**Python 3.9+** – chosen for simplicity, built-in unittest, and clean syntax.

### Class Implementation (`/src`)

| File | Description |
|------|-------------|
| [src/__init__.py](./src/__init__.py) | Package initializer |
| [src/room.py](./src/room.py) | Room class with status and pricing |
| [src/guest.py](./src/guest.py) | Guest class with loyalty points |
| [src/booking.py](./src/booking.py) | Booking class with check-in/out |
| [src/payment.py](./src/payment.py) | Payment class with authorization |
| [src/housekeeping_task.py](./src/housekeeping_task.py) | Housekeeping task management |
| [src/service_request.py](./src/service_request.py) | Guest service requests |
| [src/staff_account.py](./src/staff_account.py) | Staff account with roles |

### Creational Patterns (`/creational_patterns`)

| Pattern | File | Use Case |
|---------|------|----------|
| Simple Factory | [simple_factory.py](./creational_patterns/simple_factory.py) | Centralised room creation |
| Factory Method | [factory_method.py](./creational_patterns/factory_method.py) | Payment processor selection |
| Abstract Factory | [abstract_factory.py](./creational_patterns/abstract_factory.py) | Amenity families |
| Builder | [builder.py](./creational_patterns/builder.py) | Complex booking construction |
| Prototype | [prototype.py](./creational_patterns/prototype.py) | Cloning room templates |
| Singleton | [singleton.py](./creational_patterns/singleton.py) | Database connection |

### Unit Tests (`/tests`)

| File | Description |
|------|-------------|
| [tests/test_classes.py](./tests/test_classes.py) | Unit tests for all domain classes |
| [tests/test_creational_patterns.py](./tests/test_creational_patterns.py) | Unit tests for all creational patterns |

## Assignment 11: Repository Pattern and Storage Abstraction

### Language Choice
Python 3.9+ – continues from Assignment 10.

### Repository Pattern Justification
Used generics `Repository[T, ID]` to avoid code duplication across all entity repositories.

### Storage Abstraction Mechanism: Factory Pattern
The `RepositoryFactory` class allows switching between storage backends (MEMORY, DATABASE, FILESYSTEM).

### Storage Types

| Type | Status |
|------|--------|
| MEMORY | Implemented |
| DATABASE | Future |
| FILESYSTEM | Future |

### Repository Interfaces (`/repositories`)

| File | Description |
|------|-------------|
| [repositories/__init__.py](./repositories/__init__.py) | Package initializer |
| [repositories/repository_interface.py](./repositories/repository_interface.py) | Generic CRUD interface |
| [repositories/room_repository.py](./repositories/room_repository.py) | Room-specific queries |
| [repositories/guest_repository.py](./repositories/guest_repository.py) | Guest-specific queries |
| [repositories/booking_repository.py](./repositories/booking_repository.py) | Booking-specific queries |
| [repositories/payment_repository.py](./repositories/payment_repository.py) | Payment-specific queries |
| [repositories/housekeeping_repository.py](./repositories/housekeeping_repository.py) | Housekeeping-specific queries |
| [repositories/service_request_repository.py](./repositories/service_request_repository.py) | Service request queries |
| [repositories/staff_account_repository.py](./repositories/staff_account_repository.py) | Staff account queries |

### In-Memory Implementations (`/repositories/inmemory`)

| File | Description |
|------|-------------|
| [repositories/inmemory/__init__.py](./repositories/inmemory/__init__.py) | Package initializer |
| [repositories/inmemory/in_memory_base.py](./repositories/inmemory/in_memory_base.py) | Base HashMap storage |
| [repositories/inmemory/in_memory_room_repository.py](./repositories/inmemory/in_memory_room_repository.py) | In-memory Room repository |
| [repositories/inmemory/in_memory_guest_repository.py](./repositories/inmemory/in_memory_guest_repository.py) | In-memory Guest repository |
| [repositories/inmemory/in_memory_booking_repository.py](./repositories/inmemory/in_memory_booking_repository.py) | In-memory Booking repository |
| [repositories/inmemory/in_memory_payment_repository.py](./repositories/inmemory/in_memory_payment_repository.py) | In-memory Payment repository |
| [repositories/inmemory/in_memory_housekeeping_repository.py](./repositories/inmemory/in_memory_housekeeping_repository.py) | In-memory Housekeeping repository |
| [repositories/inmemory/in_memory_service_request_repository.py](./repositories/inmemory/in_memory_service_request_repository.py) | In-memory Service Request repository |
| [repositories/inmemory/in_memory_staff_account_repository.py](./repositories/inmemory/in_memory_staff_account_repository.py) | In-memory Staff Account repository |

### Factory (`/factories`)

| File | Description |
|------|-------------|
| [factories/__init__.py](./factories/__init__.py) | Package initializer |
| [factories/repository_factory.py](./factories/repository_factory.py) | Factory for creating repositories |

### Future Database Stub (`/future_stubs`)

| File | Description |
|------|-------------|
| [future_stubs/__init__.py](./future_stubs/__init__.py) | Package initializer |
| [future_stubs/database_repository_stub.py](./future_stubs/database_repository_stub.py) | Database implementation stub |

### Unit Tests (`/tests`)

| File | Description |
|------|-------------|
| [tests/test_in_memory_repositories.py](./tests/test_in_memory_repositories.py) | Tests for in-memory repositories |
| [tests/test_repository_factory.py](./tests/test_repository_factory.py) | Tests for repository factory |

### Class Diagram

| File | Description |
|------|-------------|
| [repository_class_diagram.md](./repository_class_diagram.md) | Updated class diagram with repository layer |

### API Documentation

The API is documented using Swagger UI. Screenshot below:

![Swagger UI](swagger-ui-full.png)

Live docs available at `http://localhost:8000/docs` when running locally.

##  Author Information

**Name:** Kamva Ntlanga

**Student ID:** 240497821

**Course:** Software Engineering

**Date:** March 8, 2026

##  License

This project is created for educational purposes as part of a Software Engineering assignment. 
