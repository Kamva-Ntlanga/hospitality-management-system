# Functional Requirements: Hospitality Management System

**Author:** Kamva Ntlanga

**Date:** March 18, 2026

**Course:** Software Engineering

**Assignment:** 4 - Stakeholder and System Requirements Documentation

## Overview

This document defines the functional requirements for the Hospitality Management System. Each requirement is traceable to stakeholder needs and includes acceptance criteria where critical.

---

## Functional Requirements Summary

| Category | Count |
|----------|-------|
| Room Management | 3 |
| Booking Management | 4 |
| Guest Management | 2 |
| Front Desk Operations | 3 |
| Housekeeping | 2 |
| Reporting | 2 |
| **Total** | **16** |

---

## Detailed Functional Requirements

### Category A: Room Management

#### FR-01: Room Inventory Management
**Description:** The system shall maintain a complete inventory of all rooms including room number, room type (single, double, suite, deluxe), floor, and amenities.

**Rationale:** Front desk staff need accurate room data to assign rooms; managers need inventory for rate planning.

**Acceptance Criteria:**
- Admin can add, edit, or deactivate rooms
- Room types are configurable
- Amenities can be assigned to rooms
- System prevents duplicate room numbers
- Room count matches physical hotel inventory

**Traceability:** Hotel Managers, Front Desk Staff

---

#### FR-02: Room Status Tracking
**Description:** The system shall track real-time room status with the following states: Available, Occupied, Cleaning, Maintenance, Reserved.

**Rationale:** Housekeeping and front desk need accurate status to coordinate room turnover and assignments.

**Acceptance Criteria:**
- Status updates reflect within 2 seconds
- Status change history is logged with timestamp and user
- System prevents assigning occupied rooms
- Color-coded status display for quick recognition
- Status automatically updates based on check-in/out

**Traceability:** Housekeeping Staff, Front Desk Staff, Hotel Managers

---

#### FR-03: Room Rate Configuration
**Description:** The system shall allow managers to configure room rates based on season, day of week, special events, and length of stay.

**Rationale:** Managers need dynamic pricing to maximize revenue during peak periods and offer discounts during low seasons.

**Acceptance Criteria:**
- Rates can be set for specific date ranges
- Different rates for weekdays vs weekends
- Minimum stay requirements configurable
- Last-minute discounts can be applied
- Rate history maintained for analysis

**Traceability:** Hotel Managers, Finance Staff

---

### Category B: Booking Management

#### FR-04: Online Room Search
**Description:** The system shall allow guests to search for available rooms by date, number of guests, and room preferences.

**Rationale:** Guests need to find available rooms that meet their needs before booking.

**Acceptance Criteria:**
- Search results display within 2 seconds
- Results show room types, rates, and amenities
- Calendar shows availability at a glance
- Filters for price, room type, and amenities
- Mobile-responsive design for phone users

**Traceability:** Hotel Guests, Marketing Team

---

#### FR-05: Booking Creation
**Description:** The system shall allow guests and front desk staff to create bookings with guest details, dates, room selection, and special requests.

**Rationale:** Core functionality for capturing reservations from both online and walk-in guests.

**Acceptance Criteria:**
- Booking confirmation within 3 seconds
- Prevents double-booking of rooms
- Calculates total price including taxes
- Captures guest contact information
- Generates unique booking reference number
- Sends confirmation to guest email

**Traceability:** Hotel Guests, Front Desk Staff

---

#### FR-06: Booking Modification
**Description:** The system shall allow modification of existing bookings including date changes, room type changes, and cancellations based on hotel policy.

**Rationale:** Guests need flexibility to change plans; staff need to manage these changes efficiently.

**Acceptance Criteria:**
- Modifications reflect in real-time
- System checks availability for new dates
- Recalculates price based on current rates
- Cancellation policy applied automatically
- Modification history maintained
- Updated confirmation sent to guest

**Traceability:** Hotel Guests, Front Desk Staff

---

#### FR-07: Channel Management Integration
**Description:** The system shall integrate with online travel agencies (Booking.com, Expedia, Agoda) to synchronize room availability and rates in real-time.

**Rationale:** Managers need to prevent overbookings from multiple sales channels and maintain rate parity.

**Acceptance Criteria:**
- Availability updates within 30 seconds on all channels
- Rates synchronized across all platforms
- Bookings from OTAs appear in system immediately
- Prevents double-bookings from channel conflicts
- API failure alerts to IT admin
- Manual override option during outages

**Traceability:** Hotel Managers, External Partners, IT Administrators

---

### Category C: Guest Management

#### FR-08: Guest Profile Management
**Description:** The system shall create and maintain guest profiles including personal information, contact details, stay history, and preferences.

**Rationale:** Front desk needs guest history for personalized service; marketing needs data for targeted campaigns.

**Acceptance Criteria:**
- Profile creation on first booking
- Search guest by name, email, or phone
- View complete stay history
- Store preferences (room type, floor, amenities)
- GDPR-compliant data management
- Merge duplicate profiles

**Traceability:** Front Desk Staff, Marketing Team, Hotel Guests

---

#### FR-09: Guest Communication
**Description:** The system shall send automated communications to guests including booking confirmations, pre-arrival information, check-in instructions, and post-stay thank you.

**Rationale:** Guests expect timely communication; automated emails reduce staff workload.

**Acceptance Criteria:**
- Emails sent within 1 minute of trigger
- Customizable email templates
- Track email delivery and open rates
- SMS option for mobile numbers
- Multi-language support for international guests
- Opt-out option for marketing emails

