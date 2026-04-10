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

This visual structure makes it immediately clear where the project stands.

## Work-in-Progress (WIP) Limits

GitHub Projects does not automatically enforce WIP limits, but I will manually enforce:

| Column | WIP Limit | Reason |
|--------|-----------|--------|
| In progress | 3 tasks | Prevents context switching |
| Testing | 2 tasks | Ensures quality focus |

## How the Board Supports Agile Principles

| Agile Principle | How My Board Implements It |
|----------------|---------------------------|
| Individuals and interactions | Assignees show who is responsible |
| Working software | "Testing" column ensures quality |
| Responding to change | "Blocked" column makes impediments visible |
| Continuous delivery | Tasks flow left to right toward "Done" |

## Screenshot

![HotelHub Kanban Board](kanban-board.png)

The screenshot shows my complete board with 16 user stories in the "To do" column, ready for Sprint 1.
