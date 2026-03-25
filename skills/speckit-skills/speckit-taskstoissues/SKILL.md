---
name: speckit-taskstoissues
description: "Convert tasks.md entries into GitHub issues in the matching remote repository using gh issue create, preserving task IDs for traceability. Use when the user wants to create GitHub issues from an existing tasks.md, needs issue tracking for implementation tasks, or wants to sync task progress with GitHub project boards."
---

# Spec Kit Tasks-to-Issues Skill

## When to Use

- You want to convert `tasks.md` into GitHub issues in the same repository.

## Inputs

- `specs/<feature>/tasks.md`
- The repository's Git remote URL
- Any user-provided issue labeling or grouping preferences

If tasks are missing, ask the user to run speckit-tasks first.

## Workflow

1. Run `.specify/scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").
1. From the executed script, extract the path to **tasks**.
1. Get the Git remote by running:

```bash
git config --get remote.origin.url
```

> [!CAUTION]
> ONLY PROCEED TO NEXT STEPS IF THE REMOTE IS A GITHUB URL

1. For each task in the list, create a new issue in the repository that matches the Git remote.
   - Prefer a GitHub issue-writing tool if available (e.g., MCP server or `gh issue create`).
   - Keep titles concise and include the task ID in the issue body for traceability.

> [!CAUTION]
> UNDER NO CIRCUMSTANCES EVER CREATE ISSUES IN REPOSITORIES THAT DO NOT MATCH THE REMOTE URL

## Outputs

- GitHub issues created from `tasks.md` (one per task), in the repository matching the Git remote
