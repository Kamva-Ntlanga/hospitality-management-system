# Stakeholder Analysis: Hospitality Management System

**Author:** Your Full Name
**Date:** March 18, 2026
**Course:** Software Engineering
**Assignment:** 4 - Stakeholder and System Requirements Documentation

## Overview

This document identifies and analyzes the key stakeholders for the Hospitality Management System. Each stakeholder's role, concerns, pain points, and success metrics are documented to ensure the system requirements address real user needs.

---

## Stakeholder Analysis Table

| # | Stakeholder | Role | Key Concerns | Pain Points | Success Metrics |
|---|-------------|------|--------------|-------------|-----------------|
| 1 | **Hotel Guests** | End-users who book rooms, check in/out, and receive services during their stay | • Easy and fast booking process<br>• Accurate room availability<br>• Secure payment processing<br>• Quick check-in/out<br>• Ability to make special requests | • Double-bookings causing reservation issues<br>• Long check-in queues upon arrival<br>• No confirmation emails leading to uncertainty<br>• Difficulty modifying or canceling bookings<br>• Hidden fees not shown during booking | • 95% of guests rate booking process 4/5 stars<br>• Check-in time under 3 minutes<br>• 50% reduction in booking-related complaints<br>• 30% increase in online bookings |
| 2 | **Front Desk Staff** | Handle check-in/check-out, manage reservations, assist guests, and coordinate with housekeeping | • Quick access to guest information<br>• Efficient check-in/out workflows<br>• Real-time room status updates<br>• Easy reservation modifications<br>• Clear billing and payment processing | • Manual paperwork slowing down check-ins<br>• Calling housekeeping to check room status<br>• Guests waiting while system loads<br>• Difficult to find past guest history<br>• Payment processing errors | • Check-in time reduced from 10 to 3 minutes<br>• 100% accurate room assignments<br>• 40% faster guest service resolution<br>• Zero manual data entry errors |
| 3 | **Hotel Managers** | Oversee daily operations, set room rates, analyze occupancy, generate reports, and make strategic decisions | • Real-time occupancy and revenue data<br>• Demand forecasting for pricing<br>• Staff performance tracking<br>• Identifying peak/off-peak patterns<br>• Integration with OTAs (Booking.com, Expedia) | • Waiting days for occupancy reports<br>• Manual Excel work for revenue analysis<br>• No visibility into future demand<br>• Channel conflicts with online travel agencies<br>• Difficulty tracking housekeeping efficiency | • Real-time dashboard with <5 second refresh<br>• 20% increase in revenue through dynamic pricing<br>• 100% accurate nightly audit reports<br>• 15% improvement in staff productivity |
| 4 | **Housekeeping Staff** | Clean rooms, update room status, report maintenance issues, and prepare rooms for new guests | • Clear daily task lists<br>• Quick room status updates<br>• Ability to report maintenance issues<br>• Prioritization of check-out vs stayover rooms<br>• Mobile-friendly interface | • Walking to front desk to update room status<br>• Unclear which rooms need priority cleaning<br>• Double-work when rooms are incorrectly marked dirty<br>• No way to report maintenance issues digitally<br>• Paper lists getting lost | • Room turnover time reduced by 25%<br>• 100% accurate room status updates<br>• 50% faster maintenance issue reporting<br>• Zero missed rooms due to lost paper lists |
| 5 | **IT Administrators** | Manage system access, maintain servers, ensure security, handle backups, and troubleshoot issues | • System uptime and reliability<br>• User access control and permissions<br>• Data backup and recovery<br>• Security against breaches<br>• Easy deployment of updates | • Frequent system crashes during peak hours<br>• Difficulty resetting user passwords<br>• Manual backup processes<br>• No audit logs for troubleshooting<br>• Complex server configuration | • 99.9% system uptime during operational hours<br>• Automated daily backups with 15-minute RPO<br>• 30-minute average issue resolution time<br>• Zero security breaches |
| 6 | **Finance/Accounting Staff** | Manage billing, process payments, handle refunds, reconcile accounts, and generate financial reports | • Accurate invoice generation<br>• Integration with accounting software<br>• Tax calculation compliance<br>• Refund and chargeback handling<br>• Revenue reconciliation | • Manual invoice creation taking hours<br>• Discrepancies between bookings and payments<br>• Complex tax calculations for different regions<br>• No payment failure notifications<br>• Time-consuming month-end reconciliation | • 100% accurate automated invoices<br>• 50% reduction in billing discrepancies<br>• Automated tax calculations with 99.9% accuracy<br>• 80% faster month-end closing |
| 7 | **Marketing Team** | Promote hotel, manage online presence, analyze booking trends, and run promotional campaigns | • Understanding booking sources/channels<br>• Guest demographic data<br>• Seasonal booking patterns<br>• Campaign performance tracking<br>• Integration with CRM | • No visibility into which channels drive bookings<br>• Limited guest data for targeted marketing<br>• Unable to track promotion effectiveness<br>• Manual data extraction for reports<br>• No integration with email marketing tools | • 25% increase in direct bookings<br>• 40% better targeting of marketing campaigns<br>• Real-time channel performance dashboard<br>• 50% improvement in campaign ROI |
| 8 | **External Partners (OTAs)** | Third-party booking platforms (Booking.com, Expedia, Agoda) that need real-time availability sync | • Real-time room availability updates<br>• Accurate rate synchronization<br>• Confirmed booking delivery<br>• No overbookings from multiple channels<br>• API reliability | • Delayed availability causing rejected bookings<br>• Rate discrepancies leading to guest complaints<br>• Lost booking data during API failures<br>• Double-bookings from channel conflicts<br>• Manual rate updates across platforms | • 100% real-time availability sync<br>• Zero overbookings from channel conflicts<br>• 99.9% API uptime<br>• Instant booking confirmation delivery |

