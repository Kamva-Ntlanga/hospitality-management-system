# Assignment 7: Template Analysis and Selection

## 1.1 Template Comparison Table

| Template Name | Columns & Workflow | Automation Features | Suitability for Agile |
|---------------|-------------------|---------------------|------------------------|
| **Basic Kanban** | To do, In progress, Done | None - manual drag and drop only | Good for small, simple projects |
| **Automated Kanban** | To do, In progress, Done | Auto-adds new issues to To do; auto-moves to In progress when PR opened | **Best for Agile teams** - reduces manual work |
| **Bug Triage** | Needs triage, High priority, Low priority, Close | Minimal - just organizes bug workflow | Only for bug tracking, not general development |
| **Team Planning** | To do, In progress, Done | Minimal - good for collaboration but no automation | Good for roadmaps, not daily sprints |

## 1.2 Justification for Chosen Template

**Chosen Template:** Automated Kanban

**Reason for Selection:**

1. **Alignment with Agile:** The HotelHub project follows Agile principles. The Automated Kanban template automatically moves issues when Pull Requests are opened, keeping the board accurate without manual updates.

2. **Workflow Visualization:** The standard columns (To do, In progress, Done) perfectly map to a developer's workflow, providing an instant snapshot of project status.

3. **Efficiency for Solo Developer:** As a single developer, automation reduces administrative overhead, allowing more focus on coding rather than board maintenance.

4. **Seamless Integration:** The template works directly with GitHub Issues already created in Assignment 6, making it easy to populate the board.

**Conclusion:** The Automated Kanban template provides the best balance of simplicity and powerful automation for the HotelHub project.
