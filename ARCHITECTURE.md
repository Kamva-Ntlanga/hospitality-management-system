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

# C4 Architecture Diagrams

## Context Diagram (Level 1)

```mermaid
C4Context
    title System Context diagram for Hospitality Management System
    
    Person(guest, "Hotel Guest", "Person staying at or booking a hotel room")
    Person(frontDesk, "Front Desk Staff", "Handles check-in/out and guest services")
    Person(manager, "Hotel Manager", "Oversees operations and reviews reports")
    Person(housekeeping, "Housekeeping Staff", "Cleans rooms and updates status")
    
    System(hms, "Hospitality Management System", "Core platform for hotel operations")
    
    System_Ext(paymentGateway, "Payment Gateway", "Processes credit card transactions")
    System_Ext(emailService, "Email Service", "Sends booking confirmations")
    System_Ext(calendarAPI, "Calendar Integration", "Sync with external booking platforms")
    
    Rel(guest, hms, "Makes reservations, views bookings")
    Rel(frontDesk, hms, "Manages check-in/out, bookings")
    Rel(manager, hms, "Views reports, manages rates")
    Rel(housekeeping, hms, "Updates room cleaning status")
    
    Rel(hms, paymentGateway, "Process payments via")
    Rel(hms, emailService, "Sends notifications via")
    Rel(hms, calendarAPI, "Syncs availability with")
    
    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")

Container Diagram (Level 2)
graph TD
    Guest["Hotel Guest"] --> Web["Web Application<br/>(React SPA)"]
    Staff["Hotel Staff"] --> Web
    Housekeeping["Housekeeping Staff"] --> Mobile["Mobile App<br/>(React Native)"]
    
    Web --> API["API Application<br/>(Node.js/Express)"]
    Mobile --> API
    
    API --> DB[(Database<br/>PostgreSQL)]
    API --> Cache[(Cache<br/>Redis)]
    API --> Payment["Payment Gateway<br/>(External)"]
    API --> Email["Email Service<br/>(External)"]

Component Diagram (Level 3) - API Application
graph TD
    subgraph "API Application"
        Auth["Auth Controller<br/>Handles login/security"]
        Booking["Booking Controller<br/>Manages reservations"]
        Room["Room Controller<br/>Manages inventory"]
        Guest["Guest Controller<br/>Manages profiles"]
        Billing["Billing Controller<br/>Handles payments"]
        Report["Reporting Controller<br/>Generates reports"]
        House["Housekeeping Controller<br/>Manages cleaning"]
        
        Service["Service Layer<br/>Business Logic"]
        Repository["Repository Layer<br/>Data Access"]
    end
    
    Auth --> Service
    Booking --> Service
    Room --> Service
    Guest --> Service
    Billing --> Service
    Report --> Service
    House --> Service
    
    Service --> Repository
    Repository --> DB[(Database)]
    
    Web["Web App"] --> Auth
    Web --> Booking
    Web --> Room
    Mobile["Mobile App"] --> House

Code Diagram (Level 4) - Class Structure
classDiagram
    class Booking {
        +Long id
        +Date checkInDate
        +Date checkOutDate
        +String status
        +BigDecimal totalPrice
        +int numberOfGuests
        +confirmBooking()
        +cancelBooking()
    }
    
    class Guest {
        +Long id
        +String firstName
        +String lastName
        +String email
        +String phone
        +getFullName()
    }
    
    class Room {
        +Long id
        +String roomNumber
        +String type
        +String status
        +BigDecimal rate
        +boolean isAvailable()
    }
    
    Booking --> Guest
    Booking --> Room

Deployment Diagram
graph TD
    subgraph "Client Devices"
        Browser["Web Browser"]
        MobileApp["Mobile App"]
    end
    
    subgraph "Cloud Platform"
        subgraph "Load Balancer"
            LB["Nginx/ALB"]
        end
        
        subgraph "Application Server"
            API["API Containers"]
        end
        
        subgraph "Cache Server"
            Redis["Redis Cache"]
        end
        
        subgraph "Database Server"
            PostgreSQL[(Primary DB)]
            Replica[(Read Replica)]
        end
    end
    
    subgraph "External Services"
        Stripe["Payment Gateway"]
        SendGrid["Email Service"]
    end
    
    Browser --> LB
    MobileApp --> LB
    LB --> API
    API --> Redis
    API --> PostgreSQL
    API --> Replica
    API --> Stripe
    API --> SendGrid

End-to-End System Flow
graph LR
    subgraph "Frontend"
        Portal["Guest Portal"]
        Dashboard["Staff Dashboard"]
        HouseApp["Housekeeping App"]
    end
    
    subgraph "Backend Services"
        BookSvc["Booking Service"]
        RoomSvc["Room Service"]
        GuestSvc["Guest Service"]
        BillSvc["Billing Service"]
        HouseSvc["Housekeeping Service"]
    end
    
    subgraph "Data Storage"
        RoomDB[(Room DB)]
        GuestDB[(Guest DB)]
        BookDB[(Booking DB)]
    end
    
    subgraph "External"
        PayAPI["Payment API"]
        EmailAPI["Email API"]
    end
    
    Portal --> BookSvc
    Dashboard --> RoomSvc
    Dashboard --> GuestSvc
    HouseApp --> HouseSvc
    
    BookSvc --> BookDB
    RoomSvc --> RoomDB
    GuestSvc --> GuestDB
    BillSvc --> PayAPI
    
    BookSvc --> EmailAPI

Booking Process Flow
sequenceDiagram
    Guest->>System: Search for rooms
    System->>Database: Check availability
    Database-->>System: Return available rooms
    System-->>Guest: Show available rooms
    
    Guest->>System: Select room and book
    System->>Database: Verify availability
    Database-->>System: Room available
    
    System->>Payment: Process payment
    Payment-->>System: Payment confirmed
    
    System->>Database: Create booking
    System->>Guest: Send confirmation

System Components Overview
pie title System Components Distribution
    "Frontend Components" : 30
    "Backend Services" : 35
    "Database Systems" : 20
    "External Integrations" : 15

Data Flow Diagram
flowchart TD
    User[(User)] -->|interacts with| UI[User Interface]
    UI -->|sends requests| API[API Gateway]
    
    API -->|routes to| Book[Booking Service]
    API -->|routes to| Room[Room Service]
    API -->|routes to| Guest[Guest Service]
    
    Book -->|reads/writes| BookDB[(Booking DB)]
    Room -->|reads/writes| RoomDB[(Room DB)]
    Guest -->|reads/writes| GuestDB[(Guest DB)]
    
    Book -->|sends| Email[Email Notification]
    Book -->|processes| Pay[Payment]

















