**Traceability:** Hotel Guests, Marketing Team, Front Desk Staff

---

### Category D: Front Desk Operations

#### FR-10: Check-in Process
**Description:** The system shall support digital check-in including guest identification verification, room assignment, key card generation, and registration card printing.

**Rationale:** Front desk needs efficient check-in process to reduce guest wait times.

**Acceptance Criteria:**
- Check-in completes in under 3 minutes
- Scan passport/ID and auto-populate fields
- Room suggestions based on preferences
- Digital signature capture
- Registration card generation
- Integration with key card system

**Traceability:** Front Desk Staff, Hotel Guests

---

#### FR-11: Check-out Process
**Description:** The system shall support digital check-out including final bill generation, payment processing, invoice email, and room release.

**Rationale:** Quick check-out improves guest experience and frees rooms for cleaning.

**Acceptance Criteria:**
- Check-out completes in under 2 minutes
- Final bill itemizes all charges
- Multiple payment methods supported
- Invoice sent to guest email
- Room automatically marked for cleaning
- Loyalty points updated

**Traceability:** Front Desk Staff, Hotel Guests, Finance Staff

---

#### FR-12: Payment Processing
**Description:** The system shall process payments including deposits, full payments, refunds, and incidentals using credit cards, debit cards, and digital wallets.

**Rationale:** Secure payment handling is critical for hotel revenue and guest trust.

**Acceptance Criteria:**
- PCI-DSS compliant payment processing
- Multiple payment gateways supported
- Partial payments and deposits
- Automatic refund processing
- Payment receipts generated
- Failed payment notifications

**Traceability:** Finance Staff, Front Desk Staff, Hotel Guests

---

### Category E: Housekeeping

#### FR-13: Housekeeping Task Management
**Description:** The system shall generate and assign housekeeping tasks based on check-outs, stayover requests, and manager priorities.

**Rationale:** Housekeeping needs clear daily assignments to ensure all rooms are cleaned efficiently.

**Acceptance Criteria:**
- Daily task lists generated automatically
- Priority marking for express requests
- Task completion tracking
- Time tracking for each room
- Supervisor dashboard for progress monitoring
- Reassignment capability

**Traceability:** Housekeeping Staff, Hotel Managers

---

#### FR-14: Maintenance Request Management
**Description:** The system shall allow housekeeping and front desk to report maintenance issues with room number, issue type, priority, and photos.

**Rationale:** Quick reporting and tracking of maintenance issues ensures rooms are properly maintained.

**Acceptance Criteria:**
- Report issues via mobile or web
- Photo attachment capability
- Priority levels (urgent, high, normal, low)
- Assignment to maintenance staff
- Status tracking (reported, in-progress, completed)
- History of room issues

**Traceability:** Housekeeping Staff, Hotel Managers, Maintenance Staff

---

### Category F: Reporting

#### FR-15: Operational Reports
**Description:** The system shall generate operational reports including daily occupancy, revenue by room type, booking source analysis, and housekeeping productivity.

**Rationale:** Managers need data-driven insights for decision-making and performance tracking.

**Acceptance Criteria:**
- Reports generated in under 10 seconds
- Export to PDF, Excel, CSV
- Scheduled report delivery via email
- Custom date range selection
- Visual charts and graphs
- Comparison with previous periods

**Traceability:** Hotel Managers, Finance Staff, Marketing Team

---

#### FR-16: Financial Reports
**Description:** The system shall generate financial reports including daily revenue, payment method breakdown, outstanding balances, and tax summaries.

**Rationale:** Finance staff need accurate financial data for accounting and tax compliance.

**Acceptance Criteria:**
- Real-time revenue tracking
- Tax calculation by jurisdiction
- Payment reconciliation by method
- Outstanding invoice tracking
- Audit trail for all transactions
- Integration with accounting software

**Traceability:** Finance Staff, Hotel Managers

---

## Requirements Traceability Matrix

| Requirement | Stakeholder | Priority | Complexity |
|-------------|-------------|----------|------------|
| FR-01: Room Inventory | Managers, Front Desk | High | Low |
| FR-02: Room Status | Housekeeping, Front Desk | High | Medium |
| FR-03: Room Rates | Managers, Finance | High | Medium |
| FR-04: Room Search | Guests, Marketing | High | Medium |
| FR-05: Booking Creation | Guests, Front Desk | Critical | High |
| FR-06: Booking Modification | Guests, Front Desk | High | Medium |
| FR-07: Channel Integration | Managers, IT | Medium | High |
| FR-08: Guest Profiles | Front Desk, Marketing | Medium | Medium |
| FR-09: Guest Communication | Guests, Marketing | Medium | Low |
| FR-10: Check-in | Front Desk, Guests | Critical | Medium |
| FR-11: Check-out | Front Desk, Guests | Critical | Medium |
| FR-12: Payment | Finance, Guests | Critical | High |
| FR-13: Housekeeping Tasks | Housekeeping, Managers | High | Low |
| FR-14: Maintenance | Housekeeping, Managers | Medium | Low |
| FR-15: Operational Reports | Managers, Marketing | Medium | Medium |
| FR-16: Financial Reports | Finance, Managers | High | Medium |

---

## Requirements Validation Checklist

- [x] Each requirement is clear and unambiguous
- [x] Requirements are testable with acceptance criteria
- [x] Requirements trace to identified stakeholders
- [x] Critical requirements have detailed acceptance criteria
- [x] Requirements are within project scope
- [x] No conflicting requirements within functional set
- [x] Requirements use consistent terminology
- [x] Priority levels are assigned
