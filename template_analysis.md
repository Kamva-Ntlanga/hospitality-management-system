# Assignment 7: Template Analysis and Justification

## Project: Hospitality Management System (HotelHub)

---

## 1.1 Detailed Template Comparison Table

GitHub Projects offers several built-in templates. Below is a comprehensive comparison of **4 templates** based on 8 evaluation criteria relevant to the HotelHub project.

| Evaluation Criteria | Basic Kanban | Automated Kanban | Bug Triage | Team Planning |
|---------------------|--------------|------------------|------------|----------------|
| **Default Columns** | To do, In progress, Done | To do, In progress, Done | Needs triage, High priority, Low priority, Close | To do, In progress, Done |
| **Automation Features** | None. Cards must be moved manually. | **High.** New issues auto-add to "To do". When PR opened, card auto-moves to "In progress". When PR merged, auto-moves to "Done". | None. Manual triage only. | None. Manual movement only. |
| **Customisation Flexibility** | High - can add/remove columns | High - can add/remove columns | Medium - designed for bug workflow | High - can add/remove columns |
| **Integration with Issues** | Manual linking only | **Automatic** linking and status sync | Manual linking only | Manual linking only |
| **Suitability for Sprint Planning** | Low - no automation to reflect progress | **High** - automation mirrors real development activity | Very Low - only for bugs | Medium - good for roadmap but not daily sprints |
| **Work-in-Progress Visibility** | Good - columns show status | **Excellent** - columns show status + automation keeps it accurate | Good - priority columns help focus | Good - columns show status |
| **Best Use Case** | Simple projects, small teams, beginners | **Agile development teams using GitHub** | Bug tracking and issue triage | High-level project roadmaps, team planning meetings |
| **Learning Curve** | Very low | Low - automation is intuitive | Low | Very low |

---

## 1.2 Evaluation of Each Template Against HotelHub Requirements

### Template 1: Basic Kanban

**Description:** The simplest template with three columns: To do, In progress, Done. No automation.

**Pros for HotelHub:**
- Very easy to set up and understand
- No complex features to learn

**Cons for HotelHub:**
- **No automation** means every status update requires manual drag-and-drop
- In a busy sprint with 6+ active tasks, manual updates become tedious
- Risk of board becoming outdated if developer forgets to move cards
- Does not leverage GitHub's powerful Issue-PR integration

**Verdict:** Too basic for a project that already has 16 well-defined issues and a clear sprint plan. Would waste time on manual admin.

---

### Template 2: Automated Kanban

**Description:** Same three columns as Basic Kanban but with built-in automation that syncs with Issues and Pull Requests.

**Automation Rules (important for justification):**
1. When a new Issue is created → automatically added to "To do" column
2. When a Pull Request linked to an Issue is opened → Issue moves to "In progress"
3. When the Pull Request is merged → Issue moves to "Done"

**Pros for HotelHub:**
- **Reduces manual work** - developer focuses on coding, not board maintenance
- **Keeps board accurate** - status reflects actual GitHub activity
- **Perfect for solo developer** - one person wearing all hats benefits from automation
- **Aligns with Agile** - real-time visibility without extra meetings
- **Integrates seamlessly** with Issues already created in Assignment 6

**Cons for HotelHub:**
- Requires discipline to link Pull Requests to Issues (good practice anyway)
- Automation only triggers on PR events, not on task splitting

**Verdict:** **Best fit.** The automation directly supports the sprint plan from Assignment 6, where 6 stories are being developed in Sprint 1. The developer can simply open PRs and the board stays updated.

---

### Template 3: Bug Triage

**Description:** Specialised template for managing incoming bug reports with columns: Needs triage, High priority, Low priority, Close.

**Pros for HotelHub:**
- Good if the project had many bug reports

**Cons for HotelHub:**
- **Not designed for feature development** - the HotelHub project is building new features, not primarily fixing bugs
- Columns (High priority, Low priority) do not map to development workflow (coding, testing, done)
- Cannot track progress of user stories through completion
- No "In progress" or "Done" columns for feature work

**Verdict:** Completely unsuitable. HotelHub needs a development board, not a bug tracker.

---

### Template 4: Team Planning

**Description:** Similar to Basic Kanban but intended for higher-level planning, often used with milestones.

**Pros for HotelHub:**
- Good for roadmap visualisation
- Can group issues by milestone

**Cons for HotelHub:**
- **No automation** - same problem as Basic Kanban
- Designed for planning meetings, not daily development tracking
- Would require manual updates for every status change
- Does not reflect real-time development progress

**Verdict:** Suitable for initial planning but not for sprint execution. The HotelHub project already has milestones (Sprint 1, 2, 3) in GitHub; a board with automation is better for tracking work during the sprint.

