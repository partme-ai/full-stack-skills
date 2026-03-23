---
name: pencil-skill-creator
description: Factory skill for creating new pencil-ui-design-system-* skills. Use when you need to add support for a new design system layui antd bootstrap element uview uviewpro vant ucharts echarts etc. to the Pencil ecosystem.
license: Complete terms in LICENSE.txt
---


# Pencil Skill Creator

This skill guides the creation of new **pencil-ui-design-system-* skills**. Each skill initializes a design system in Pencil (variables + component overview frames) via PENCIL_PLAN.

## Core Philosophy

All design-system skills created by this creator **MUST** adhere to:

1. **Trigger**: The skill triggers when the user explicitly mentions Pencil and the target design system (e.g. "init layui design system with Pencil").
2. **Action-level plan**: Output a PENCIL_PLAN (Step 1: set_variables; Step 2: batch_design component overview). Do not execute; output the plan for the Agent to call Pencil MCP tools.
3. **Self-contained**: The skill encapsulates design tokens (colors, typography, radius) and component categories from the official design system docs.

## Workflow (Progressive Disclosure)

Keep this file concise. Use bundled references when you need full details:

- Workflow: `references/workflows.md`
- Output patterns: `references/output-patterns.md`

## Quick start (Automated Creation)

### Option A: Automated Creation (Recommended)

Use the bundled script to automatically generate the skill structure, `SKILL.md` (with Golden Template), and `references/` placeholders.

```bash
# Usage: ./scripts/init_pencil_design_system_skill.py <name> --path <skills-directory>
./scripts/init_pencil_design_system_skill.py layui --path skills/
```

This will:

1. Create `skills/pencil-ui-design-system-layui`.
2. Populate `SKILL.md` with the required structure (When to use, Step 1 Variables, Step 2 Component overview).
3. Create `references/contract.md`, `references/official.md`, `references/examples.md` placeholders.
4. Copy `LICENSE.txt` from an existing skill.

### Option B: Manual Creation

Follow: `references/workflows.md` -> Manual creation.

### Step 1: Define the design system

Identify the framework and name the skill: `pencil-ui-design-system-<name>` (kebab-case).

- Example: "layui" -> `pencil-ui-design-system-layui`
- Example: "uview pro" -> `pencil-ui-design-system-uviewpro`

### Step 2: Create directory structure

```bash
mkdir -p skills/pencil-ui-design-system-<name>/references
```

### Step 3: Write `SKILL.md` (Golden Template)

You **MUST** use the following template structure for the new skill:

- **Frontmatter**: `name: pencil-ui-design-system-{{name}}`, description containing "初始化 {{design_system}}: design system components".
- **Constraint**: Only use when user explicitly mentions Pencil or design system initialization.
- **When to use**: Trigger keywords (e.g. layui, antd).
- **Step 1: Variables**: Table of variables for `set_variables` (colors, fonts, radius). Follow .pen schema.
- **Step 2: Component overview**: List of frames/categories to create via `batch_design` (component categories and component names per category).
- **Best practices**: Verify tokens against official docs; use `replace: false` unless full reset; use Auto Layout for frames.
- **Keywords**: pencil, design system, init, <framework-name>.

### Step 4: Fill references

- `references/contract.md`: Design tokens and component contracts (prefix, naming).
- `references/official.md`: Link to official documentation.
- `references/examples.md`: Example PENCIL_PLAN or usage.

## Integration with Pencil path

This skill is part of the **Pencil specification flow**:

1. **PRD** -> **pencil-ui-design-spec-generator** outputs PENCIL_PLAN.
2. **pencil-ui-design-system-*** skills output the concrete variables + component structure for a given design system.
3. Agent calls Pencil MCP tools (`open_document`, `set_variables`, `batch_design`, `get_screenshot`) in order.

## Naming validation

Script enforces: `pencil-ui-design-system-[a-z0-9]+(-[a-z0-9]+)*`.
