# 🏨 Hospitality Management System

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A comprehensive hotel operations management system designed to streamline front desk operations, room inventory management, booking processing, and housekeeping coordination for small to medium-sized hotels.

---

## 🚀 Quick Start (5 minutes)

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/hospitality-management-system.git
cd hospitality-management-system

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install fastapi uvicorn pydantic httpx pytest pytest-cov

# 4. Run the server
uvicorn api.main:app --reload

# 5. Open http://localhost:8000/docs
```

---

## 📚 Table of Contents

- Quick Start
- Features
- API Documentation
- Project Structure
- Business Rules
- Testing
- CI/CD Pipeline
- Contributing
- Assignments
- Author

---

## ✨ Features

| Module | Capabilities |
|----------|-------------|
| Room Management | Create, update status, delete rooms |
| Guest Management | Profile management, loyalty points |
| Booking Processing | Date validation, check-in/out |
| Payment Processing | Authorization and confirmation |
| Housekeeping | Task assignment and tracking |
| Service Requests | Guest service management |
| REST API | Full CRUD with Swagger docs |

---

## 📡 API Documentation

FastAPI provides automatic interactive documentation:

| URL | Description |
|------|------------|
| http://localhost:8000/docs | Swagger UI (test endpoints live) |
| http://localhost:8000/redoc | ReDoc documentation |
| http://localhost:8000/openapi.json | Raw OpenAPI specification |

### Main Endpoints

| Resource | Operations |
|----------|-----------|
| Rooms | GET, POST, PUT, DELETE `/api/rooms` |
| Guests | GET, POST, PUT, DELETE `/api/guests` |
| Bookings | GET, POST, confirm, cancel, check-in, check-out |

---

## 📁 Project Structure

```text
hospitality-management-system/
├── src/                    # Domain classes (Room, Guest, Booking, Payment)
├── services/               # Business logic layer
├── api/                    # REST API endpoints
├── repositories/           # Data access layer
│   └── inmemory/           # In-memory implementations
├── factories/              # Repository factory
├── creational_patterns/    # Factory, Builder, Singleton patterns
├── tests/                  # Unit and integration tests
├── future_stubs/           # Future database stubs
└── .github/workflows/      # CI/CD pipeline
```

---

## 📋 Business Rules

| Entity | Business Rule |
|---------|--------------|
| Room | Room number must be unique |
| Room | Price per night must be positive |
| Room | Cannot delete if booked or occupied |
| Guest | Email must be unique and contain `@` |
| Guest | Phone number must be at least 10 digits |
| Booking | Check-in must be before check-out |
| Booking | Check-in cannot be in the past |
| Booking | Cannot exceed 30 days |
| Booking | Room must be available |
| Booking | No overlapping bookings |

---

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=src --cov=services --cov=api

# Run specific test file
python -m pytest tests/test_booking_service.py -v
```

---

## 🔄 CI/CD Pipeline

GitHub Actions automates testing and deployment:

| Trigger | Action |
|----------|--------|
| Push to any branch | Runs all tests |
| Pull request to main | Runs tests, blocks merge if fail |
| Push to main (tests pass) | Builds and uploads artifact |

### Branch Protection

- Require PR review (1 approval)
- Require status checks to pass
- Block force pushes

---

## 🤝 Contributing

We welcome contributions! See `CONTRIBUTING.md` for guidelines.

### Good First Issues

| Issue | Difficulty | Description |
|--------|-----------|-------------|
| #1 | Easy | Search for available rooms |
| #2 | Easy | Book a room |
| #3 | Easy | Make payment for booking |
| #4 | Easy | Online check-in |
| #5 | Easy | Request services |

### How to Contribute

1. Comment on the issue you want.
2. Fork the repository.
3. Create a feature branch.
4. Make your changes.
5. Run tests.
6. Open a Pull Request.

---

## 📚 Assignments

| Assignment | Description |
|------------|------------|
| Assignment 4 | Stakeholder and System Requirements |
| Assignment 5 | Use Case Modeling and Test Cases |
| Assignment 6 | Agile User Stories and Sprint Planning |
| Assignment 7 | Kanban Board and GitHub Projects |
| Assignment 8 | State and Activity Diagrams |
| Assignment 9 | Domain Model and Class Diagram |
| Assignment 10 | Creational Patterns Implementation |
| Assignment 11 | Repository Pattern and Storage Abstraction |
| Assignment 12 | Service Layer and REST API |
| Assignment 13 | CI/CD with GitHub Actions |
| Assignment 14 | Open-Source Collaboration |

---

## 📖 Full Documentation

Documentation for all assignments, diagrams, and project artifacts can be found in the project repository.

---

## 👤 Author

**Kamva Ntlanga**
## Assignment 14: Open-Source Collaboration

### Getting Started

#### Prerequisites
- Python 3.9 or higher
- Git
- GitHub account

#### Installation

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/hospitality-management-system.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
5. Install dependencies: `pip install -r requirements.txt`
6. Run tests: `python -m pytest tests/ -v`

### Features for Contribution

| Feature | Difficulty | Labels | Issue |
|---------|------------|--------|-------|
| Search for available rooms | Easy | `good-first-issue` | #1 |
| Book a room | Easy | `good-first-issue` | #2 |
| Make payment for booking | Easy | `good-first-issue` | #3 |
| Online check-in | Easy | `good-first-issue` | #4 |
| Request services | Easy | `good-first-issue` | #5 |
| Manage housekeeping tasks | Medium | `feature-request` | #6 |

### Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

### Roadmap

See [ROADMAP.md](./ROADMAP.md) for future plans.

### License

This project is licensed under the MIT License - see [LICENSE](./LICENSE) for details.


##  Author Information

- Student ID: 240497821
- Course: Software Engineering
- Date: March 8, 2026

---

## 📄 License

MIT License - see `LICENSE` for details.

---

Built for educational purposes as part of a Software Engineering assignment.