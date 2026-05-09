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

### Running Tests
```bash
python -m unittest discover tests
