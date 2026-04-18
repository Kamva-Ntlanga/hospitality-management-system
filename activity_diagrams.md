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
```

Explanation:
The guest starts by searching for rooms. After selecting a room, they enter their details (name, email, phone). The system validates the details – if invalid (e.g., missing name, bad email format), it shows an error and asks the guest to re-enter. Once valid, the guest confirms the booking.

Next, the system processes payment. If payment fails (e.g., declined card), it shows a failure message and returns to the payment step. If payment succeeds, the system creates a booking record and sends a confirmation email. The process ends.

Swimlanes: Guest (search, select, enter, confirm); System (validate, process, create, send email)

Traceability: FR-1, FR-7

User Stories US-001, US-002, US-003

## 2. Online Check-in Activity Diagram
```mermaid
flowchart TD
    start([Start]) --> login[Guest logs in]
    login --> upcoming[View upcoming booking]
    upcoming --> checkWindow{Within 24 hours?}
    checkWindow -- No --> tooEarly[Show not available]
    tooEarly --> end1([End])
    checkWindow -- Yes --> verify[Verify payment status]
    verify --> paid{Payment complete?}
    paid -- No --> pay[Redirect to payment]
    pay --> verify
    paid -- Yes --> showForm[Show check-in form]
    showForm --> confirm[Confirm details]
    confirm --> generateKey[Generate digital key]
    generateKey --> updateStatus[Update booking status]
    updateStatus --> sendNotification[Send confirmation]
    sendNotification --> end2([End])
```

Explanation:
The guest logs in and views their upcoming booking. The system checks if the check-in window is open (within 24 hours of arrival). If not, it shows a message and ends. If yes, it verifies that payment is complete. If payment is missing, the guest is redirected to pay.

Once payment is confirmed, the guest sees a check-in form to confirm details (e.g., number of guests, vehicle info). After confirmation, the system generates a digital room key (if supported), updates the booking status to "Checked In", and sends a confirmation email/notification.

Swimlanes: Guest (login, view, confirm); System (verify, generate, update, send)

Traceability: FR-2, FR-7; User Story US-004

## 3. Request Service Activity Diagram
```mermaid
flowchart TD
    start([Start]) --> select[Guest selects service category]
    select --> describe[Enter description]
    describe --> submit[Submit request]
    submit --> notify[System notifies staff]
    notify --> assign[Staff assigns task]
    assign --> inProgress[Work in progress]
    inProgress --> complete[Service completed]
    complete --> feedback[Guest gives feedback]
    feedback --> end1([End])
```

Explanation:
The guest selects a service category (housekeeping, room service, maintenance) and enters a description. After submitting, the system notifies the relevant staff (e.g., housekeeping for towels, kitchen for food). A staff member picks up the task and assigns it to themselves. They work on it, then mark it completed. Finally, the guest provides feedback (e.g., rating, comment). This feedback helps the hotel improve service quality.

Swimlanes: Guest (select, describe, submit, feedback); System (notify); Staff (assign, work)

Traceability: FR-4; User Story US-005

## 4. Process Payment Activity Diagram
```mermaid
flowchart TD
    start([Start]) --> choose[User chooses payment method]
    choose --> enter[Enter payment details]
    enter --> validate[Validate card]
    validate -- Invalid --> error[Show error]
    error --> enter
    validate -- Valid --> auth[Authorize payment]
    auth -- Decline --> decline[Show decline]
    decline --> choose
    auth -- Approve --> capture[Capture funds]
    capture --> receipt[Generate receipt]
    receipt --> update[Update booking status]
    update --> end1([End])
```

Explanation: 
The user (guest or front desk staff) chooses a payment method (credit card, debit card, digital wallet). They enter card details. The system validates the card format (e.g., 16 digits, valid expiry). If invalid, it shows an error and asks again.

Once valid, the system authorizes the payment with the gateway. If declined (e.g., insufficient funds), it shows a decline message and returns to method selection. If approved, it captures the funds, generates a receipt, and updates the booking status to "Confirmed". The process ends.

Swimlanes: User (choose, enter); System (validate, authorize, capture, generate, update)

Traceability: FR-7; User Stories US-003, US-013

## 5. Manage Housekeeping Task Activity Diagram

```mermaid
flowchart TD
    start([Start]) --> checkout[Guest checks out]
    checkout --> autoCreate[System auto-creates task]
    autoCreate --> list[Housekeeping views task list]
    list --> priority[Prioritize check-out rooms]
    priority --> startTask[Start cleaning]
    startTask --> decision{Issue found?}
    decision -- Yes --> report[Report maintenance]
    report --> createMaint[Create maintenance request]
    createMaint --> continue[Continue cleaning]
    decision -- No --> complete[Mark completed]
    continue --> complete
    complete --> updateStatus[Update room status]
    updateStatus --> notifyFront[Notify front desk]
    notifyFront --> end1([End])
```

Explanation: 
When a guest checks out, the system automatically creates a housekeeping task for that room. Housekeeping staff view their task list and prioritize check-out rooms (since those need to be ready for new guests). They start cleaning.

If they find an issue (e.g., broken fixture, stained carpet), they report maintenance, which creates a separate maintenance request. They continue cleaning after noting the issue. If no issue, they mark the task completed. The system updates the room status to "Available" and notifies the front desk that the room is ready.

Swimlanes: Guest (checkout); System (auto-create, update, notify); Housekeeping (view, prioritize, start, report, complete); Front Desk (receive notification)

Traceability: FR-3; User Story US-006







































































