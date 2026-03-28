# Use Case Specifications - Hospitality Management System

---

## UC-01: Search Rooms

| Element | Description |
|---------|-------------|
| **Use Case ID** | UC-01 |
| **Use Case Name** | Search Rooms |
| **Actor(s)** | Hotel Guest, Front Desk Staff |
| **Description** | User searches for available rooms based on dates, room type, and preferences |
| **Preconditions** | User is on the search page; system has room inventory data |
| **Postconditions** | Available rooms matching criteria are displayed |

### Basic Flow:
1. User enters check-in date and check-out date
2. User selects room type (optional)
3. User specifies number of guests (optional)
4. User adds preferences (view type, floor, etc.)
5. User clicks "Search"
6. System validates dates (check-in before check-out)
7. System queries available rooms matching criteria
8. System displays list with room type, photos, price per night, total price, and available amenities
9. User can sort results by price, rating, or size

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

### Basic Flow:
1. User selects a room from search results
2. System displays booking summary (dates, price, room details)
3. User enters guest information: full name, email address, phone number, special requests (optional)
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

### Basic Flow:
1. Guest logs into system
2. Guest selects upcoming booking
3. System displays "Check-in Available" button (if within 24-hour window)
4. Guest clicks "Check-in"
5. System displays check-in form: confirm guest details, upload ID (optional), add vehicle information (optional), add additional guests
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

### Basic Flow:
1. Guest selects "Request Service" from menu
2. System displays service categories: Housekeeping (extra towels, pillows, cleaning), Room Service (food, beverages), Maintenance (AC issues, plumbing, TV), Concierge (tours, transport)
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
| A-04 | Request is maintenance-related | System extends to Manage Maintenance Requests |

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

### Basic Flow:
1. User selects "Make Payment"
2. System displays outstanding balance with breakdown: room charges, service charges, taxes and fees
3. User selects payment method: Credit Card, Debit Card, Digital Wallet, or Cash (in-person)
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

### Basic Flow:
1. Housekeeping staff logs into mobile interface
2. System displays daily task list: check-out rooms (priority), stay-over rooms, VIP rooms flagged
3. Staff selects a task
4. Staff marks task status: "In Progress", "Completed", or "Issue Reported"
5. System updates room status
6. Front desk receives notification when VIP room is ready
7. Housekeeping supervisor reviews completed tasks

### Alternative Flows:
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Staff reports issue | System creates maintenance request linked to room |
| A-02 | Room needs inspection | System flags room for supervisor review |
| A-03 | No tasks remaining | System displays completion message |

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

### Basic Flow:
1. User selects "Reports" from dashboard
2. System displays report types: Occupancy Report, Revenue Report, Housekeeping Performance, Guest Satisfaction, Financial Summary
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

### Basic Flow:
1. User selects "My Profile"
2. System displays current profile information: personal details (name, email, phone), preferences (room type, amenities, dietary), stay history, loyalty points balance
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

### Basic Flow:
1. User selects "OTA Integration"
2. System displays connected OTAs: Booking.com, Expedia, Agoda
3. User selects OTA to manage
4. System shows current sync status
5. User can: sync now, update room mapping, adjust commission settings, view sync history
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

### Basic Flow:
1. System detects trigger event (booking, check-in, service request)
2. System determines recipient(s) based on event type
3. System selects appropriate channel(s): email, SMS, in-app notification, push notification
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
