

```markdown
# Assignment 8: Activity Diagrams – Workflow Modeling

## Overview
This document contains 8 activity diagrams for complex workflows in the HotelHub system. Each diagram shows start/end nodes, actions, decisions, and swimlanes.

---

## 1. Book Room Activity Diagram

```mermaid
flowchart TD
    start([Start]) --> search[Guest searches rooms]
    search --> select[Select room]
    select --> enterDetails[Enter guest details]
    enterDetails --> validate{Valid details?}
    validate -- No --> showError[Show error message]
    showError --> enterDetails
    validate -- Yes --> confirm[Confirm booking]
    confirm --> payment[Process payment]
    payment --> success{Payment OK?}
    success -- Yes --> createBooking[Create booking record]
    createBooking --> sendEmail[Send confirmation email]
    sendEmail --> end1([End])
    success -- No --> fail[Show payment failed]
    fail --> payment
