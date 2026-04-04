# Assignment 6: Agile User Stories, Backlog, and Sprint Planning

## Project: Hospitality Management System (HotelHub)

---

## Part 1: User Stories (16 Stories)

| Story ID | User Story | Acceptance Criteria | Priority |
|----------|------------|---------------------|----------|
| US-001 | As a Hotel Guest, I want to search for available rooms by date and room type so that I can find accommodation that meets my needs. | 1. Search results within 2 seconds<br>2. Shows room type, price, availability<br>3. Filter by date and room type<br>4. Error when no rooms | High |
| US-002 | As a Hotel Guest, I want to book a room after searching so that I can secure my accommodation. | 1. Select room from results<br>2. Show booking summary<br>3. Require name, email, phone<br>4. Send confirmation email | High |
| US-003 | As a Hotel Guest, I want to make payment for my booking so that my reservation is confirmed. | 1. Enter credit card details<br>2. Validate payment info<br>3. Process payment<br>4. Generate receipt | High |
| US-004 | As a Hotel Guest, I want to complete online check-in 24 hours before arrival so that I can avoid waiting at the front desk. | 1. Check-in button 24hrs before<br>2. Confirm guest details<br>3. Generate digital key<br>4. Send confirmation | Medium |
| US-005 | As a Hotel Guest, I want to request services like extra towels or room service so that I can get assistance without calling reception. | 1. Select service category<br>2. Add instructions<br>3. Show estimated time<br>4. Notify staff | Medium |
| US-006 | As a Front Desk Staff member, I want to view and manage housekeeping tasks so that I can coordinate room cleaning efficiently. | 1. View rooms needing cleaning<br>2. Priority rooms shown first<br>3. Mark In Progress/Completed<br>4. Auto-update room status | Medium |
| US-007 | As a Front Desk Staff member, I want to process walk-in check-ins so that I can accommodate guests without prior reservations. | 1. Search available rooms<br>2. Create booking<br>3. Process payment<br>4. Generate room key | High |
| US-008 | As a Hotel Manager, I want to generate occupancy reports so that I can track hotel performance. | 1. Select date range<br>2. Show occupancy % and nights sold<br>3. Export as PDF<br>4. Compare to previous period | Low |
| US-009 | As a Hotel Manager, I want to view a dashboard with key metrics so that I can monitor hotel operations in real-time. | 1. Show current occupancy<br>2. Show today's check-ins/outs<br>3. Show daily revenue<br>4. Update every 5 minutes | High |
| US-010 | As a Housekeeping Staff member, I want to report maintenance issues from my mobile device so that maintenance team can address problems quickly. | 1. Select room number<br>2. Describe issue<br>3. Attach photo<br>4. Create maintenance request | Low |
| US-011 | As a Marketing Team member, I want to sync room availability with Booking.com so that inventory is consistent across all channels. | 1. Initiate manual sync<br>2. Show last sync timestamp<br>3. Show confirmation<br>4. Show error if fails | Low (Deferred) |
| US-012 | As an IT Administrator, I want to manage staff accounts with role-based permissions so that staff only access what they need. | 1. Create new staff accounts<br>2. Assign roles<br>3. Disable accounts<br>4. Role-based permissions | Low |
| US-013 | As a Finance Department user, I want to generate financial summary reports so that I can reconcile revenue at month-end. | 1. Select date range<br>2. Show revenue by category<br>3. Show payment method breakdown<br>4. Export to Excel | Medium |
| US-014 | As a Hotel Guest, I want to view my booking history so that I can track my past and upcoming stays. | 1. See past bookings<br>2. See upcoming bookings<br>3. Show dates, room type, price<br>4. Click for details | Low |
| US-015 | As a Hotel Guest, I want to manage my profile with preferences so that I don't have to re-enter information each time. | 1. Update name, email, phone<br>2. Save room preferences<br>3. Save dietary preferences<br>4. Auto-populate future bookings | Low |
| US-016 | As a System Admin, I want to encrypt all guest data with AES-256 so that security compliance is met. | 1. Encrypt data at rest<br>2. TLS 1.3 for data in transit<br>3. Separate encryption keys<br>4. No plaintext in logs | High |

---

## Part 2: Product Backlog (MoSCoW Prioritized)

