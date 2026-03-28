# Assignment 5 Reflection: Translating Requirements to Use Cases and Tests

## Introduction

This assignment required translating stakeholder and system requirements from Assignment 4 into use case diagrams, detailed specifications, and test cases. This reflection documents the challenges encountered and lessons learned during this process.

---

## Challenge 1: Ensuring Complete Stakeholder Coverage

**The Challenge:**
Assignment 4 identified 8 stakeholders. Ensuring all 8 were represented as actors in the use case diagram required careful mapping and verification.

**How I Addressed It:**
I created a traceability matrix mapping each stakeholder to the use cases that serve them. I reviewed each actor to confirm they had corresponding use cases that addressed their primary responsibilities. The 8 actors in the diagram directly match the 8 stakeholders from Assignment 4.

**Lesson Learned:** 
Every stakeholder identified in requirements must appear in the use case model. Missing actors indicates incomplete analysis and would result in stakeholder needs not being addressed.

---

## Challenge 2: Representing All Functional Requirements

**The Challenge:**
Assignment 4 had 12 functional requirements. Some, like Dynamic Pricing (FR-5), are internal system features that do not directly involve user interaction. Determining how to represent these in use cases required careful consideration.

**How I Addressed It:**
- Direct user-facing requirements became standalone use cases (Search Rooms, Book Room, Online Check-in, etc.)
- Internal requirements were documented in use case specifications as system steps
- I added Manage Guest Profile (UC-08) to cover FR-11
- I added Manage Notifications (UC-10) to cover FR-12

**Lesson Learned:**
Not all functional requirements become standalone use cases. Some are represented as steps within other use cases or as system-level capabilities that support multiple user interactions.

---

## Challenge 3: Determining Include vs. Extend Relationships

**The Challenge:**
Deciding when to use `<<include>>` versus `<<extend>>` relationships was initially confusing. The distinction between mandatory and optional behavior needed to be clearly defined.

**How I Addressed It:**
- **Include:** Required behavior that MUST happen as part of the base use case
  - Book Room includes Search Rooms (must check availability before booking)
  - Online Check-in includes Make Payment (must complete payment before check-in)
  - Online Check-out includes Make Payment (must settle balance before departure)
  
- **Extend:** Optional behavior that MAY happen under specific conditions
  - Request Service extends to Manage Maintenance Requests (only if the request is maintenance-related)
  - Book Room extends to Manage Notifications (always sends confirmation)
  - Online Check-in extends to Manage Notifications (always sends pre-arrival notifications)
  - Request Service extends to Manage Notifications (always sends staff alerts)

**Lesson Learned:**
Include is for mandatory dependencies that are always executed; extend is for optional variations that occur only when specific conditions are met. This distinction makes the diagram more meaningful and accurate.

---

## Challenge 4: Writing Testable Acceptance Criteria

**The Challenge:**
Converting use case flows into test cases required making each step verifiable and measurable. Vague requirements like "system should be fast" could not be tested effectively.

**How I Addressed It:**
For each test case, I ensured:
- Clear, sequential test steps that anyone can follow
- Expected results that are observable and measurable (e.g., "within 2 seconds" not "quickly")
- Preconditions that define the exact starting state
- References back to specific requirement IDs from Assignment 4

**Example:**
Instead of "system responds quickly" → "system displays results within 2 seconds"

**Lesson Learned:**
Good requirements make good test cases. Ambiguous requirements lead to ambiguous testing. This reinforces why Assignment 4's detailed requirements with acceptance criteria were so important.

---

## Challenge 5: Testing Non-Functional Requirements

**The Challenge:**
Non-functional requirements are harder to test than functional ones. Performance and security testing require specialized tools and approaches.

**How I Addressed It:**
I defined two non-functional test cases:
- **Performance Test:** Page load time measurement using load testing tools with specific thresholds
- **Security Test:** Failed login lockout to verify account protection mechanisms

