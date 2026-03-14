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
graph TD
    Guest["Hotel Guest"] -->|books rooms| HMS["Hospitality Management System"]
    FrontDesk["Front Desk Staff"] -->|manages check-in/out| HMS
    Manager["Hotel Manager"] -->|views reports| HMS
    Housekeeping["Housekeeping Staff"] -->|updates room status| HMS
    HMS -->|processes payments| Payment["Payment Gateway<br/>(External)"]
    HMS -->|sends confirmations| Email["Email Service<br/>(External)"]
    HMS -->|syncs availability| Calendar["Calendar Integration<br/>(External)"]

graph TD
    Guest["Hotel Guest"] --> WebApp["Web Application<br/>React SPA"]
    Staff["Hotel Staff"] --> WebApp
    HouseStaff["Housekeeping Staff"] --> MobileApp["Mobile App<br/>React Native"]
    
    WebApp --> API["API Application<br/>Node.js/Express"]
    MobileApp --> API
    
    API --> Database[("Database<br/>PostgreSQL")]
    API --> Cache[("Cache<br/>Redis")]
    API --> Payment["Payment Gateway<br/>(External)"]
    API --> Email["Email Service<br/>(External)"]
