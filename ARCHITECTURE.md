
Every diagram must have its **own block**.

---

# Here is the FULL FIXED VERSION  
Copy **everything below** and replace your file with it.

```markdown
# C4 Architectural Diagrams: Hospitality Management System

## Project Title
Hospitality Management System

## Domain
Hospitality / Hotel Operations

## Problem Statement
Small to medium-sized hotels need an integrated digital platform to manage room inventory, reservations, guest check-in/out, and housekeeping coordination to eliminate manual processes, reduce errors, and improve operational efficiency.

## Individual Scope
The system focuses on core hotel operations (front desk, reservations, room management) and is designed for incremental development, starting with essential features and expanding to additional modules as time permits.

---

## Context Diagram (Level 1)

```mermaid
graph TD
    G1["Hotel Guest<br>Person booking or staying in a hotel"] -->|"Books rooms, views reservations"| S1["Hospitality Management System"]
    G2["Front Desk Staff<br>Handles check-in/out"] -->|"Manages reservations"| S1
    G3["Hotel Manager<br>Oversees operations"] -->|"Views reports"| S1
    G4["Housekeeping Staff<br>Cleans rooms"] -->|"Updates room status"| S1

    S1 -->|"Processes payments"| E1["Payment Gateway"]
    S1 -->|"Sends confirmations"| E2["Email Service"]
    S1 -->|"Syncs bookings"| E3["Calendar Integration"]
