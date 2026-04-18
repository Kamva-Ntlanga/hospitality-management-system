# Assignment 8 Reflection: State and Activity Modeling

## Challenges in Choosing Granularity

The main challenge was deciding how many states and actions to include. Too few states would oversimplify the object lifecycle (e.g., Room only Available/Booked ignores maintenance). Too many states would make diagrams cluttered. I balanced by focusing on states that directly affect business logic and stakeholder decisions from Assignment 4.

For activity diagrams, the challenge was breaking workflows into atomic steps without becoming overly technical. I kept the level at user/system interaction to align with use case specifications from Assignment 5.

## Aligning Diagrams with Agile User Stories

Each state and activity diagram traces directly to user stories from Assignment 6. For example, the Room state diagram supports US-001 (search rooms) through the Available state, US-004 (online check-in) through Booked→Occupied transition, and US-010 (maintenance reporting) through Occupied→Maintenance.

## Comparing State Diagrams vs. Activity Diagrams

State diagrams and activity diagrams serve different purposes in system modeling:

| Aspect | State Diagram | Activity Diagram |
|--------|---------------|------------------|
| **Focus** | Lifecycle of a single object | Flow of a process or workflow |
| **Question answered** | What states can an object be in and how does it change? | What steps are needed to complete a task? |
| **Key elements** | States (rounded rectangles), transitions (arrows), events | Actions, decisions (diamonds), start/end nodes, swimlanes |
| **Example from HotelHub** | Room: Available → Booked → Occupied → Available | Book Room: Search → Select → Enter details → Validate → Pay → Confirm |
| **Use case** | Understanding how a booking or payment status changes over time | Documenting step-by-step user interactions |

**Why both are needed:** State diagrams ensure we don't miss object lifecycles (e.g., a payment must go from Pending → Authorized → Captured). Activity diagrams ensure we capture the correct sequence of user actions and system responses. Together, they provide a complete dynamic model of the system.

## Lessons Learned

Modeling dynamic behavior revealed gaps in earlier requirements. For example, the HousekeepingTask state diagram exposed the need for an "Inspected" state after completion – a requirement not explicitly stated in Assignment 4 but critical for quality assurance.


