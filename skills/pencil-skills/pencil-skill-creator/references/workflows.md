# Workflows

## Table of contents

- Overview
- Automated creation (recommended)
- Manual creation
- Validation checklist

## Overview

This skill creates new **pencil-ui-design-system-*** skills that initialize a design system in Pencil (variables + component overview frames) via PENCIL_PLAN.

Follow this workflow in order:

1. Identify the design system and name the skill (e.g. layui, antd, uviewpro).
2. Scaffold the skill directory (automated script recommended).
3. Refine the generated `SKILL.md` with design tokens (colors, typography, radius) and component categories from official docs.
4. Fill `references/contract.md`, `references/official.md`, `references/examples.md`.
5. Validate the generated skill against the checklist below.

## Automated creation (recommended)

1. Decide the design system slug, e.g. `layui`, `antd`, `uviewpro`.
2. Run:

```bash
./scripts/init_pencil_design_system_skill.py <name> --path skills/
```

Accepted inputs:

- `layui` -> generates `pencil-ui-design-system-layui`
- `uview-pro` -> generates `pencil-ui-design-system-uview-pro` (normalized to kebab-case)
- `pencil-ui-design-system-antd` -> generates `pencil-ui-design-system-antd`

3. Open the generated files and refine:

- `SKILL.md` (Step 1 Variables table, Step 2 Component overview list)
- `references/contract.md`, `references/official.md`, `references/examples.md`

## Manual creation

1. Create directory structure:

```bash
mkdir -p skills/pencil-ui-design-system-<name>/references
```

2. Write `SKILL.md`:

- Must include constraint ("only when user mentions Pencil or design system initialization").
- Must define Step 1: Variables (for `set_variables` MCP tool).
- Must define Step 2: Component overview (for `batch_design` MCP tool).
- Must NOT execute MCP tools; output PENCIL_PLAN only.

3. Create references:

- `references/contract.md`: Design tokens and component naming.
- `references/official.md`: Link to official documentation.
- `references/examples.md`: Example PENCIL_PLAN or usage.

## Validation checklist

The created design-system skill must satisfy:

1. Naming: directory and `name:` field are `pencil-ui-design-system-<name>` (kebab-case).
2. Trigger: only triggers when the user mentions Pencil and the target design system.
3. Output: PENCIL_PLAN (Step 1 set_variables, Step 2 batch_design component overview); does not call MCP tools directly.
4. Variables: table or list of variable names and values per .pen schema.
5. Component overview: list of categories and component names per category.
