# Test Case Development - Hospitality Management System

---

## Functional Test Cases

| Test Case ID | Requirement ID | Description | Test Steps | Expected Result |
|--------------|----------------|-------------|------------|-----------------|
| TC-FR-01 | FR-1 | Search for available rooms | 1. Enter check-in: 2025-04-15<br>2. Enter check-out: 2025-04-17<br>3. Select "Deluxe Room"<br>4. Click Search | System displays available Deluxe Rooms with prices within 2 seconds |
| TC-FR-02 | FR-1 | Search with no rooms available | 1. Enter fully booked dates<br>2. Click Search | System displays "No rooms available" message with alternative date suggestions |
| TC-FR-03 | FR-1 | Search with invalid dates | 1. Enter check-out before check-in<br>2. Click Search | System displays error: "Check-out must be after check-in" |
| TC-FR-04 | FR-2 | Complete online check-in | 1. Login as guest with booking<br>2. Navigate to upcoming booking<br>3. Click "Check-in" within 24-hour window<br>4. Confirm details<br>5. Submit | System confirms check-in; generates digital key; sends confirmation email |
| TC-FR-05 | FR-2 | Check-in outside allowed window | 1. Login as guest with booking 3 days away<br>2. Attempt check-in | System displays: "Check-in available 24 hours before arrival" |
| TC-FR-06 | FR-3 | Assign housekeeping task | 1. Guest checks out of Room 205<br>2. Front desk marks room as check-out | System automatically creates housekeeping task for Room 205; displays in housekeeping queue |
| TC-FR-07 | FR-3 | Complete housekeeping task | 1. Housekeeping staff logs into mobile app<br>2. Selects task for Room 205<br>3. Marks as "Completed" | System updates room status to "Available"; front desk notified |
| TC-FR-08 | FR-4 | Request extra towels | 1. Guest logs in during stay<br>2. Selects "Request Service"<br>3. Chooses "Extra Towels"<br>4. Submits request | System creates request; housekeeping staff receives notification; confirmation shown to guest with ETA |
| TC-FR-09 | FR-4 | Request maintenance service | 1. Guest logs in during stay<br>2. Selects "Request Service"<br>3. Chooses "Maintenance"<br>4. Describes AC issue<br>5. Submits request | System creates maintenance request; maintenance staff notified; extends to maintenance tracking |
| TC-FR-10 | FR-6 | Staff role access verification | 1. Login as Housekeeping staff<br>2. Attempt to access Financial Reports | System displays "Access Denied" error |
| TC-FR-11 | FR-7 | Process payment | 1. Guest has outstanding balance<br>2. Enters valid credit card<br>3. Confirms payment | System processes payment; generates receipt; updates balance to zero |
| TC-FR-12 | FR-7 | Payment declined | 1. Guest enters expired credit card<br>2. Submits payment | System displays: "Payment declined. Please try another method" |
| TC-FR-13 | FR-8 | OTA sync successful | 1. Marketing staff clicks "Sync Now" for Booking.com<br>2. System pushes availability | System confirms successful sync; updates last sync timestamp |
| TC-FR-14 | FR-9 | Report maintenance issue | 1. Housekeeping finds broken AC in Room 205<br>2. Reports via mobile app with photo | System creates maintenance request; assigns priority; notifies maintenance staff |
| TC-FR-15 | FR-10 | Generate occupancy report | 1. Manager selects "Occupancy Report"<br>2. Sets date range: March 2025<br>3. Clicks Generate | System generates PDF with occupancy percentage, room nights sold, and comparison to previous month |
| TC-FR-16 | FR-11 | Update guest profile | 1. Guest logs in<br>2. Navigates to Profile<br>3. Updates phone number and dietary preference<br>4. Saves changes | System updates profile; confirms change; logs update timestamp |

---

## Non-Functional Test Cases

| Test Case ID | Requirement ID | Description | Test Steps | Expected Result |
|--------------|----------------|-------------|------------|-----------------|
| TC-NF-01 | NFR-P1 | Page load time - Search | 1. Navigate to search page<br>2. Measure time to fully load | Page loads within 2 seconds on standard broadband connection |
| TC-NF-02 | NFR-P1 | Page load time - Booking confirmation | 1. Complete booking<br>2. Measure time for confirmation page | Confirmation page loads within 3 seconds |
| TC-NF-03 | NFR-P3 | API response time | 1. Send 100 search requests<br>2. Calculate average response time | 95% of requests respond within 300ms |
| TC-NF-04 | NFR-S1 | Concurrent user load | 1. Simulate 500 concurrent users searching rooms<br>2. Monitor response times | Response time degradation less than 20% from baseline |
| TC-NF-05 | NFR-S1 | Peak hour performance | 1. Simulate 3x normal traffic (holiday season)<br>2. Monitor system stability | System remains operational; auto-scaling triggers at 70% capacity |
| TC-NF-06 | NFR-SE1 | Data encryption verification | 1. Inspect database for stored guest data<br>2. Check network traffic for TLS | Sensitive data stored with AES-256; all traffic uses TLS 1.3 |
| TC-NF-07 | NFR-SE2 | Failed login lockout | 1. Attempt login with wrong password 5 times<br>2. Try 6th attempt | Account locked after 5 attempts; error message displayed |
| TC-NF-08 | NFR-SE2 | Session timeout | 1. Login to system<br>2. Leave idle for 16 minutes<br>3. Attempt to perform action | Session expired; user redirected to login page |
| TC-NF-09 | NFR-U1 | Mobile responsiveness | 1. Open system on iPhone 12<br>2. Open on Android phone<br>3. Open on tablet | All features accessible; no horizontal scrolling; touch targets minimum 44x44px |
| TC-NF-10 | NFR-U2 | Screen reader compatibility | 1. Enable screen reader (VoiceOver/TalkBack)<br>2. Navigate all pages | All interactive elements announced; images have alt text; forms have labels |
| TC-NF-11 | NFR-M1 | API documentation accessibility | 1. Navigate to /api/docs endpoint<br>2. Verify Swagger/OpenAPI presence | API documentation available with all endpoints documented |
| TC-NF-12 | NFR-D1 | Cross-platform deployment | 1. Deploy to Linux server<br>2. Deploy to Windows server | System runs identically on both platforms |

---

## Test Case Summary

| Category | Number of Test Cases |
|----------|---------------------|
| Functional Test Cases | 16 |
| Non-Functional Test Cases | 12 |
| **Total** | **28** |

---

## Test Execution Notes

### Prerequisites for Testing:
- Test environment with sample data (rooms, bookings, guest profiles)
- Test accounts for each user role (Guest, Front Desk, Housekeeping, Manager, IT Admin, Finance, Marketing, Restaurant Manager)
- Load testing tool (e.g., JMeter, k6) for performance tests
- Mobile devices or emulators for responsiveness testing
- Screen reader software for accessibility testing

### Testing Priorities:
| Priority | Test Cases |
|----------|------------|
| High | Payment processing, room booking, online check-in |
| Medium | Service requests, housekeeping tasks, report generation |
| Low | OTA integration, profile management, notifications |

### Traceability to Assignment 4 Requirements:
All test cases reference the specific Functional Requirements (FR) and Non-Functional Requirements (NFR) defined in Assignment 4, ensuring complete traceability between requirements and validation.