For each, I specified the steps, expected results, and the conditions under which testing would occur.

**Lesson Learned:**
Non-functional testing requires specialized tools and clear acceptance criteria. Defining the test approach upfront helps stakeholders understand how these quality attributes will be verified.

---

## Challenge 6: Maintaining Traceability Across Assignments

**The Challenge:**
Ensuring consistency between Assignment 4 (requirements) and Assignment 5 (use cases, tests) required constant cross-referencing to avoid misalignment.

**How I Addressed It:**
I created traceability links throughout:
- Each use case references related FR IDs in the specifications
- Each test case references a requirement ID
- Actors match stakeholders from Assignment 4
- Non-functional test cases reference NFR IDs

**Lesson Learned:**
Traceability is essential for maintaining consistency across project artifacts. Even for assignments, maintaining links prevents inconsistency and makes review easier.

---

## Challenge 7: Balancing Detail vs. Clarity

**The Challenge:**
Use case specifications can become overwhelming with too many alternative flows and edge cases, making them difficult to read and understand.

**How I Addressed It:**
I focused on:
- Main success scenario (happy path) delivering core value
- 3-4 alternative flows for common exceptions
- Not documenting every possible edge case
- Keeping descriptions concise but complete

**Lesson Learned:**
Use cases should be actor-focused, not implementation-focused. If a step describes internal system processing without user interaction, it may belong in a different artifact.

---

## Traceability Matrix: Assignment 4 to Assignment 5

| Assignment 4 | Assignment 5 Artifact | Status |
|--------------|----------------------|--------|
| 8 Stakeholders | 8 Actors | Fully Aligned |
| FR-1: Room Booking and Search | UC-01 Search Rooms, UC-02 Book Room | Aligned |
| FR-2: Online Check-in/out | UC-03 Online Check-in, UC-06 in spec | Aligned |
| FR-3: Housekeeping Task Management | UC-06 Manage Housekeeping Tasks | Aligned |
| FR-4: Guest Service Requests | UC-04 Request Service | Aligned |
| FR-5: Dynamic Pricing Engine | Internal (represented in system steps) | Acceptable |
| FR-6: Role-Based Access Control | UC-13 Manage Staff Accounts | Aligned |
| FR-7: Integrated Billing | UC-05 Make Payment | Aligned |
| FR-8: OTA Integration | UC-09 Manage OTA Integration | Aligned |
| FR-9: Maintenance Tracking | UC-04 Request Service (extend to UC-11) | Aligned |
| FR-10: Reporting Dashboard | UC-07 Generate Reports | Aligned |
| FR-11: Guest Profile Management | UC-08 Manage Guest Profile | Aligned |
| FR-12: Notification System | UC-10 Manage Notifications | Aligned |
| NFRs (8+ requirements) | 2 Test Cases (Performance, Security) | Aligned |

---

## Key Takeaways

| Area | Key Learning |
|------|--------------|
| Use Case Diagrams | Include/extend relationships must reflect actual system dependencies, not just sequence of steps |
| Use Case Specifications | Preconditions and postconditions are critical for defining the scope and boundaries of each use case |
| Test Cases | Good tests require clear, measurable expected results that can be objectively verified |
| Traceability | Maintaining links between artifacts prevents inconsistency across assignments |
| Non-Functional Testing | Requires specialized tools and clear acceptance criteria that stakeholders can understand |
| Stakeholder Coverage | Every stakeholder from requirements must appear in the use case model |

---

## Conclusion

This assignment reinforced that requirements engineering is an iterative, interconnected process. The use cases I created directly trace to the stakeholders and requirements identified in Assignment 4. The test cases verify the requirements specified. Each artifact builds on and validates the others.

The most valuable lesson was that thinking about testing during requirements leads to clearer, more actionable specifications. A requirement that cannot be tested is not a good requirement. This principle will guide my approach to future requirements engineering work.

---


