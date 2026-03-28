# Test Case Development - Hospitality Management System

---

## Functional Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status (Pass/Fail) |
|--------------|----------------|-------------|-------|-----------------|---------------|-------------------|
| TC-FR-01 | FR-1 | Search for available rooms | 1. Enter check-in: 2025-04-15<br>2. Enter check-out: 2025-04-17<br>3. Select "Deluxe Room"<br>4. Click Search | System displays available Deluxe Rooms with prices within 2 seconds | | Pending |
| TC-FR-02 | FR-1 | Search with no rooms available | 1. Enter fully booked dates<br>2. Click Search | System displays "No rooms available" message with alternative date suggestions | | Pending |
| TC-FR-03 | FR-1 | Search with invalid dates | 1. Enter check-out before check-in<br>2. Click Search | System displays error: "Check-out must be after check-in" | | Pending |
| TC-FR-04 | FR-2 | Complete online check-in | 1. Login as guest with booking<br>2. Navigate to upcoming booking<br>3. Click "Check-in" within 24-hour window<br>4. Confirm details<br>5. Submit | System confirms check-in; generates digital key; sends confirmation email | | Pending |
| TC-FR-05 | FR-2 | Check-in outside allowed window | 1. Login as guest with booking 3 days away<br>2. Attempt check-in | System displays: "Check-in available 24 hours before arrival" | | Pending |
| TC-FR-06 | FR-3 | Assign housekeeping task | 1. Guest checks out of Room 205<br>2. Front desk marks room as check-out | System automatically creates housekeeping task for Room 205; displays in housekeeping queue | | Pending |
| TC-FR-07 | FR-3 | Complete housekeeping task | 1. Housekeeping staff logs into mobile app<br>2. Selects task for Room 205<br>3. Marks as "Completed" | System updates room status to "Available"; front desk notified | | Pending |
| TC-FR-08 | FR-4 | Request extra towels | 1. Guest logs in during stay<br>2. Selects "Request Service"<br>3. Chooses "Extra Towels"<br>4. Submits request | System creates request; housekeeping staff receives notification; confirmation shown to guest with ETA | | Pending |
| TC-FR-09 | FR-4 | Request maintenance service | 1. Guest logs in during stay<br>2. Selects "Request Service"<br>3. Chooses "Maintenance"<br>4. Describes AC issue<br>5. Submits request | System creates maintenance request; maintenance staff notified; extends to maintenance tracking | | Pending |
| TC-FR-10 | FR-6 | Staff role access verification | 1. Login as Housekeeping staff<br>2. Attempt to access Financial Reports | System displays "Access Denied" error | | Pending |
| TC-FR-11 | FR-7 | Process payment | 1. Guest has outstanding balance<br>2. Enters valid credit card<br>3. Confirms payment | System processes payment; generates receipt; updates balance to zero | | Pending |
| TC-FR-12 | FR-7 | Payment declined | 1. Guest enters expired credit card<br>2. Submits payment | System displays: "Payment declined. Please try another method" | | Pending |
| TC-FR-13 | FR-8 | OTA sync successful | 1. Marketing staff clicks "Sync Now" for Booking.com<br>2. System pushes availability | System confirms successful sync; updates last sync timestamp | | Pending |
| TC-FR-14 | FR-9 | Report maintenance issue | 1. Housekeeping finds broken AC in Room 205<br>2. Reports via mobile app with photo | System creates maintenance request; assigns priority; notifies maintenance staff | | Pending |
| TC-FR-15 | FR-10 | Generate occupancy report | 1. Manager selects "Occupancy Report"<br>2. Sets date range: March 2025<br>3. Clicks Generate | System generates PDF with occupancy percentage, room nights sold, and comparison to previous month | | Pending |
| TC-FR-16 | FR-11 | Update guest profile | 1. Guest logs in<br>2. Navigates to Profile<br>3. Updates phone number and dietary preference<br>4. Saves changes | System updates profile; confirms change; logs update timestamp | | Pending |

---

## Non-Functional Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status (Pass/Fail) |
|--------------|----------------|-------------|-------|-----------------|---------------|-------------------|
| TC-NF-01 | NFR-P1 | Performance Test: Page load time | 1. Navigate to search page<br>2. Measure time to fully load<br>3. Repeat 10 times for average | Page loads within 2 seconds on standard broadband connection | | Pending |
| TC-NF-02 | NFR-SE2 | Security Test: Failed login lockout | 1. Attempt login with wrong password 5 times<br>2. Try 6th attempt with correct password | Account locked after 5 attempts; error message displayed; user cannot login for 15 minutes | | Pending |

---

## Test Case Summary

| Category | Number of Test Cases |
|----------|---------------------|
| Functional Test Cases | 16 |
| Non-Functional Test Cases | 2 |
| **Total** | **18** |

---

## Test Execution Notes

### Prerequisites for Testing:
- Test environment with sample data (rooms, bookings, guest profiles)
- Test accounts for each user role
- Load testing tool for performance test
- Stopwatch or performance monitoring tool for page load measurement

### Traceability:
All test cases reference the specific Functional Requirements (FR) and Non-Functional Requirements (NFR) defined in Assignment 4, ensuring complete traceability between requirements and validation.
