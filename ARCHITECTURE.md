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
graph TD
    G1["Hotel Guest<br>Person booking or staying in a hotel"] -->|"Books rooms, views reservations"| S1["Hospitality Management System<br>Core hotel operations platform"]
    G2["Front Desk Staff<br>Handles check-in/out and guest support"] -->|"Manages reservations and check-ins"| S1
    G3["Hotel Manager<br>Oversees operations and analytics"] -->|"Reviews reports and system data"| S1
    G4["Housekeeping Staff<br>Cleans rooms and updates room status"] -->|"Updates room status"| S1

    S1 -->|"Processes credit card payments"| E1["Payment Gateway (External)<br>Stripe or PayPal"]
    S1 -->|"Sends booking confirmations"| E2["Email Service (External)<br>SendGrid"]
    S1 -->|"Syncs booking schedules"| E3["Calendar Integration (External)<br>Google Calendar / Booking.com"]

    graph TD
    User1["Hotel Guest"] --> C1["Web Application<br>React SPA<br>Guest booking portal"]
    User2["Hotel Staff"] --> C1
    User3["Housekeeping Staff"] --> C2["Mobile App<br>React Native<br>Housekeeping management"]

    C1 --> C3["API Application<br>Node.js / Express<br>Business logic layer"]
    C2 --> C3

    C3 --> D1[("Database<br>PostgreSQL<br>Stores rooms, bookings and guest data")]
    C3 --> D2[("Cache<br>Redis<br>Session and availability caching")]

    C3 --> E1["Payment Gateway<br>External payment processing"]
    C3 --> E2["Email Service<br>Notification service"]

    graph TD

    subgraph Frontend
        F1["Web Application<br>Admin and booking interface"]
        F2["Mobile App<br>Housekeeping interface"]
    end

    subgraph Backend
        B1["Authentication Controller"]
        B2["Booking Controller"]
        B3["Room Controller"]
        B4["Guest Controller"]
        B5["Billing Controller"]
        B6["Housekeeping Controller"]
        B7["Service Layer<br>Business logic"]
        B8["Repository Layer<br>Database access"]
    end

    subgraph Database
        DB1[("PostgreSQL Database")]
    end

    F1 --> B1
    F1 --> B2
    F1 --> B3
    F1 --> B4
    F2 --> B6

    B1 --> B7
    B2 --> B7
    B3 --> B7
    B4 --> B7
    B5 --> B7
    B6 --> B7

    B7 --> B8
    B8 --> DB1

    classDiagram

    class Booking {
        id
        checkInDate
        checkOutDate
        status
        totalPrice
        numberOfGuests
    }

    class Guest {
        id
        firstName
        lastName
        email
        phone
    }

    class Room {
        id
        roomNumber
        type
        status
        rate
    }

    class Payment {
        id
        amount
        method
        status
    }

    Booking --> Guest
    Booking --> Room
    Booking --> Payment

    sequenceDiagram

    participant Guest
    participant Web
    participant API
    participant DB
    participant Payment

    Guest->>Web: Search available rooms
    Web->>API: GET /rooms/available
    API->>DB: Query room availability
    DB-->>API: Return available rooms
    API-->>Web: Send room list
    Web-->>Guest: Display available rooms

    Guest->>Web: Select room and book
    Web->>API: POST /bookings
    API->>DB: Verify room availability
    DB-->>API: Confirm room is available

    API->>Payment: Process payment
    Payment-->>API: Payment confirmed

    API->>DB: Save booking record
    API-->>Web: Return booking confirmation
    Web-->>Guest: Show booking success

    pie
    title System Component Distribution
    "Frontend Interfaces" : 25
    "API Services" : 30
    "Database Layer" : 25
    "External Integrations" : 20