---

## 1.3 Justification for Selected Template: Automated Kanban

After careful evaluation of all 4 templates against the HotelHub project's specific needs, **I have selected the Automated Kanban template.**

### Justification Point 1: Alignment with Agile Methodology

The HotelHub project follows Agile principles as established in Assignment 6 (sprint planning, user stories, backlog prioritisation). Agile teams need **real-time visibility** into work status without administrative overhead. The Automated Kanban template's automation rules ensure that:

- When a developer starts work and opens a Pull Request, the Issue automatically moves to "In progress"
- When work is completed and the PR is merged, the Issue automatically moves to "Done"

This creates a **live, accurate picture** of the sprint without requiring the developer to remember to drag cards. This directly supports the Agile value of "working software over comprehensive documentation" by reducing process friction.

### Justification Point 2: Supports the Sprint Plan from Assignment 6

In Assignment 6, Sprint 1 was planned with 6 user stories:

| Story ID | Title | Story Points |
|----------|-------|--------------|
| US-001 | Search for available rooms | 3 |
| US-002 | Book a room | 5 |
| US-003 | Make payment | 5 |
| US-007 | Process walk-in check-ins | 3 |
| US-009 | View dashboard | 3 |
| US-016 | Encrypt guest data | 2 |

**Total: 21 story points**

The Automated Kanban template allows these 6 issues to be placed in the "To do" column at sprint start. As the developer works on each issue, opening a Pull Request automatically moves it to "In progress". This provides **instant visual feedback** on sprint progress without any manual board management.

### Justification Point 3: Integration with Existing GitHub Issues

Assignment 6 already created 16 GitHub Issues with:
- Detailed acceptance criteria
- Task checklists
- Labels (must-have, should-have, could-have)
- Milestones (Sprint 1, Sprint 2, Sprint 3)

The Automated Kanban template **automatically pulls these issues** into the board when they are created. No double-entry or manual linking required. This seamless integration saves significant time and ensures consistency between the issue tracker and the project board.

### Justification Point 4: Scalability for Future Sprints

The HotelHub project has 3 sprints planned (Assignment 6). The Automated Kanban template scales easily:

- **Sprint 1 (current):** 6 issues in "To do" column
- **Sprint 2 (future):** Additional issues can be added to the board and moved into "To do" when Sprint 2 begins
- **Sprint 3 (future):** Same pattern

The automation continues to work for all sprints without reconfiguration. This makes the template suitable for the entire project duration.

### Justification Point 5: Industry Best Practice

Automated Kanban boards are widely used in professional software development. Companies like GitHub, Microsoft, and Netflix use similar workflows where:

- Issues represent work units
- Pull Requests represent work in progress
- Merges represent completion

By using the Automated Kanban template, the HotelHub project **mirrors real-world industry practices**, which is a key learning objective of this course.

### Justification Point 6: Addressing Stakeholder Needs from Assignment 4

Recall the stakeholder concerns from Assignment 4:

| Stakeholder | Concern | How Automated Kanban Addresses It |
|-------------|---------|----------------------------------|
| Hotel Manager | Real-time visibility into progress | Board shows exactly what is done, in progress, or to do at any moment |
| Front Desk Staff | Knowing when features are ready | "Done" column provides clear signal of completed work |
| IT Administrator | Tracking development activity | Automation provides audit trail of when work started and finished |

The board is not just a developer tool; it provides transparency to all stakeholders about project status.

---

## 1.4 Summary Table of Evaluation Scores

| Template | Automation | Integration | Suitability for Sprints | Fit for HotelHub | Score (1-5) |
|----------|------------|-------------|------------------------|------------------|-------------|
| Basic Kanban | 1 | 2 | 2 | 2 | **1.75** |
| Automated Kanban | 5 | 5 | 5 | 5 | **5.0** |
| Bug Triage | 2 | 3 | 1 | 1 | **1.75** |
| Team Planning | 2 | 2 | 3 | 3 | **2.5** |

**Conclusion:** The Automated Kanban template is the optimal choice for the HotelHub project, scoring 5 out of 5 across all evaluation criteria. It will be used as the foundation for the custom Kanban board in Part 2 of this assignment.

---

## 1.5 Next Steps

With the template selected, Part 2 will involve:

1. Creating the Automated Kanban project in GitHub
2. Adding two custom columns: "Testing" and "Blocked"
3. Populating the board with all 16 issues from Assignment 6
4. Organising issues according to the Sprint 1 plan
5. Taking a screenshot of the final board

The customisation will enhance the base template to better reflect the HotelHub development workflow, which includes a quality assurance phase (Testing) and handling of impediments (Blocked).
