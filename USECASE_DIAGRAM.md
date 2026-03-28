# Use Case Diagram - Hospitality Management System

```mermaid
graph TB
    subgraph Actors["<b>ACTORS</b>"]
        direction LR
        Guest["🏨 Hotel Guest"]
        FrontDesk["📋 Front Desk Staff"]
        Housekeeping["🧹 Housekeeping Staff"]
        Manager["📊 Hotel Manager"]
        ITAdmin["💻 IT Administrator"]
        Finance["💰 Finance Department"]
        Marketing["📢 Marketing Team"]
        RestaurantMgr["🍽️ Restaurant Manager"]
    end

    subgraph SystemBoundary["<b>HOTELHUB SYSTEM BOUNDARY</b>"]
        
        subgraph BookingMgmt["📅 BOOKING MANAGEMENT"]
            UC1["🔍 Search Rooms"]
            UC2["📝 Book Room"]
            UC3["❌ Cancel Booking"]
            UC4["📜 View Booking History"]
        end
        
        subgraph GuestServices["👤 GUEST SERVICES"]
            UC5["✅ Online Check-in"]
            UC6["🚪 Online Check-out"]
            UC7["🛎️ Request Service"]
            UC8["💳 Make Payment"]
            UC17["👤 Manage Guest Profile"]
        end
        
        subgraph Operations["⚙️ OPERATIONS"]
            UC9["🧹 Manage Housekeeping Tasks"]
            UC10["🚶 Process Walk-in Check-in"]
            UC11["🔧 Manage Maintenance Requests"]
            UC12["📈 Generate Reports"]
        end
        
        subgraph AdminMgmt["👔 ADMINISTRATION"]
            UC13["👥 Manage Staff Accounts"]
            UC14["📊 View Dashboard"]
            UC15["🔌 Manage OTA Integration"]
            UC16["🎯 Create Promotions"]
            UC18["🔔 Manage Notifications"]
        end
    end

    %% Guest Connections
    Guest --> UC1
    Guest --> UC2
    Guest --> UC3
    Guest --> UC4
    Guest --> UC5
    Guest --> UC6
    Guest --> UC7
    Guest --> UC8
    Guest --> UC17
    
    %% Front Desk Connections
    FrontDesk --> UC7
    FrontDesk --> UC8
    FrontDesk --> UC9
    FrontDesk --> UC10
    FrontDesk --> UC14
    FrontDesk --> UC17
    
    %% Housekeeping Connections
    Housekeeping --> UC9
    Housekeeping --> UC11
    
    %% Manager Connections
    Manager --> UC12
    Manager --> UC14
    Manager --> UC16
    
    %% IT Admin Connections
    ITAdmin --> UC13
    ITAdmin --> UC14
    ITAdmin --> UC18
    
    %% Finance Connections
    Finance --> UC8
    Finance --> UC12
    
    %% Marketing Connections
    Marketing --> UC15
    Marketing --> UC16
    
    %% Restaurant Manager Connections
    RestaurantMgr --> UC7
    
    %% Include Relationships
    UC2 -.->|<<include>>| UC1
    UC5 -.->|<<include>>| UC8
    UC6 -.->|<<include>>| UC8
    
    %% Extend Relationships
    UC7 -.->|<<extend>>| UC11

```mermaid

## Actor Summary Table

| Actor | Icon | Role Description | Use Cases |
|-------|------|------------------|-----------|
| **Hotel Guest** | 🏨 | Primary user who books rooms and uses services | Search, Book, Cancel, Check-in/out, Request Service, Payment, Manage Profile |
| **Front Desk Staff** | 📋 | Assists walk-in guests and manages operations | Housekeeping Tasks, Walk-in Check-in, Service Requests, Payments, Guest Profiles |
| **Housekeeping Staff** | 🧹 | Cleans rooms and reports maintenance | Housekeeping Tasks, Maintenance Requests |
| **Hotel Manager** | 📊 | Oversees operations and performance | Reports, Dashboard, Promotions |
| **IT Administrator** | 💻 | Manages system and security | Staff Accounts, Dashboard, Notifications |
| **Finance Department** | 💰 | Handles payments and financial reporting | Reports, Payment |
| **Marketing Team** | 📢 | Manages online presence and promotions | OTA Integration, Promotions |
| **Restaurant Manager** | 🍽️ | Manages dining and room service | Service Requests |

