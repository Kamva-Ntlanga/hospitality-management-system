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
## CONTAINER DIAGRAM (LEVEL 2)

```mermaid
graph TD
    Guest["Hotel Guest"] --> Web["Web Application"]
    Staff["Hotel Staff"] --> Web
    House["Housekeeping Staff"] --> Mobile["Mobile App"]
    
    Web --> API["API Application"]
    Mobile --> API
    
    API --> DB[("Database")]
    API --> Cache[("Cache")]
    API --> Pay["Payment Gateway"]
    API --> Email["Email Service"]
```

## COMPONENT DIAGRAM (LEVEL 3)

```mermaid
graph TD
    subgraph Controllers
        Auth["Auth Controller"]
        Book["Booking Controller"]
        Room["Room Controller"]
        GuestC["Guest Controller"]
        Bill["Billing Controller"]
        HouseC["Housekeeping Controller"]
    end

    subgraph Services
        Service["Service Layer"]
    end

    subgraph Data
        Repo["Repository Layer"]
        DB[("Database")]
    end

    Auth --> Service
    Book --> Service
    Room --> Service
    GuestC --> Service
    Bill --> Service
    HouseC --> Service
    
    Service --> Repo
    Repo --> DB
```

## CODE DIAGRAM (LEVEL 4)

```mermaid
classDiagram
    class Booking {
        +id: Long
        +checkInDate: Date
        +checkOutDate: Date
        +status: String
        +confirm()
        +cancel()
    }
    
    class Guest {
        +id: Long
        +firstName: String
        +lastName: String
        +email: String
        +getFullName()
    }
    
    class Room {
        +id: Long
        +roomNumber: String
        +type: String
        +status: String
        +isAvailable()
    }
    
    Booking --> Guest
    Booking --> Room
```

## DEPLOYMENT DIAGRAM

```mermaid
graph TD
    subgraph Users
        Browser["Web Browser"]
        Phone["Mobile Phone"]
    end

    subgraph Cloud
        LB["Load Balancer"]
        
        subgraph Servers
            API1["API Server 1"]
            API2["API Server 2"]
        end
        
        Redis[("Redis Cache")]
        
        subgraph Databases
            Master[("Primary DB")]
            Replica[("Read Replica")]
        end
    end

    subgraph External
        Stripe["Stripe"]
        SendGrid["SendGrid"]
    end

    Browser --> LB
    Phone --> LB
    LB --> API1
    LB --> API2
    API1 --> Redis
    API2 --> Redis
    API1 --> Master
    API2 --> Master
    API1 --> Replica
    API2 --> Replica
    API1 --> Stripe
    API2 --> Stripe
    API1 --> SendGrid
    API2 --> SendGrid
```

## SYSTEM FLOW DIAGRAM

```mermaid
flowchart LR
    subgraph Frontend
        Portal["Guest Portal"]
        Dashboard["Staff Dashboard"]
        HouseApp["Housekeeping App"]
    end

    subgraph Backend
        API["API Gateway"]
        BookSvc["Booking Service"]
        RoomSvc["Room Service"]
        GuestSvc["Guest Service"]
    end

    subgraph Storage
        RoomDB[(Room DB)]
        GuestDB[(Guest DB)]
        BookDB[(Booking DB)]
    end

    Portal --> API
    Dashboard --> API
    HouseApp --> API
    
    API --> BookSvc
    API --> RoomSvc
    API --> GuestSvc
    
    BookSvc --> BookDB
    RoomSvc --> RoomDB
    GuestSvc --> GuestDB
```

## BOOKING SEQUENCE DIAGRAM

```mermaid
sequenceDiagram
    participant Guest
    participant Web
    participant API
    participant DB
    participant Payment
    
    Guest->>Web: Search rooms
    Web->>API: GET /rooms
    API->>DB: Query availability
    DB-->>API: Available rooms
    API-->>Web: Room list
    Web-->>Guest: Display options
    
    Guest->>Web: Select room
    Web->>API: POST /booking
    API->>DB: Check availability
    DB-->>API: Confirmed
    API->>Payment: Process payment
    Payment-->>API: Success
    API->>DB: Save booking
    API-->>Web: Confirmation
    Web-->>Guest: Booking complete
```

## COMPONENT DISTRIBUTION CHART

```mermaid
pie
    title "System Components by Percentage"
    "Frontend Interfaces" : 25
    "API Services" : 30
    "Databases" : 25
    "External Services" : 20
```