| Story ID | User Story | MoSCoW Priority | Story Points | Dependencies |
|----------|------------|-----------------|--------------|--------------|
| US-001 | Search for available rooms | Must-have | 3 | None |
| US-002 | Book a room | Must-have | 5 | US-001 |
| US-003 | Make payment for booking | Must-have | 5 | US-002 |
| US-007 | Process walk-in check-ins | Must-have | 3 | US-001, US-002 |
| US-009 | View dashboard with key metrics | Must-have | 3 | None |
| US-016 | Encrypt all guest data | Must-have | 2 | None |
| US-004 | Online check-in | Should-have | 3 | US-002, US-003 |
| US-005 | Request services | Should-have | 3 | US-004 |
| US-006 | Manage housekeeping tasks | Should-have | 3 | US-002 |
| US-013 | Generate financial reports | Should-have | 3 | US-003 |
| US-008 | Generate occupancy reports | Could-have | 2 | US-009 |
| US-010 | Report maintenance issues | Could-have | 2 | US-006 |
| US-012 | Manage staff accounts | Could-have | 3 | None |
| US-014 | View booking history | Could-have | 2 | US-002 |
| US-015 | Manage profile with preferences | Could-have | 2 | US-002 |
| US-011 | Sync with Booking.com | Won't-have | 5 | US-001 |

### Justification for Must-have Prioritization

These 6 stories are critical for the system to function as a basic hotel management system:

| Story | Justification |
|-------|---------------|
| US-001 | Without search, guests cannot find rooms - core functionality |
| US-002 | Without booking, no reservations can be made - core functionality |
| US-003 | Without payment, no revenue can be collected - business critical |
| US-007 | Front desk cannot serve walk-in guests without this - operational critical |
| US-009 | Manager cannot monitor operations without dashboard - management critical |
| US-016 | Security compliance is mandatory - legal/regulatory requirement |

These align with stakeholder success metrics from Assignment 4.

---

## Part 3: Sprint Plan (2-Week Sprint)

### Sprint Goal

**"Implement core booking functionality allowing guests to search for rooms, make reservations, complete payments, and enabling front desk staff to process walk-in check-ins with a basic management dashboard."**

### Sprint Duration: 2 Weeks (10 Working Days)

### Sprint Backlog (6 Stories)

| Story ID | User Story | Story Points | Tasks | Effort (Hours) |
|----------|------------|--------------|-------|-----------------|
| US-001 | Search for available rooms | 3 | Create room schema, search API, date validation, search UI, connect frontend | 24 |
| US-002 | Book a room | 5 | Create booking schema, booking API, confirmation page, email service, validation | 40 |
| US-003 | Make payment | 5 | Integrate payment gateway, payment API, payment form, receipt generation, status tracking | 40 |
| US-007 | Walk-in check-ins | 3 | Staff dashboard, room search, walk-in booking, on-the-spot payment, key generation | 24 |
| US-009 | Manager dashboard | 3 | Dashboard UI, metrics API, occupancy logic, check-ins/outs display, auto-refresh | 16 |
| US-016 | Data encryption | 2 | App-level encryption, DB encryption, TLS setup, key management, encryption testing | 16 |

**Total Story Points:** 21

**Total Estimated Hours:** 160

**Team Capacity:** 2 developers × 80 hours = 160 hours

### Sprint Timeline (10 Days)

| Day | Focus | Stories Worked On |
|-----|-------|-------------------|
| Day 1 | Setup & Database | US-001, US-002, US-016 |
| Day 2 | Search functionality | US-001 |
| Day 3 | Booking backend | US-002 |
| Day 4 | Booking frontend | US-002 |
| Day 5 | Payment integration | US-003 |
| Day 6 | Payment UI & receipt | US-003 |
| Day 7 | Walk-in check-in | US-007 |
| Day 8 | Walk-in payment & key | US-007 |
| Day 9 | Manager dashboard | US-009 |
| Day 10 | Testing & Bug fixes | All stories |

### Definition of Done

- [ ] Code complete and reviewed
- [ ] All acceptance criteria met
- [ ] Tests pass
- [ ] Deployed to staging
- [ ] Documentation updated

---

## Part 4: GitHub Tools Used

### GitHub Issues Created

| Issue # | Story ID | Title | Labels | Milestone |
|---------|----------|-------|--------|-----------|
| #1 | US-001 | Search for available rooms | user-story, must-have, high-priority | Sprint 