## Relationship Explanations

| Relationship Type | From | To | Explanation |
|------------------|------|-----|-------------|
| **<<include>>** | Book Room | Search Rooms | Booking requires checking availability first |
| **<<include>>** | Online Check-in | Make Payment | Check-in requires payment completion |
| **<<include>>** | Online Check-out | Make Payment | Check-out requires final payment |
| **<<extend>>** | Request Service | Manage Maintenance Requests | If service request is maintenance-related, it triggers maintenance workflow |
| **<<extend>>** | Book Room | Manage Notifications | Booking triggers confirmation notifications |
| **<<extend>>** | Online Check-in | Manage Notifications | Check-in triggers pre-arrival notifications |
| **<<extend>>** | Request Service | Manage Notifications | Service request triggers staff alerts |

---

# PART 2: Use Case Specifications (10 Critical Use Cases)

## UC-01: Search Rooms

| Element | Description |
|---------|-------------|
| **Use Case ID** | UC-01 |
| **Use Case Name** | Search Rooms |
| **Actor(s)** | Hotel Guest, Front Desk Staff |
| **Description** | User searches for available rooms based on dates, room type, and preferences |
| **Preconditions** | User is on the search page; system has room inventory data |
| **Postconditions** | Available rooms matching criteria are displayed |
| **Related FR** | FR-1: Room Booking and Search |
| **Related Stakeholder** | Hotel Guest, Front Desk Staff |

### Basic Flow:
1. User enters check-in date and check-out date
2. User selects room type (optional)
3. User specifies number of guests (optional)
4. User adds preferences (view type, floor, etc.)
5. User clicks "Search"
6. System validates dates (check-in before check-out)
7. System queries available rooms matching criteria
8. System displays list with:
   - Room type and photos
   - Price per night
   - Total price
   - Available amenities
9. User can sort results (price, rating, size)

### Alternative Flows:
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | No rooms available | System displays "No rooms available for selected dates" with alternative date suggestions |
| A-02 | Invalid date range | System displays error: "Check-out must be after check-in" |
| A-03 | Past dates entered | System displays error: "Cannot select past dates" |

---

## UC-02: Book Room

| Element | Description |
|---------|-------------|
| **Use Case ID** | UC-02 |
| **Use Case Name** | Book Room |
| **Actor(s)** | Hotel Guest, Front Desk Staff |
| **Description** | User reserves a selected room for specified dates |
| **Preconditions** | User has searched for rooms; selected room is available |
| **Postconditions** | Booking is created; room is marked as reserved; notification sent |
| **Related FR** | FR-1: Room Booking and Search, FR-12: Real-time Notification System |
| **Related Stakeholder** | Hotel Guest, Front Desk Staff |

### Basic Flow:
1. User selects a room from search results
2. System displays booking summary (dates, price, room details)
3. User enters guest information:
   - Full name
   - Email address
   - Phone number
   - Special requests (optional)
4. User reviews cancellation policy
5. User confirms booking
6. System creates booking record
7. System sends confirmation email with booking ID
8. System displays booking confirmation page

### Alternative Flows:
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Room no longer available | System displays "Room no longer available" and returns to search results |
| A-02 | Invalid email format | System displays error: "Please enter a valid email address" |
| A-03 | Missing required fields | System highlights missing fields and prevents submission |

---

## UC-03: Online Check-in

