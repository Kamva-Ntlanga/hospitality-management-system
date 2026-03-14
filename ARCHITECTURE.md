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

graph TD
    subgraph Frontend["Frontend Clients"]
        F1["Web Application<br>React-based admin panel"]
        F2["Mobile App<br>Housekeeping interface"]
    end

    subgraph Backend["API Application Components"]
        B1["Authentication Controller<br>Handles login, JWT tokens, user sessions"]
        B2["Booking Controller<br>Manages reservations, availability checks"]
        B3["Room Controller<br>Room inventory, status updates, rate management"]
        B4["Guest Controller<br>Guest profiles, history, preferences"]
        B5["Billing Controller<br>Invoice generation, payment processing"]
        B6["Housekeeping Controller<br>Cleaning tasks, room status"]
        B7["Service Layer<br>Business logic, validation, calculations"]
        B8["Data Repository Layer<br>Database queries, data persistence"]
    end

    subgraph Storage["Data Storage"]
        S1[("PostgreSQL Database<br>All persistent data")]
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
    B8 --> S1

classDiagram
    class Booking {
        +Long id
        +Date checkInDate
        +Date checkOutDate
        +String status
        +BigDecimal totalPrice
        +int numberOfGuests
        +String specialRequests
        +"Confirms the booking and blocks room"
        confirmBooking()
        +"Cancels booking and frees room"
        cancelBooking()
        +"Calculates number of nights stayed"
        calculateNights() int
    }
    
    class Guest {
        +Long id
        +String firstName
        +String lastName
        +String email
        +String phone
        +String passportNumber
        +"Returns full name of guest"
        getFullName() String
        +"Gets all past and upcoming bookings"
        getBookingHistory() List
    }
    
    class Room {
        +Long id
        +String roomNumber
        +String type
        +String status
        +BigDecimal rate
        +int maxOccupancy
        +List~String~ amenities
        +"Checks if room is free for given dates"
        isAvailable(Date start, Date end) boolean
        +"Updates room status (clean/dirty/maintenance)"
        updateStatus(String status)
    }
    
    class Payment {
        +Long id
        +BigDecimal amount
        +String method
        +String status
        +Date paymentDate
        +String transactionId
        +"Processes payment through gateway"
        processPayment()
        +"Processes refund if needed"
        refundPayment()
    }
    
    Booking --> Guest : " belongs to"
    Booking --> Room : " assigned to"
    Booking --> Payment : " has one"

graph TD
    subgraph Client["Client Layer - User Devices"]
        CL1["Web Browser<br>Chrome/Firefox/Safari<br>Runs React SPA"]
        CL2["Mobile Device<br>iOS/Android<br>Runs housekeeping app"]
    end

    subgraph Cloud["Cloud Infrastructure (AWS/Azure)"]
        
        subgraph LoadBalancer["Load Balancing Layer"]
            LB["Load Balancer<br>Nginx/ALB<br>Distributes incoming traffic"]
        end

        subgraph Application["Application Layer"]
            APP1["API Instance 1<br>Node.js container<br>Handles API requests"]
            APP2["API Instance 2<br>Node.js container<br>Handles API requests"]
        end

        subgraph Cache["Caching Layer"]
            RC["Redis Cache<br>In-memory data store<br>Session data & availability"]
        end

        subgraph Database["Database Layer"]
            DB1[("Primary Database<br>PostgreSQL Master<br>All write operations")]
            DB2[("Read Replica<br>PostgreSQL Slave<br>Reporting & queries")]
        end
    end

    subgraph External["External Services"]
        EX1["Stripe Payment Gateway<br>Payment processing"]
        EX2["SendGrid Email Service<br>Email notifications"]
    end

    CL1 --> LB
    CL2 --> LB
    LB --> APP1
    LB --> APP2
    APP1 --> RC
    APP2 --> RC
    APP1 --> DB1
    APP2 --> DB1
    APP1 --> DB2
    APP2 --> DB2
    APP1 --> EX1
    APP2 --> EX1
    APP1 --> EX2
    APP2 --> EX2

flowchart TB
    subgraph UI["User Interface Layer"]
        UI1["Guest Portal<br>Booking website"]
        UI2["Staff Dashboard<br>Admin interface"]
        UI3["Housekeeping App<br>Mobile interface"]
    end

    subgraph API["API Gateway Layer"]
        API1["REST API Endpoints<br>/api/bookings, /api/rooms, etc."]
    end

    subgraph Services["Business Logic Layer"]
        direction TB
        S1["Booking Service<br>Reservation logic"]
        S2["Room Service<br>Inventory management"]
        S3["Guest Service<br>Profile management"]
        S4["Billing Service<br>Payment processing"]
        S5["Housekeeping Service<br>Task management"]
    end

    subgraph Data["Data Persistence Layer"]
        D1[("Room Database<br>Room info & status")]
        D2[("Guest Database<br>Guest profiles")]
        D3[("Booking Database<br>Reservations")]
        D4[("Transaction Database<br>Payments & invoices")]
    end

    subgraph External["External Integration Layer"]
        E1["Payment Gateway API<br>Stripe"]
        E2["Email Service API<br>SendGrid"]
    end

    UI1 --> API1
    UI2 --> API1
    UI3 --> API1
    
    API1 --> S1
    API1 --> S2
    API1 --> S3
    API1 --> S4
    API1 --> S5
    
    S1 --> D3
    S2 --> D1
    S3 --> D2
    S4 --> D4
    
    S4 --> E1
    S1 --> E2

sequenceDiagram
    participant Guest as "Hotel Guest"
    participant Web as "Web Interface"
    participant API as "API Service"
    participant DB as "Database"
    participant Pay as "Payment Gateway"
    
    Note over Guest,Web: Guest searches for available rooms
    Guest->>Web: Enter dates and search
    Web->>API: GET /api/rooms/available
    API->>DB: Query room availability
    DB-->>API: Return available rooms
    API-->>Web: Send room list with rates
    Web-->>Guest: Display available rooms
    
    Note over Guest,Web: Guest selects room and books
    Guest->>Web: Select room & click Book
    Web->>API: POST /api/bookings
    API->>DB: Verify room still available
    DB-->>API: Confirmed available
    
    Note over API,Pay: Process payment
    API->>Pay: Process payment(amount, details)
    Pay-->>API: Payment confirmation
    
    Note over API,DB: Create booking record
    API->>DB: Insert booking record
    DB-->>API: Booking created
    
    API-->>Web: Return booking confirmation
    Web-->>Guest: Display success message

pie
    title "System Component Distribution (% of total codebase)"
    "Frontend Interfaces" : 25
    "API Services" : 30
    "Database Layer" : 25
    "External Integrations" : 20

