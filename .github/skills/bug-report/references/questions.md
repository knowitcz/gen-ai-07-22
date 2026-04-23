# Bug Report Questions

These are the required questions for a complete bug report. Each maps to a field in the final GitHub issue.

| ID | Question  | Field in issue |
|----|-----------|----------------|
| Q1 | What is the problem? | Title + Summary |
| Q2 | What exactly happened? | Steps to Reproduce / Actual Behaviour |
| Q3 | What was I doing before the problem occurred? Was I doing something else at the same time? | Context / Pre-conditions |
| Q4 | Did the problem occur more than once? | Reproducibility |
| Q5 | Do I have any screenshots or video? | Attachments (optional) |
| Q6 | Did I use specific data or inputs? | Test Data / Inputs |
| Q7 | Why do I consider this a problem? | Impact / Expected Behaviour |
| Q8 | What version and where did I encounter the problem? | Environment / Version |

## Completeness Rules

- **Required fields**: Q1, Q2, Q7 — a report cannot be submitted without these.
- **Strongly recommended**: Q3, Q4, Q8 — ask for these if missing.
- **Optional**: Q5 (attachments), Q6 (test data) — mention that they can be added but do not block submission.

## Gap Detection Heuristics

When scanning the user's input, treat a question as **answered** if the input contains a clear, direct answer — not merely a mention. Examples:

- Q1 answered: user states a specific problem or bug title.
- Q2 answered: user describes what happened (error message, wrong output, crash).
- Q3 answered: user describes steps taken before the issue, or explicitly says "no prior steps".
- Q4 answered: user says "always", "sometimes", "only once", or equivalent.
- Q5 answered: user provides a link/attachment, or explicitly says "no screenshot".
- Q6 answered: user names specific inputs/data, or says "default data".
- Q7 answered: user explains why it is wrong or what the expected behaviour is.
- Q8 answered: user states version, environment, or location (URL, screen name, etc.).