| Element | Description |
|---------|-------------|
| **Use Case ID** | UC-03 |
| **Use Case Name** | Online Check-in |
| **Actor(s)** | Hotel Guest |
| **Description** | Guest completes check-in process online 24 hours before arrival |
| **Preconditions** | Guest has confirmed booking; arrival date is tomorrow or today; payment completed |
| **Postconditions** | Guest is checked in; digital key is generated; notification sent |
| **Related FR** | FR-2: Online Check-in/out, FR-7: Integrated Billing, FR-12: Notifications |
| **Related Stakeholder** | Hotel Guest, Front Desk Staff |

### Basic Flow:
1. Guest logs into system
2. Guest selects upcoming booking
3. System displays "Check-in Available" button (if within 24-hour window)
4. Guest clicks "Check-in"
5. System displays check-in form:
   - Confirm guest details
   - Upload ID (optional)
   - Add vehicle information (optional)
   - Add additional guests
6. Guest completes form
7. Guest confirms check-in
8. System updates booking status to "Checked In"
9. System generates digital room key (if supported)
10. System sends check-in confirmation with room number

### Alternative Flows:
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Check-in window not open | System displays: "Check-in available 24 hours before arrival" |
| A-02 | Payment incomplete | System redirects to payment page before allowing check-in |
| A-03 | Guest cancels check-in | System returns to booking details without changes |

---

## UC-04: Request Service

| Element | Description |
|---------|-------------|
| **Use Case ID** | UC-04 |
| **Use Case Name** | Request Service |
| **Actor(s)** | Hotel Guest, Front Desk Staff, Restaurant Manager |
| **Description** | Guest requests services like extra towels, room service, or maintenance |
| **Preconditions** | Guest is checked in; guest is authenticated |
| **Postconditions** | Request is created and assigned to appropriate staff; notification sent |
| **Related FR** | FR-4: Guest Service Requests, FR-9: Maintenance Requests, FR-12: Notifications |
| **Related Stakeholder** | Hotel Guest, Front Desk Staff, Restaurant Manager, Housekeeping Staff |

### Basic Flow:
1. Guest selects "Request Service" from menu
2. System displays service categories:
   - Housekeeping (extra towels, pillows, cleaning)
   - Room Service (food, beverages)
   - Maintenance (AC issues, plumbing, TV)
   - Concierge (tours, transport)
3. Guest selects category
4. Guest enters details and quantity
5. Guest adds special instructions (optional)
6. Guest submits request
7. System creates request with timestamp
8. System notifies appropriate staff
9. System displays confirmation with estimated completion time

### Alternative Flows:
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Invalid request type | System displays error and returns to category selection |
| A-02 | Request during off-hours | System displays: "Will be addressed during next staff shift" |
| A-03 | Guest cancels request | System removes pending request |
| A-04 | Request is maintenance-related | System extends to UC-11 (Manage Maintenance Requests) |

---

## UC-05: Make Payment

| Element | Description |
|---------|-------------|
| **Use Case ID** | UC-05 |
| **Use Case Name** | Make Payment |
| **Actor(s)** | Hotel Guest, Front Desk Staff, Finance Department |
| **Description** | User processes payment for booking, room charges, or services |
| **Preconditions** | User has outstanding balance; payment method available |
| **Postconditions** | Payment is processed; balance is updated; receipt generated |
| **Related FR** | FR-7: Integrated Billing and Payments |
| **Related Stakeholder** | Hotel Guest, Finance Department |

### Basic Flow:
1. User selects "Make Payment"
2. System displays outstanding balance with breakdown:
   - Room charges
   - Service charges
   - Taxes and fees
3. User selects payment method:
   - Credit Card
   - Debit Card
   - Digital Wallet
   - Cash (in-person)
4. User enters payment details
5. System validates payment information
6. System processes payment
7. System marks balance as paid
8. System generates receipt
9. System sends receipt to user

