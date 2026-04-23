## GitHub Issue Body Template

Use this markdown template when composing the issue body. Fill only the sections for which data was collected; omit empty optional sections.

```markdown
## Summary

{Q1 — concise one-line problem statement}

## What Happened

{Q2 — exact observed behaviour, error messages, wrong output}

## Pre-conditions / Context

{Q3 — what the user was doing before; concurrent activities}

## Reproducibility

{Q4 — always / sometimes / happened once; frequency details}

## Expected Behaviour / Why It Matters

{Q7 — why this is a problem; expected correct behaviour}

## Environment

{Q8 — version, platform, URL, screen name, deployment environment}

## Test Data / Inputs

{Q6 — specific data or inputs used; omit section if not provided}

## Attachments

{Q5 — links to screenshots/video; omit section if not provided}
```

## Label Mapping

| Condition | Suggested label |
|-----------|----------------|
| Reproducibility = always | `bug` |
| Reproducibility = sometimes | `bug`, `intermittent` |
| Reproducibility = once | `needs-investigation` |
| Affects multiple areas (Q7) | `bug`, `impact:high` |
| Version specified (Q8) | Add version label if repo uses them |
