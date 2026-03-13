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
