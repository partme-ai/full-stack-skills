# Workflows

## Table of contents

- Overview
- Automated creation (recommended)
- Manual creation
- Validation checklist

## Overview

This skill creates new Stitch Scenario Skills (e.g., `stitch-ui-music-designer`) that act as domain-specific prompt architects.

Follow this workflow in order:

1. Identify the scenario and name the skill.
2. Scaffold the skill directory (automated script recommended).
3. Refine the generated `SKILL.md` to encode domain knowledge and strict output format.
4. Add `examples/usage.md` with at least 2 real input/output pairs.
5. Validate the generated skill against the checklist below.

## Automated creation (recommended)

1. Decide the scenario slug, e.g. `music`, `login`, `crm`.
2. Run:

```bash
./scripts/init_stitch_skill.py <scenario-or-skill-name> --path skills/
```

Accepted inputs:

- `music` -> generates `stitch-ui-music-designer`
- `music-designer` -> generates `stitch-ui-music-designer`
- `stitch-ui-music-designer` -> generates `stitch-ui-music-designer`

3. Open the generated files and refine:

- `SKILL.md`
- `examples/usage.md`

## Manual creation

1. Create directory structure:

```bash
mkdir -p skills/stitch-ui-<scenario>-designer/examples
```

2. Write `SKILL.md`:

- Must include trigger constraint (“only when user mentions Stitch”).
- Must define strict output format (one prompt code block).
- Must NOT execute MCP tools.

3. Write `examples/usage.md` with at least:

- One mobile example
- One desktop example (or a second distinct flow)

## Validation checklist

The created scenario skill must satisfy:

1. Naming: directory and `name:` field are `stitch-ui-<scenario>-designer`.
2. Trigger safety: only triggers when the user mentions “Stitch”.
3. Design-first: outputs a prompt; does not call any MCP tool.
4. Output strictness: returns exactly one prompt code block using `[Context] [Layout] [Components]`.
5. Examples: at least 2 input/output pairs, not placeholders.
