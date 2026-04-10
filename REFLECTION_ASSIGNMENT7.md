# Assignment 7 Reflection: Kanban Board Implementation

## Challenges in Selecting and Customizing the Template

The main challenge was navigating GitHub's two different project interfaces (new vs. classic). The classic interface had "Automated Kanban" but the new interface has different template names. I eventually used the new "Kanban" template and added automation workflows manually.

Another challenge was deciding which columns to add. The assignment required 2+ new columns. I chose "Testing" to represent quality assurance and "Blocked" to handle impediments. I also renamed existing columns to standard Kanban terms: "To do", "In progress", "Testing", "Done", "Blocked".

A third challenge was that some issues from Assignment 6 were marked as "closed". I had to reopen them so they would appear as active tasks on the board.

## GitHub Projects vs. Other Tools (Trello, Jira)

| Tool | Best For | Weakness for This Project |
|------|----------|---------------------------|
| **GitHub Projects** | Teams already using GitHub for code | Less feature-rich than Jira |
| **Trello** | Simple, visual boards | No native code integration |
| **Jira** | Large enterprises with complex workflows | Overkill for solo developer |

For the HotelHub project, GitHub Projects is the best choice because it integrates directly with my existing Issues, Pull Requests, and commits. The automation (auto-adding new issues, moving closed issues to Done) reduces manual work.

## Lessons Learned

This assignment taught me that a Kanban board is not just a visual aid. When set up thoughtfully, it becomes the central hub for a project. It provides transparency, enforces discipline (through WIP limits), and makes progress measurable.

The most important lesson was that customising columns to match your actual workflow is essential. Generic columns are a start, but adding "Testing" and "Blocked" makes the board more useful for identifying bottlenecks.

I also learned how to enable and test GitHub's built-in automation workflows Item added to project, Item closed, Pull request merged. These automations keep the board accurate without manual effort, which is a huge time-saver in Agile development.


