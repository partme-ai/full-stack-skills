# Awesome Agent Skills

> Curated list of resources for designing, building, and evaluating Agent Skills.
> _Generated from official specs, best practices, and example skills._
> _Review entries periodically for freshness._

## Contents

- [Specs](#specs)
- [Skill design & best practices](#skill-design--best-practices)
- [Evaluation & QA](#evaluation--qa)
- [Security & scripts](#security--scripts)
- [Example skills](#example-skills)
- [Templates](#templates)

## Specs

- [Agent Skills Specification](https://agentskills.io/specification) — Complete format specification for SKILL.md frontmatter, directory structure, and progressive disclosure. (spec)
- [Agent Skills Overview](https://agentskills.io/home) — What Agent Skills are, why they exist, and how progressive disclosure works. (spec)
- [How to create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) — Claude-specific guide for creating, structuring, testing, and packaging skills. (spec)

## Skill design & best practices

- [Best practices for skill creators](https://agentskills.io/skill-creation/best-practices) — How to write well-scoped skills: real expertise extraction, context budgeting, calibration, gotchas, checklists, and validation loops. (best-practice)
- [Quickstart: Create your first skill](https://agentskills.io/skill-creation/quickstart) — Step-by-step tutorial creating a `roll-dice` skill in VS Code with Copilot. (best-practice examples)
- [Optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) — How to test and improve description triggering accuracy with eval queries and a train/validation split. (best-practice evaluation)
- [Using scripts in skills](https://agentskills.io/skill-creation/using-scripts) — One-off commands, self-contained scripts, and designing script interfaces for agentic use. (best-practice scripts)

## Evaluation & QA

- [Evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills) — Structured eval workflow: test cases, assertions, grading, benchmarking with baseline comparisons. (evaluation)
- [SkillHub TRACE Evaluation Framework](https://skillhub.cn/tutorials#trace-evaluation) — Five-dimension quality model (Trust, Reliability, Adaptability, Convention, Effectiveness) for evaluating skills. (evaluation)
- [SkillHub TRACE announcement](https://skillhub.cn/announcements/3) — Tencent × SkillHub × Xuanwu Lab joint release of the TRACE framework. (evaluation)

## Security & scripts

- [Script safety checklist](skills/base-skills/skill-official-evaluation/references/script-safety-checklist.md) — Non-interactive CLI, `--help`, clear errors, no secrets, safe defaults, structured output. (security scripts)
- [Using scripts in skills](https://agentskills.io/skill-creation/using-scripts) — Covers `uvx`, `npx`, `pipx`, `bunx`, `deno run`, `go run` for one-off commands; PEP 723 inline dependencies for self-contained scripts. (security scripts)

## Example skills

- [Mermaid diagram skill](skills/document-skills/mermaid) — Well-structured skill with 23+ diagram types, version compatibility handling, and detailed workflow instructions. (examples docs)
- [skill-official-evaluation](skills/base-skills/skill-official-evaluation) — Official spec compliance evaluator using agentskills.io rubric with script safety checklist. (examples evaluation)
- [skill-trace-evaluation](skills/base-skills/skill-trace-evaluation) — TRACE five-dimension quality evaluator with HTML/Markdown/JSON output and SkillHub-style radar reports. (examples evaluation)

## Templates

- [Official evaluation report template](skills/base-skills/skill-official-evaluation/examples/sample-report.md) — Example Pass/Needs-improvement report with spec compliance checklist, Top-3 issues, and prioritized suggestions. (templates evaluation)
- [TRACE evaluation report template](skills/base-skills/skill-trace-evaluation/examples/sample-report.md) — Example TRACE report with overall rating, per-dimension scores, evidence, risks, and actionable suggestions. (templates evaluation)
