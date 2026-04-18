# Assignment 8 Reflection: State and Activity Modeling

## Challenges in Choosing Granularity

The main challenge was deciding how many states and actions to include. Too few states would oversimplify the object lifecycle (e.g., Room only Available/Booked ignores maintenance). Too many states would make diagrams cluttered. I balanced by focusing on states that directly affect business logic and stakeholder decisions from Assignment 4.

For activity diagrams, the challenge was breaking workflows into atomic steps without becoming overly technical. I kept the level at user/system interaction to align with use case specifications from Assignment 5.

## Aligning Diagrams with Agile User Stories

Each state and activity diagram traces directly to user stories from Assignment 6. For example, the Room state diagram supports US-001 (search rooms) through the Available state, US-004 (online check-in) through Booked→Occupied transition, and US-010 (maintenance reporting) through Occupied→Maintenance.

## Comparing State Diagrams vs. Activity Diagrams

State diagrams focus on the lifecycle of a single object – its possible statuses and the events that cause changes. They answer: "What can happen to this object?" Activity diagrams focus on a process flow – sequences of actions, decisions, and parallel tasks across multiple objects and actors. They answer: "How do we accomplish a goal?"

For HotelHub, state diagrams were essential for objects like Booking and Payment that have complex status rules. Activity diagrams were essential for workflows like Check-in that involve guest, system, and staff interactions.

## Lessons Learned

Modeling dynamic behavior revealed gaps in earlier requirements. For example, the HousekeepingTask state diagram exposed the need for an "Inspected" state after completion – a requirement not explicitly stated in Assignment 4 but critical for quality assurance.

