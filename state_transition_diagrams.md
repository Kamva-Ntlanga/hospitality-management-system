# Assignment 8: State Transition Diagrams – Object Lifecycles

## Overview
This document contains 8 state transition diagrams for critical objects in the HotelHub system. Each diagram shows the object's lifecycle, states, transitions, and triggering events.

---

## 1. Room State Diagram

```mermaid
stateDiagram-v2
    [*] --> Available
    Available --> Booked: Guest books room
    Booked --> Available: Booking cancelled
    Booked --> Occupied: Guest checks in
    Occupied --> Available: Guest checks out
    Occupied --> Maintenance: Issue reported
    Maintenance --> Available: Repair completed
    Available --> Maintenance: Preventive maintenance