---

## Stakeholder Prioritization Matrix

| Stakeholder | Power/Influence | Interest | Priority Level |
|-------------|-----------------|----------|----------------|
| Hotel Guests | High | High | **Critical** |
| Hotel Managers | High | High | **Critical** |
| Front Desk Staff | Medium | High | **High** |
| IT Administrators | High | Medium | **High** |
| Housekeeping Staff | Low | High | **Medium** |
| Finance/Accounting | Medium | Medium | **Medium** |
| Marketing Team | Low | Medium | **Low** |
| External Partners | Medium | Low | **Low** |

---

## Stakeholder-Requirement Traceability Matrix

| Requirement ID | Requirement Description | Primary Stakeholder(s) | Secondary Stakeholder(s) |
|----------------|------------------------|------------------------|--------------------------|
| FR-01 | Online room search | Hotel Guests | Marketing |
| FR-02 | Booking management | Hotel Guests, Front Desk | Managers |
| FR-03 | Room status updates | Housekeeping, Front Desk | Managers |
| FR-04 | Payment processing | Guests, Finance | Front Desk |
| FR-05 | Reporting dashboard | Managers, Finance | Marketing |
| FR-06 | User access control | IT Admin | All staff |
| FR-07 | OTA integration | Managers, External Partners | IT Admin |
| FR-08 | Check-in/out workflow | Front Desk, Guests | Housekeeping |
| FR-09 | Maintenance requests | Housekeeping, Maintenance | Managers |
| FR-10 | Guest profile management | Front Desk, Marketing | Managers |

---

## Key Stakeholder Conflicts and Trade-offs

| Conflicting Stakeholders | Issue | Proposed Balance |
|--------------------------|-------|------------------|
| Guests (fast booking) vs IT Admin (security) | Guests want 1-click booking; IT needs security checks | Implement 2FA only for first-time users; return guests get streamlined process |
| Managers (detailed data) vs Guests (privacy) | Managers want guest data for analytics; guests want privacy | Anonymize data for analytics; obtain consent for marketing |
| Housekeeping (mobile app) vs IT Admin (device cost) | Housekeeping needs mobile devices; IT has budget constraints | Provide shared tablets per floor; implement BYOD policy with security |
| Front Desk (quick check-in) vs Finance (payment verification) | Front desk wants instant check-in; Finance needs payment confirmation | Real-time payment verification with cached results for returning guests |

---

## Stakeholder Validation Checklist

- [x] All identified stakeholders interact with or are impacted by the system
- [x] Each stakeholder has clearly defined role
- [x] Concerns are specific and actionable
- [x] Pain points reflect real-world frustrations
- [x] Success metrics are measurable
- [x] Stakeholder conflicts are identified
- [x] Requirements can be traced back to stakeholders
