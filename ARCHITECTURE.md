# C4 Architectural Diagrams: Hospitality Management System

## Project Title
Hospitality Management System

## Domain
Hospitality/Hotel Operations

## Problem Statement
Small to medium-sized hotels need an integrated digital platform to manage room inventory, reservations, guest check-in/out, and housekeeping coordination to eliminate manual processes, reduce errors, and improve operational efficiency.

## Individual Scope
The system focuses on core hotel operations (front desk, reservations, room management) and is designed for incremental development, starting with essential features and expanding to additional modules as time permits.

---

## Context Diagram (Level 1)
*Shows the system boundaries and external users/services*

```mermaid
graph TD
    G1["Hotel Guest<br>Person staying at or booking a hotel room"] -->|"Books rooms, views reservations"| S1["Hospitality Management System<br>Core hotel operations platform"]
    G2["Front Desk Staff<br>Handles check-in/out and guest services"] -->|"Manages reservations, processes check-ins"| S1
    G3["Hotel Manager<br>Oversees operations and reviews analytics"] -->|"Views reports, manages rates"| S1
    G4["Housekeeping Staff<br>Cleans rooms and updates status"] -->|"Updates room cleaning status"| S1
    S1 -->|"Processes credit card payments"| E1["Payment Gateway (External)<br>Stripe/PayPal"]
    S1 -->|"Sends booking confirmations"| E2["Email Service (External)<br>SendGrid"]
    S1 -->|"Syncs availability with booking platforms"| E3["Calendar Integration (External)<br>Google Calendar/Booking.com"]
```



```mermaid
graph TD
    User1["Hotel Guest<br>End user"] --> C1["Web Application<br>React SPA<br>Guest portal for booking"]
    User2["Hotel Staff<br>Front desk employees"] --> C1
    User3["Housekeeping Staff<br>Room cleaners"] --> C2["Mobile App<br>React Native<br>Housekeeping task management"]
    
    C1 --> C3["API Application<br>Node.js/Express<br>Business logic and data processing"]
    C2 --> C3
    
    C3 --> D1[("Database<br>PostgreSQL<br>Stores rooms, bookings, guests")]
    C3 --> D2[("Cache<br>Redis<br>Stores session data, availability")]
    C3 --> E1["Payment Gateway<br>External service<br>Processes transactions"]
    C3 --> E2["Email Service<br>External service<br>Sends notifications"]
```