### Alternative Flows:
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Payment declined | System displays: "Payment declined. Please try another method" |
| A-02 | Insufficient funds | System displays error and offers alternative payment method |
| A-03 | Split payment | System processes multiple payment methods for single balance |

---

## UC-06: Manage Housekeeping Tasks

| Element | Description |
|---------|-------------|
| **Use Case ID** | UC-06 |
| **Use Case Name** | Manage Housekeeping Tasks |
| **Actor(s)** | Front Desk Staff, Housekeeping Staff |
| **Description** | Staff views, assigns, and updates housekeeping tasks for rooms |
| **Preconditions** | User has appropriate role permissions |
| **Postconditions** | Tasks are updated; room status reflects cleaning progress |
| **Related FR** | FR-3: Housekeeping Task Management |
| **Related Stakeholder** | Front Desk Staff, Housekeeping Staff |

### Basic Flow:
1. Housekeeping staff logs into mobile interface
2. System displays daily task list:
   - Check-out rooms (priority)
   - Stay-over rooms
   - VIP rooms flagged
3. Staff selects a task
4. Staff marks task status:
   - "In Progress"
   - "Completed"
   - "Issue Reported"
5. System updates room status
6. Front desk receives notification when VIP room is ready
7. Housekeeping supervisor reviews completed tasks

### Alternative Flows:
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Staff reports issue | System creates maintenance request linked to room |
| A-02 | Room needs inspection | System flags room for supervisor review |
| A-03 | No tasks remaining | System displays completion message and thank you |

---

## UC-07: Generate Reports

| Element | Description |
|---------|-------------|
| **Use Case ID** | UC-07 |
| **Use Case Name** | Generate Reports |
| **Actor(s)** | Hotel Manager, Finance Department |
| **Description** | Authorized users generate operational and financial reports |
| **Preconditions** | User has manager or finance role permissions |
| **Postconditions** | Report is generated and available for download |
| **Related FR** | FR-10: Reporting and Analytics Dashboard |
| **Related Stakeholder** | Hotel Manager, Finance Department |

### Basic Flow:
1. User selects "Reports" from dashboard
2. System displays report types:
   - Occupancy Report
   - Revenue Report
   - Housekeeping Performance
   - Guest Satisfaction
   - Financial Summary
3. User selects report type
4. User sets date range
5. User selects format (PDF, Excel, CSV)
6. User clicks "Generate"
7. System queries data based on criteria
8. System generates report
9. System displays download link
10. System can schedule recurring reports

### Alternative Flows:
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | No data for date range | System displays: "No data found for selected period" |
| A-02 | Large date range | System warns: "Large data set may take several minutes" |
| A-03 | Invalid permissions | System displays: "Access denied" |

---

## UC-08: Manage Guest Profile

| Element | Description |
|---------|-------------|
| **Use Case ID** | UC-08 |
| **Use Case Name** | Manage Guest Profile |
| **Actor(s)** | Hotel Guest, Front Desk Staff |
| **Description** | User views and updates guest profile information, preferences, and loyalty status |
| **Preconditions** | User is authenticated |
| **Postconditions** | Profile information is updated |
| **Related FR** | FR-11: Guest Profile Management |
| **Related Stakeholder** | Hotel Guest, Marketing Team |

### Basic Flow:
1. User selects "My Profile"
2. System displays current profile information:
   - Personal details (name, email, phone)
   - Preferences (room type, amenities, dietary)
   - Stay history
   - Loyalty points balance
3. User updates information as needed
4. User saves changes
5. System validates updated information
6. System confirms successful update
7. System logs profile change

### Alternative Flows:
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Invalid email format | System displays error and requests correction |
| A-02 | Duplicate email | System displays: "Email already registered to another account" |
| A-03 | User requests data export | System generates GDPR-compliant data export file |

---

## UC-09: Manage OTA Integration

