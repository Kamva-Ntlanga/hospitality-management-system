# Assignment 7: Kanban Board Explanation

## What is a Kanban Board?

In my own words, **a Kanban board is a visual project management tool that helps teams see the flow of their work at a glance. It uses cards to represent tasks and columns to show each task's stage in a process, from "Not Started" to "Completed".**

## How My HotelHub Kanban Board Visualizes Workflow

My board has 5 columns, each representing a stage in the development process:

| Column | Purpose |
|--------|---------|
| **To do** | Tasks that are planned but not yet started |
| **In progress** | Tasks currently being worked on (developer actively coding) |
| **Testing** | Completed code waiting for quality assurance |
| **Done** | Fully completed and verified tasks |
| **Blocked** | Tasks that cannot proceed due to an issue or dependency |

This visual structure makes it immediately clear where the project stands. A manager can look at the board and know exactly what is delayed, what is being worked on, and what is finished.

## Work-in-Progress (WIP) Limits

GitHub Projects does not automatically enforce WIP limits, but I will manually enforce the following limits to prevent bottlenecks:

| Column | WIP Limit | Reason |
|--------|-----------|--------|
| In progress | 3 tasks maximum | Too many concurrent tasks causes context switching and delays |
| Testing | 2 tasks maximum | Quality assurance needs focused attention; limit prevents rushed testing |

If a column exceeds its limit, the team must finish or move a task before starting a new one. This ensures work flows smoothly through the system.

## How the Board Supports Agile Principles

| Agile Principle | How My Board Implements It |
|----------------|---------------------------|
| **Individuals and interactions** | The board shows who is assigned to each task (e.g., @Kamva-Ntlanga), promoting collaboration |
| **Working software** | The "Testing" column ensures quality before marking as "Done" |
| **Customer collaboration** | Stakeholders can view the board to see progress without asking for status reports |
| **Responding to change** | The "Blocked" column makes impediments visible so they can be resolved quickly |
| **Continuous delivery** | Tasks flow from left to right; "Done" items are ready for deployment |
| **Simplicity** | The board has only 5 columns, avoiding unnecessary complexity |

## Automation Rules Enabled

To ensure the board reflects real-time progress without manual updates, I enabled the following built-in GitHub workflows:

| Workflow Name | Function | How It Helps Agile |
|---------------|----------|--------------------|
| **Item added to project** | When a new issue is created, it is automatically added to the "To do" column | Reduces manual admin; ensures all tasks are captured |
| **Item closed** | When an issue is closed (e.g., via a merged pull request), it automatically moves to "Done" | Keeps the board synchronized with actual development work |
| **Pull request merged** | When a pull request linked to an issue is merged, the issue is automatically closed | Automates the completion step, saving time |

## Automation Testing Results

I tested all three workflows to confirm they work correctly:

| Test | Steps Performed | Expected Result | Actual Result | Status |
|------|----------------|----------------|---------------|--------|
| **Item added to project** | Created a new test issue | Issue appears in "To do" column automatically | Issue appeared in "To do" within 5 seconds | ✅ Pass |
| **Item closed** | Closed an existing issue from the "To do" column | Issue moves to "Done" column automatically | Issue moved to "Done" column | ✅ Pass |
| **Pull request merged** | Created a PR with "Closes #X" and merged it | Linked issue closes and moves to "Done" | Issue closed and appeared in "Done" | ✅ Pass |

**Evidence Screenshots:**
- Main board with all columns and labels: ![HotelHub Kanban Board](kanban-board.png)
- Workflows page showing enabled rules: [workflows-enabled.png](images/screenshot.png)
- Issues + labels: ![issues.png](images/screenshot.png)

## Screenshot of My Kanban Board

![HotelHub Kanban Board](kanban-board.png)

The screenshot above shows my complete HotelHub Development Kanban board with all 16 user stories from Assignment 6 loaded into the "To do" column. Each issue has labels (must-have, should-have, etc.) and is assigned to me as the developer. The "Testing" and "Blocked" columns are custom additions that support quality assurance and issue tracking.

## Conclusion

My Kanban board provides full visibility into the HotelHub project's workflow, enforces WIP limits to prevent bottlenecks, and uses automation to keep the board accurate with minimal manual effort. This aligns perfectly with Agile principles of transparency, continuous delivery, and adaptability.
