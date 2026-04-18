# Assignment 8 Reflection: State and Activity Modeling

## Challenges in Choosing Granularity

The main challenge was deciding how many states and actions to include. Too few states would oversimplify the object lifecycle (e.g., Room only Available/Booked ignores maintenance). Too many states would make diagrams cluttered. I balanced by focusing on states that directly affect business logic and stakeholder decisions from Assignment 4.

For activity diagrams, the challenge was breaking workflows into atomic steps without becoming overly technical. I kept the level at user/system interaction to align with use case specifications from Assignment 5.

## Aligning Diagrams with Agile User Stories

Each state and activity diagram traces directly to user stories from Assignment 6. For example, the Room state diagram supports US-001 (search rooms) through the Available state, US-004 (online check-in) through Booked→Occupied transition, and US-010 (maintenance reporting) through Occupied→Maintenance.

## Comparing State Diagrams vs. Activity Diagrams (Detailed)

### 1. Purpose and Focus

| Aspect | State Diagram | Activity Diagram |
|--------|---------------|------------------|
| **Primary purpose** | Model the lifecycle of a single object | Model the flow of a process or workflow |
| **What it captures** | Possible states an object can be in, transitions between states, and events that trigger transitions | Sequence of actions, decisions, parallel activities, and responsibilities |
| **Perspective** | Time-based – how an object changes over time | Flow-based – how a task moves from start to finish |
| **Example question answered** | "What happens to a Booking after payment?" | "What steps does a guest take to book a room?" |

### 2. Key Elements

| Element | State Diagram | Activity Diagram |
|---------|---------------|------------------|
| **Nodes** | States (rounded rectangles) | Actions (rectangles), decisions (diamonds), start/end (circles) |
| **Arrows** | Transitions triggered by events | Control flow showing sequence |
| **Swimlanes** | Not typically used | Yes – shows which actor does which action |
| **Parallel flows** | Not supported | Yes – forks and joins show concurrent activities |
| **Guard conditions** | Yes (e.g., `[payment valid]`) | Yes (on decision branches) |

### 3. When to Use Each

| Scenario | Use State Diagram | Use Activity Diagram |
|----------|-------------------|----------------------|
| An object has complex status rules | ✅ Yes (e.g., Payment: Pending → Authorized → Captured → Refunded) | ❌ No |
| A process involves multiple actors | ❌ No | ✅ Yes (e.g., Check-in involves Guest, System, Staff) |
| You need to understand all possible object lifecycles | ✅ Yes | ❌ No |
| You need to document a step-by-step user procedure | ❌ No | ✅ Yes |
| Parallel tasks happen simultaneously | ❌ No | ✅ Yes (e.g., Send email + Update inventory at same time) |

### 4. Examples from HotelHub

**State Diagram Example – Booking:**
- States: Pending → Confirmed → CheckedIn → Completed
- Shows lifecycle of a single booking object
- Helps developers understand when a booking can be cancelled (only in Pending or Confirmed, not after CheckedIn)

**Activity Diagram Example – Book Room:**
- Actions: Search → Select → Enter details → Validate → Pay → Confirm
- Shows step-by-step process
- Helps developers understand the exact sequence of user interactions

### 5. Why Both Are Necessary for HotelHub

| Object/Process | Why State Diagram Needed | Why Activity Diagram Needed |
|----------------|-------------------------|----------------------------|
| **Payment** | Must track Pending → Authorized → Captured → Refunded for audit trail | Process payment workflow shows validation, decline handling, receipt generation |
| **Booking** | Must prevent cancellation after check-in | Booking workflow shows guest entry, validation, confirmation email |
| **Maintenance** | Must track OnHold state when parts are needed | Reporting workflow shows photo attachment, priority assignment, technician notification |

### 6. Key Differences Summary Table

| Difference | State Diagram | Activity Diagram |
|------------|---------------|------------------|
| **Number of objects** | One primary object | Multiple objects and actors |
| **Time dimension** | Shows object over time | Shows sequence of actions |
| **Concurrency** | Not represented | Can show parallel tasks |
| **Swimlanes** | No | Yes (responsibility separation) |
| **End states** | Object terminates or returns to initial | Process reaches end node |
| **Best for** | Requirements analysis, database design | Process documentation, UI flow design |

### 7. Practical Insight

In real-world software development:

- **State diagrams** are often used by backend developers to design database state machines and business logic rules. For example, ensuring a "Refunded" payment cannot be "Captured" again.

- **Activity diagrams** are often used by frontend developers and UX designers to map out user journeys and system responses. For example, showing what happens when a guest clicks "Confirm Booking" – including validation, error handling, and success paths.

## Lessons Learned

Modeling dynamic behavior revealed gaps in earlier requirements. For example, the HousekeepingTask state diagram exposed the need for an "Inspected" state after completion – a requirement not explicitly stated in Assignment 4 but critical for quality assurance.

**Word count: ~700 words**
