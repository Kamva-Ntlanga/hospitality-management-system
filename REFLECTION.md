# Reflection: Challenges in Balancing Stakeholder Needs


## Introduction

This document reflects on the challenges encountered while balancing the diverse and sometimes conflicting needs of stakeholders during the requirements elicitation process for the Hospitality Management System.

---

## Key Challenges Identified

### Challenge 1: Speed vs Security

**The Conflict:**
- **Hotel Guests** want a fast, frictionless booking and check-in experience with minimal steps
- **IT Administrators** require robust security measures including multi-factor authentication, complex passwords, and session timeouts

**How I Balanced It:**
I addressed this by implementing a tiered security approach:
- First-time users: Standard authentication with email verification
- Returning users: Simplified login with device recognition
- High-risk actions (payment changes, refunds): Require additional verification
- Admin accounts: Full MFA always required

This gives guests speed for regular tasks while maintaining security where it matters most.

---

### Challenge 2: Data Collection vs Privacy

**The Conflict:**
- **Marketing Team** wants extensive guest data for targeted campaigns and analytics
- **Hotel Guests** are concerned about privacy and how their data is used
- **Hotel Managers** need enough data for business intelligence

**How I Balanced It:**
I implemented:
- Explicit consent checkboxes for marketing communications
- Anonymized data for analytics (removing personally identifiable information)
- Clear privacy policy explaining data usage
- Guest portal to view and delete personal data
- Data retention limits (automatically delete after 3 years)

This satisfies marketing needs while respecting guest privacy and complying with GDPR.

---

### Challenge 3: Mobile Access vs Device Costs

**The Conflict:**
- **Housekeeping Staff** need mobile devices to update room status in real-time
- **IT Administrators** have budget constraints for purchasing and maintaining devices
- **Hotel Managers** want efficiency gains without large capital expenditure

**How I Balanced It:**
I proposed a hybrid solution:
- Shared tablets on each floor for staff during shifts
- BYOD (Bring Your Own Device) option with secure container
- Web-based mobile app (no app store deployment costs)
- Device management software for security on shared devices

This provides mobile access while minimizing costs and maintenance overhead.

---

### Challenge 4: Rich Features vs Simplicity

**The Conflict:**
- **Hotel Managers** want extensive features, reports, and analytics
- **Front Desk Staff** need a simple interface for quick tasks during busy check-in times
- **Hotel Guests** want an uncluttered booking experience

**How I Balanced It:**
I designed role-based interfaces:
- Guest portal: Clean, simple with only booking-related functions
- Front desk dashboard: Quick-action buttons for common tasks, advanced features in separate menu
- Manager portal: Full access to reports and configuration
- Customizable layouts for power users

Each user sees only what they need for their role, keeping interfaces clean while preserving functionality.

---

### Challenge 5: Real-time Updates vs System Performance

**The Conflict:**
- **Hotel Managers** want real-time occupancy and revenue dashboards
- **Housekeeping Staff** need instant room status updates
- **IT Administrators** worry about database load from constant updates
- **Performance** requirements demand fast response times

**How I Balanced It:**
I implemented:
- Redis cache for frequently accessed data (room status, availability)
- WebSocket connections for real-time updates to relevant users only
- Database write queuing for non-critical updates
- Dashboard data refreshes every 30 seconds instead of real-time for non-critical metrics
- Read replicas for reporting queries to separate from transactional database

This provides near real-time experience without overwhelming the database.

---

### Challenge 6: OTA Integration vs Control

**The Conflict:**
- **Hotel Managers** want integration with Booking.com, Expedia for maximum bookings
- **IT Administrators** worry about API reliability and security
- **External Partners** need reliable data sync
- **Front Desk Staff** need to see all bookings in one place

**How I Balanced It:**
I designed:
- Bidirectional API with rate limiting
- Queue system for OTA updates to prevent overload
- Manual override capability during API outages
- Unified booking view regardless of source
- Conflict resolution rules (direct booking takes priority)
- Monitoring and alerts for sync failures

This provides integration benefits while maintaining control and reliability.

---

### Challenge 7: Comprehensive Reporting vs Performance

**The Conflict:**
- **Hotel Managers** want detailed reports with historical data
- **Finance Staff** need complex financial reports
- **Performance** requirements demand fast report generation

**How I Balanced It:**
I implemented:
- Read-only database replica for all reporting queries
- Pre-aggregated summary tables for common reports
- Scheduled report generation with email delivery
- Cached results for frequently accessed reports
- Asynchronous report generation for complex queries
- Export options for Excel for custom analysis

This enables rich reporting without impacting transaction performance.

---

## Lessons Learned

### 1. Early Stakeholder Identification is Critical
Identifying all stakeholders early prevents missing important requirements. I initially forgot external partners (OTAs) and had to revise requirements.

### 2. Trade-offs are Inevitable
No system can satisfy every stakeholder perfectly. Clear prioritization based on business value is essential.

### 3. Communication is Key
Understanding the "why" behind stakeholder requests helps find creative solutions that address underlying needs.

### 4. Documentation Matters
Recording decisions and trade-offs helps when stakeholders question why certain choices were made.

### 5. Prototypes Validate Assumptions
Showing stakeholders visual representations of solutions helps confirm understanding before building.

---

## How Requirements Addressed Stakeholder Concerns

| Stakeholder | Key Concern | How Requirements Address It |
|-------------|-------------|----------------------------|
| Hotel Guests | Fast booking | FR-04 (2-second search), FR-05 (quick booking) |
| Front Desk | Efficient check-in | FR-10 (under 3 minutes), NFR-US-01 (intuitive interface) |
| Housekeeping | Mobile updates | FR-13 (task management), NFR-US-02 (mobile responsive) |
| Managers | Real-time data | FR-15 (operational reports), NFR-PF-03 (concurrent users) |
| IT Admin | Security | NFR-SC-01 (encryption), NFR-SC-02 (access control) |
| Finance | Accurate billing | FR-12 (payment processing), FR-16 (financial reports) |

---

## Conclusion

Balancing stakeholder needs requires empathy, creativity, and compromise. The key is understanding that perfect satisfaction for one stakeholder often means disappointment for another. The goal is not to make everyone 100% happy, but to create a system that delivers maximum value within constraints while being transparent about trade-offs.

This assignment reinforced that requirements engineering is as much about negotiation and communication as it is about technical specification.