| Element | Description |
|---------|-------------|
| **Use Case ID** | UC-09 |
| **Use Case Name** | Manage OTA Integration |
| **Actor(s)** | Marketing Team |
| **Description** | Staff manages synchronization with Online Travel Agencies |
| **Preconditions** | User has marketing role permissions; OTA accounts configured |
| **Postconditions** | Room inventory and rates are synced with selected OTAs |
| **Related FR** | FR-8: OTA Integration Management |
| **Related Stakeholder** | Marketing Team, Hotel Manager |

### Basic Flow:
1. User selects "OTA Integration"
2. System displays connected OTAs:
   - Booking.com
   - Expedia
   - Agoda
3. User selects OTA to manage
4. System shows current sync status
5. User can:
   - Sync now
   - Update room mapping
   - Adjust commission settings
   - View sync history
6. User clicks "Sync Now"
7. System pushes current availability to OTA
8. System confirms successful sync
9. System logs sync activity

### Alternative Flows:
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Sync fails | System displays error; logs issue for investigation |
| A-02 | OTA credentials expired | System prompts for re-authentication |
| A-03 | Rate conflict | System flags conflict and requires manual resolution |

---

## UC-10: Manage Notifications

| Element | Description |
|---------|-------------|
| **Use Case ID** | UC-10 |
| **Use Case Name** | Manage Notifications |
| **Actor(s)** | IT Administrator, System (automated) |
| **Description** | System sends notifications to users; administrators configure notification settings |
| **Preconditions** | System is operational; user contact information is available |
| **Postconditions** | Notifications are delivered as configured |
| **Related FR** | FR-12: Real-time Notification System |
| **Related Stakeholder** | IT Administrator, Hotel Guest, Staff |

### Basic Flow:
1. System detects trigger event (booking, check-in, service request)
2. System determines recipient(s) based on event type
3. System selects appropriate channel(s):
   - Email
   - SMS
   - In-app notification
   - Push notification
4. System formats notification content
5. System sends notification
6. System logs delivery attempt
7. System handles delivery confirmation

### Alternative Flows:
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Invalid email/SMS | System logs failure and retries once |
| A-02 | User opted out | System respects opt-out preferences and does not send |
| A-03 | High notification volume | System queues notifications for batch processing |

---

# PART 3: Test Case Development

## Functional Test Cases

