---
name: 'bug-report'
description: 'Gather a complete bug report from the user by interviewing them against a structured question checklist, then submit the resulting GitHub issue via MCP. Use when: reporting a bug, filing an issue, something is broken or behaves unexpectedly. DO NOT USE FOR: searching existing issues, fixing bugs (coding task), general Q&A about the product.'
---

# Bug Report Skill

Guides any agent through collecting a complete bug report from a user, filling gaps with targeted follow-up questions, then submitting the issue to the correct GitHub repository via MCP.

## When to Use

- User says "I found a bug", "report a bug", "file an issue", or describes broken behaviour
- User wants to document unexpected or incorrect product behaviour
- User asks to create a GitHub issue for a defect
- A tester or developer wants to formally capture a defect

## 1. Parse User Input

Scan the user's initial description against all questions in [references/questions.md](references/questions.md).

Mark each question as **answered** or **missing** using the Gap Detection Heuristics in that file.

Do not ask for information already present in the user's description.

## 2. Ask Only for Missing Information

Ask the user to clarify only the **missing** questions, grouped into one message.

- Lead with required fields (Q1, Q2, Q7) if any are missing.
- Follow with strongly recommended fields (Q3, Q4, Q8) in a second group.
- Mention optional fields (Q5, Q6) as "if available, please share".
- Do not repeat questions the user has already answered.

Wait for the user's response before proceeding.

## 3. Confirm the Complete Report

Present a structured summary of all collected answers to the user for confirmation.

Ask: "Does this look correct? Shall I submit it as a GitHub issue?"

If the user requests corrections, apply them and re-confirm.

## 4. Resolve the Target Repository

Check whether the user explicitly named a repository in their request.

If **named**: use that repository.

If **not named**:
1. Run `git remote -v` to list available remotes.
2. Present the remote list to the user and ask them to select the target repository.
3. Wait for the user's selection before proceeding.

> The workspace may have multiple origins. Never assume a single remote.

## 5. Submit via MCP

Compose the GitHub issue using the template in [references/issue-template.md](references/issue-template.md).

Use the MCP server at `https://api.githubcopilot.com/mcp/x/issues` to create the issue in the resolved repository.

Report the created issue URL back to the user.

## Error Handling

| Situation | Action |
|-----------|--------|
| User provides contradictory answers | Point out the contradiction and ask to clarify before submitting |
| Required field (Q1, Q2, Q7) still missing after follow-up | Do not submit; ask once more and explain why it is required |
| Multiple remotes, user does not select | Ask again; do not guess the repository |
| MCP submission fails | Show the error, offer to retry or provide the issue body for manual submission |
| User says "skip" for a required field | Explain it is required and ask for at least a minimal answer |
