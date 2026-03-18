# Assignment 4: Functional Requirements
## Project: HotelHub - Comprehensive Hotel Management System

## Overview
This document defines 12 functional requirements for the HotelHub system. Each requirement includes a clear description, acceptance criteria, and traceability to stakeholders identified in the stakeholder analysis.

---

## FR-1: Room Booking and Search
**Description:** The system shall allow guests to search for available rooms based on dates, room type, and preferences.

**Acceptance Criteria:**
- Search results display within 2 seconds
- Real-time availability shown with color coding (available/booked/maintenance)
- Filters include: date range, room type, price range, amenities
- Calendar view shows blocked dates for each room
- Search results can be sorted by price, rating, or room size

**Traceability:** Addresses Guest concern for easy booking, Front Desk concern for availability visibility

---

## FR-2: Online Check-in/Check-out
**Description:** The system shall enable guests to check in online 24 hours before arrival and check out digitally.

**Acceptance Criteria:**
- Check-in window opens exactly 24 hours before arrival
- Digital key generation for mobile access (where hardware supports)
- Final bill preview available at check-out
- Email receipt automatically sent after check-out
- Check-out available without visiting front desk

**Traceability:** Addresses Guest pain point of long queues, Front Desk workload reduction

---

## FR-3: Housekeeping Task Management
**Description:** The system shall assign and track housekeeping tasks based on room status and priorities.

**Acceptance Criteria:**
- Automatic task generation for check-out rooms
- Mobile interface for housekeeping staff
- Real-time status updates (cleaning in progress, completed, inspected)
- Priority flagging for VIP/urgent rooms
- Supervisor can reassign tasks as needed

**Traceability:** Addresses Housekeeping Staff concerns about task clarity and efficiency

---

## FR-4: Guest Service Requests
**Description:** The system shall allow guests to request services (extra towels, room service, maintenance) via mobile/web.

**Acceptance Criteria:**
- Request categorized by type (housekeeping, maintenance, food)
- Estimated time of arrival/completion shown to guest
- Status tracking: received → assigned → in progress → completed
- Staff notifications for new requests
- Request history visible to guest

**Traceability:** Addresses Guest desire for convenience, Staff need for organized request management

---

## FR-5: Dynamic Pricing Engine
**Description:** The system shall adjust room prices based on occupancy, seasonality, and events.

**Acceptance Criteria:**
- Configurable pricing rules by Manager
- Automatic rate updates across all channels
- Minimum and maximum price boundaries enforced
- Historical data used for future predictions
- Price change history logged for audit

**Traceability:** Addresses Hotel Manager revenue optimization, Marketing competitive positioning

---

## FR-6: Staff Role-Based Access Control
**Description:** The system shall provide different access levels and dashboards based on staff roles.

**Acceptance Criteria:**
- Minimum 5 role types (Admin, Manager, Front Desk, Housekeeping, Finance)
- Granular permissions per module (view/edit/delete)
- Audit log of all user actions
- Single sign-on capability for staff
- New staff accounts created with default role permissions

**Traceability:** Addresses IT Administrator security concerns, Department-specific needs

---

## FR-7: Integrated Billing and Payments
**Description:** The system shall process payments and generate invoices with integration to room charges.

**Acceptance Criteria:**
- Multiple payment methods (credit card, cash, digital wallet)
- Split payment capability for groups
- Automatic posting of room charges to guest folio
- Integration with accounting software export
- Tax calculation based on local regulations

**Traceability:** Addresses Finance Department accuracy needs, Guest payment convenience

---

## FR-8: OTA Integration Management
**Description:** The system shall synchronize room availability and rates with major Online Travel Agencies.

**Acceptance Criteria:**
- Two-way sync with Booking.com, Expedia, Agoda
- Prevents overbooking by updating within 5 minutes
- Mapping of room types across platforms
- Commission tracking per OTA
- Manual override capability for manager

**Traceability:** Addresses Marketing need for rate parity, Manager revenue concerns

---

## FR-9: Maintenance Request and Tracking
**Description:** The system shall allow staff to report and track maintenance issues for rooms and facilities.

**Acceptance Criteria:**
- Photo attachment capability for issues
- Priority assignment (urgent, high, medium, low)
- Assignment to specific maintenance staff
- History log of all repairs by room/asset
- Status tracking: reported → assigned → in progress → resolved

**Traceability:** Addresses Housekeeping pain point of delayed reporting, Manager asset tracking

---

## FR-10: Reporting and Analytics Dashboard
**Description:** The system shall provide customizable reports on occupancy, revenue, and guest satisfaction.

**Acceptance Criteria:**
- Minimum 10 pre-built report templates
- Export formats: PDF, Excel, CSV
- Scheduled report delivery via email
- Visual charts and graphs for trends
- Drill-down capability for detailed data

**Traceability:** Addresses Manager need for insights, Finance reporting requirements

---

## FR-11: Guest Profile Management
**Description:** The system shall maintain guest profiles with preferences, stay history, and loyalty status.

**Acceptance Criteria:**
- Automatic profile creation after first stay
- Preference tracking (room type, amenities, dietary)
- Stay history with spending analysis
- GDPR-compliant data export/deletion
- Loyalty points tracking and redemption

**Traceability:** Addresses Marketing targeting needs, Guest personalization expectations

---

## FR-12: Real-time Notification System
**Description:** The system shall send notifications to guests and staff for key events.

**Acceptance Criteria:**
- Notification types: email, SMS, in-app, push
- Guest notifications: booking confirmation, pre-arrival, check-in ready
- Staff notifications: new booking, guest request, VIP arrival
- Opt-out options for guests
- Notification delivery status tracking

**Traceability:** Addresses Guest expectation for updates, Staff need for alerts

---

## Requirements Traceability Matrix

| Requirement | Guests | Front Desk | Manager | Housekeeping | IT | Finance | Marketing | Restaurant |
|------------|--------|------------|---------|--------------|-----|---------|-----------|------------|
| FR-1 Booking | ✓ | ✓ | | | | | | |
| FR-2 Check-in | ✓ | ✓ | | | | | | |
| FR-3 Housekeeping | | | | ✓ | | | | |
| FR-4 Service Requests | ✓ | ✓ | | ✓ | | | | |
| FR-5 Dynamic Pricing | | | ✓ | | | ✓ | ✓ | |
| FR-6 Access Control | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| FR-7 Billing | ✓ | | ✓ | | | ✓ | | ✓ |
| FR-8 OTA Integration | | | ✓ | | | | ✓ | |
| FR-9 Maintenance | | | ✓ | ✓ | | | | |
| FR-10 Reports | | | ✓ | | | ✓ | ✓ | |
| FR-11 Guest Profiles | ✓ | ✓ | ✓ | | | | ✓ | ✓ |
| FR-12 Notifications | ✓ | ✓ | ✓ | ✓ | | | | ✓ |

---

## Summary
- **Total Functional Requirements:** 12
- **Requirements with Acceptance Criteria:** 12 (100%)
- **Stakeholders Addressed:** All 8 stakeholders covered