| Test Case ID | Requirement ID | Description | Test Steps | Expected Result |
|--------------|----------------|-------------|------------|-----------------|
| **TC-FR-01** | FR-1 | Search for available rooms | 1. Enter check-in: 2025-04-15<br>2. Enter check-out: 2025-04-17<br>3. Select "Deluxe Room"<br>4. Click Search | System displays available Deluxe Rooms with prices within 2 seconds |
| **TC-FR-02** | FR-1 | Search with no rooms available | 1. Enter fully booked dates<br>2. Click Search | System displays "No rooms available" message with alternative date suggestions |
| **TC-FR-03** | FR-1 | Search with invalid dates | 1. Enter check-out before check-in<br>2. Click Search | System displays error: "Check-out must be after check-in" |
| **TC-FR-04** | FR-2 | Complete online check-in | 1. Login as guest with booking<br>2. Navigate to upcoming booking<br>3. Click "Check-in" within 24-hour window<br>4. Confirm details<br>5. Submit | System confirms check-in; generates digital key; sends confirmation email |
| **TC-FR-05** | FR-2 | Check-in outside allowed window | 1. Login as guest with booking 3 days away<br>2. Attempt check-in | System displays: "Check-in available 24 hours before arrival" |
| **TC-FR-06** | FR-3 | Assign housekeeping task | 1. Guest checks out of Room 205<br>2. Front desk marks room as check-out | System automatically creates housekeeping task for Room 205; displays in housekeeping queue |
| **TC-FR-07** | FR-3 | Complete housekeeping task | 1. Housekeeping staff logs into mobile app<br>2. Selects task for Room 205<br>3. Marks as "Completed" | System updates room status to "Available"; front desk notified |
| **TC-FR-08** | FR-4 | Request extra towels | 1. Guest logs in during stay<br>2. Selects "Request Service"<br>3. Chooses "Extra Towels"<br>4. Submits request | System creates request; housekeeping staff receives notification; confirmation shown to guest with ETA |
| **TC-FR-09** | FR-4 | Request maintenance service | 1. Guest logs in during stay<br>2. Selects "Request Service"<br>3. Chooses "Maintenance"<br>4. Describes AC issue<br>5. Submits request | System creates maintenance request; maintenance staff notified; extends to maintenance tracking |
| **TC-FR-10** | FR-6 | Staff role access verification | 1. Login as Housekeeping staff<br>2. Attempt to access Financial Reports | System displays "Access Denied" error |
| **TC-FR-11** | FR-7 | Process payment | 1. Guest has outstanding balance<br>2. Enters valid credit card<br>3. Confirms payment | System processes payment; generates receipt; updates balance to $0 |
| **TC-FR-12** | FR-7 | Payment declined | 1. Guest enters expired credit card<br>2. Submits payment | System displays: "Payment declined. Please try another method" |
| **TC-FR-13** | FR-8 | OTA sync successful | 1. Marketing staff clicks "Sync Now" for Booking.com<br>2. System pushes availability | System confirms successful sync; updates last sync timestamp |
| **TC-FR-14** | FR-9 | Report maintenance issue | 1. Housekeeping finds broken AC in Room 205<br>2. Reports via mobile app with photo | System creates maintenance request; assigns priority; notifies maintenance staff |
| **TC-FR-15** | FR-10 | Generate occupancy report | 1. Manager selects "Occupancy Report"<br>2. Sets date range: March 2025<br>3. Clicks Generate | System generates PDF with occupancy percentage, room nights sold, and comparison to previous month |
| **TC-FR-16** | FR-11 | Update guest profile | 1. Guest logs in<br>2. Navigates to Profile<br>3. Updates phone number and dietary preference<br>4. Saves changes | System updates profile; confirms change; logs update timestamp |

---

## Non-Functional Test Cases

| Test Case ID | Requirement ID | Description | Test Steps | Expected Result |
|--------------|----------------|-------------|------------|-----------------|
| **TC-NF-01** | NFR-P1 | Page load time - Search | 1. Navigate to search page<br>2. Measure time to fully load | Page loads within 2 seconds on standard broadband connection |
| **TC-NF-02** | NFR-P1 | Page load time - Booking confirmation | 1. Complete booking<br>2. Measure time for confirmation page | Confirmation page loads within 3 seconds |
| **TC-NF-03** | NFR-P3 | API response time | 1. Send 100 search requests<br>2. Calculate average response time | 95% of requests respond within 300ms |
| **TC-NF-04** | NFR-S1 | Concurrent user load | 1. Simulate 500 concurrent users searching rooms<br>2. Monitor response times | Response time degradation < 20% from baseline |
| **TC-NF-05** | NFR-S1 | Peak hour performance | 1. Simulate 3x normal traffic (holiday season)<br>2. Monitor system stability | System remains operational; auto-scaling triggers at 70% capacity |
| **TC-NF-06** | NFR-SE1 | Data encryption verification | 1. Inspect database for stored guest data<br>2. Check network traffic for TLS | Sensitive data stored with AES-256; all traffic uses TLS 1.3 |
| **TC-NF-07** | NFR-SE2 | Failed login lockout | 1. Attempt login with wrong password 5 times<br>2. Try 6th attempt | Account locked after 5 attempts; error message displayed |
| **TC-NF-08** | NFR-SE2 | Session timeout | 1. Login to system<br>2. Leave idle for 16 minutes<br>3. Attempt to perform action | Session expired; user redirected to login page |
| **TC-NF-09** | NFR-U1 | Mobile responsiveness | 1. Open system on iPhone 12<br>2. Open on Android phone<br>3. Open on tablet | All features accessible; no horizontal scrolling; touch targets 44x44px minimum |
| **TC-NF-10** | NFR-U2 | Screen reader compatibility | 1. Enable screen reader (VoiceOver/TalkBack)<br>2. Navigate all pages | All interactive elements announced; images have alt text; forms have labels |
| **TC-NF-11** | NFR-M1 | API documentation accessibility | 1. Navigate to /api/docs endpoint<br>2. Verify Swagger/OpenAPI presence | API documentation available with all endpoints documented |
| **TC-NF-12** | NFR-D1 | Cross-platform deployment | 1. Deploy to Linux server<br>2. Deploy to Windows server | System runs identically on both platforms |

---

## Test Case Summary

| Category | Number of Test Cases |
|----------|---------------------|
| Functional Test Cases | 16 |
| Non-Functional Test Cases | 12 |
| **Total** | **28** |

---

# PART 4: Reflection on Use Case Modeling and Test Case Development

Create a new file `ASSIGNMENT5_REFLECTION.md`:

```markdown
# Assignment 5 Reflection: Translating Requirements to Use Cases and Tests

## Introduction

This assignment required translating stakeholder and system requirements from Assignment 4 into use case diagrams, detailed specifications, and test cases. This reflection documents the challenges encountered and lessons learned.

---

## Challenge 1: Ensuring Complete Stakeholder Coverage

**The Challenge:**
Assignment 4 identified 8 stakeholders. Ensuring all 8 were represented as actors in the use case diagram required careful mapping.

**How I Addressed It:**
I created a traceability matrix mapping each stakeholder to the use cases that serve them:
- Hotel Guest → 9 use cases (Search, Book, Check-in, etc.)
- Front Desk Staff → 6 use cases
- Restaurant Manager → 1 use case (Service Requests)

**Lesson Learned:** 
Every stakeholder identified in requirements must appear in the use case model. Missing actors indicates incomplete analysis.

---

## Challenge 2: Representing All Functional Requirements

**The Challenge:**
Assignment 4 had 12 functional requirements. Some (like Dynamic Pricing) are internal system features that don't directly involve user interaction.

**How I Addressed It:**
- Direct user-facing FRs became use cases (Search, Book, Check-in, etc.)
- Internal FRs were documented in use case specifications as system steps
- Added UC-17 (Manage Guest Profile) to cover FR-11
- Added UC-18 (Manage Notifications) to cover FR-12

**Lesson Learned:**
Not all functional requirements become standalone use cases. Some are represented as steps within other use cases or as system-level capabilities.

---

## Challenge 3: Determining Include vs. Extend Relationships

**The Challenge:**
Deciding when to use `<<include>>` vs `<<extend>>` was initially confusing.

**How I Addressed It:**
- **Include:** Required behavior that MUST happen as part of the base use case
  - "Book Room" includes "Search Rooms" (must check availability)
  - "Online Check-in" includes "Make Payment" (must pay first)
  
- **Extend:** Optional behavior that MAY happen
  - "Request Service" extends to "Manage Maintenance Requests" (only if maintenance issue)
  - Bookings extend to notifications (confirmation always sent)

**Lesson Learned:**
Include is for mandatory dependencies; extend is for optional variations. This distinction makes the diagram more meaningful.

---

## Challenge 4: Writing Testable Acceptance Criteria

**The Challenge:**
Converting use case flows into test cases required making each step verifiable.

**How I Addressed It:**
For each test case, I ensured:
- Clear, sequential test steps anyone can follow
- Expected results that are **observable and measurable**
- Preconditions that define exact starting state
- References back to specific requirement IDs

**Example:**
Instead of "system responds quickly" → "system displays results within 2 seconds"

**Lesson Learned:**
Good requirements make good test cases. Ambiguous requirements lead to ambiguous testing.

---

## Challenge 5: Testing Non-Functional Requirements

**The Challenge:**
Non-functional requirements (performance, security, scalability) are harder to test than functional ones.

**How I Addressed It:**
I defined test cases with:
- **Performance:** Load testing tools (JMeter) with specific thresholds
- **Security:** Verification steps (inspect encryption, check TLS, test lockout)
- **Scalability:** Simulating peak loads and monitoring auto-scaling
- **Usability:** Using actual devices and accessibility tools

**Lesson Learned:**
Non-functional testing requires specialized tools. Defining the test approach upfront helps stakeholders understand verification methods.

---

## Challenge 6: Maintaining Traceability Across Assignments

**The Challenge:**
Ensuring consistency between Assignment 4 (requirements) and Assignment 5 (use cases, tests) required constant cross-referencing.

**How I Addressed It:**
I created traceability links:
- Each use case references related FR IDs
- Each test case references a requirement ID
- Actors match stakeholders from Assignment 4
- Non-functional test cases reference NFR IDs

**Lesson Learned:**
Traceability is not just for large projects. Even for assignments, maintaining links prevents inconsistency and makes review easier.

---

## Challenge 7: Balancing Detail vs. Clarity

**The Challenge:**
Use case specifications can become overwhelming with too many alternative flows.

**How I Addressed It:**
I focused on:
- Main success scenario (happy path) delivering core value
- 3-4 alternative flows for common exceptions
- Not documenting every possible edge case

**Lesson Learned:**
Use cases should be **actor-focused**, not implementation-focused. If a step describes internal processing without user interaction, it may belong elsewhere.

---

## Traceability Matrix: Assignment 4 → Assignment 5

| Assignment 4 | Assignment 5 Artifact | Status |
|--------------|----------------------|--------|
| 8 Stakeholders | 8 Actors | ✅ Fully Aligned |
| FR-1: Search/Book | UC-01, UC-02 | ✅ Aligned |
| FR-2: Check-in/out | UC-03, UC-06 in spec | ✅ Aligned |
| FR-3: Housekeeping | UC-06 | ✅ Aligned |
| FR-4: Service Requests | UC-04 | ✅ Aligned |
| FR-5: Dynamic Pricing | Internal (backend) | ✅ Acceptable |
| FR-6: Access Control | UC-13 | ✅ Aligned |
| FR-7: Payments | UC-05 | ✅ Aligned |
| FR-8: OTA Integration | UC-09 | ✅ Aligned |
| FR-9: Maintenance | UC-04 (extend) | ✅ Aligned |
| FR-10: Reports | UC-07 | ✅ Aligned |
| FR-11: Guest Profile | UC-08 | ✅ Aligned |
| FR-12: Notifications | UC-10 | ✅ Aligned |
| NFRs (8+) | 12 Test Cases | ✅ Aligned |

---

## Key Takeaways

| Area | Key Learning |
|------|--------------|
| Use Case Diagrams | Relationships (include/extend) must reflect actual dependencies |
| Use Case Specifications | Preconditions and postconditions are critical for defining scope |
| Test Cases | Good tests require clear, measurable expected results |
| Traceability | Maintaining links prevents inconsistency across assignments |
| Non-Functional Testing | Requires specialized tools and clear acceptance criteria |
| Stakeholder Coverage | Every stakeholder from requirements must appear in use case model |

---

## Conclusion

This assignment reinforced that requirements engineering is an iterative, interconnected process. The use cases I created directly trace to the stakeholders and requirements identified in Assignment 4. The test cases verify the requirements specified. Each artifact builds on and validates the others.

The most valuable lesson was that **thinking about testing during requirements** (not after) leads to clearer, more actionable specifications. A requirement that cannot be tested is not a good requirement.

**Word Count: ~1,100 words**

    UC2 -.->|<<extend>>| UC18
    UC5 -.->|<<extend>>| UC18
    UC7 -.->|<<extend>>| UC18
