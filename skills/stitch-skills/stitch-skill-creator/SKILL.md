---
name: stitch-skill-creator
description: "A factory skill for creating new Stitch Scenario Skills. It enforces the \"Design First, Execute Last\" SOP and standard Stitch architectural patterns. Use this when you need to add support for a new domain e.g. \"Music Apps\" \"Social Networks\" to the Stitch ecosystem."
license: Complete terms in LICENSE.txt
allowed-tools:
  - "Read"
  - "Write"
  - "Bash"
---


# Stitch Skill Creator

This skill guides the creation of new **Stitch Scenario Skills**. A Scenario Skill is a specialized "Prompt Architect" for a specific domain (e.g., `stitch-ui-music-designer`, `stitch-ui-blog-designer`).

## Core Philosophy

All Stitch Skills created by this creator **MUST** adhere to the **Stitch Design SOP**:

1.  **Trigger Safety**: The skill must ONLY trigger when the user explicitly mentions "Stitch".
2.  **Design First**: Never execute. Always construct a high-quality prompt first.
3.  **Self-Contained**: The skill should act as a specialized "Prompt Template" that encapsulates domain knowledge (e.g., a Music App needs a "Play Button", "Cover Art").

## Workflow (Progressive Disclosure)

Keep this file concise. Use bundled references when you need full details:

- Workflow: `references/workflows.md`
- Output patterns: `references/output-patterns.md`

## Quick start (Automated Creation)

### Option A: Automated Creation (Recommended)

Use the bundled script to automatically generate the skill structure, `SKILL.md` (with Golden Template), and `examples/usage.md`.

```bash
# Usage: ./scripts/init_stitch_skill.py <scenario-name> --path <skills-directory>
./scripts/init_stitch_skill.py music-designer --path skills/
```

This will automatically:
1.  Create `skills/stitch-ui-music-designer`.
2.  Populate `SKILL.md` with the required SOP and Templates.
3.  Create `examples/usage.md`.

### Option B: Manual Creation (Only if needed)

Follow: `references/workflows.md` -> Manual creation.

### Step 1: Define the Scenario
Identify the domain and name the skill following the strict naming convention: `stitch-ui-<scenario>-designer`.
*   *Example Scenario*: "Music Apps"
*   *Skill Name*: `stitch-ui-music-designer` (MUST start with `stitch-ui-`)
*   *Example Scenario*: "Login Pages"
*   *Skill Name*: `stitch-ui-login-designer`

### Step 2: Create Directory Structure
```bash
mkdir -p skills/stitch-ui-<scenario>-designer/examples
```

### Step 3: Write `SKILL.md` (The Golden Template)
You **MUST** use the following template for the new skill. It enforces the required SOP.

````markdown
---


# <Scenario> Screen Designer

**Constraint**: Only use this skill when the user explicitly mentions "Stitch" or when orchestrating a Stitch design task.

This skill helps you construct high-quality prompts for <Scenario> flows to be used by the Stitch Orchestrator.

## Functionality
It encapsulates best practices for <Scenario> UI design and translates user intent into a structured Stitch prompt.

## Integration with Stitch Designer SOP
This skill is part of the **Stitch UI Orchestration** flow.
1.  **Orchestrator**: `stitch-ui-designer` calls this skill when a scenario-specific prompt is needed.
2.  **Guidelines**: You MUST apply principles from `stitch-ued-guide` (e.g., visual vocabulary, device constraints).
3.  **Output**: You do NOT execute. You return a prompt only.

## Prompt Template

When the user asks for a <Scenario> screen, use this template to construct the prompt:

```text
[Context]
[Device] <Scenario> screen for [App Name]. [Style] aesthetic.

[Layout]
Header: [...]
Body: [...]
Footer: [...]

[Components]
- [...]
- [...]
```

## Output Format (STRICT)

Return exactly one code block and no extra prose:

```text
[Context]
...

[Layout]
...

[Components]
...
```

## Usage in Orchestrator
This skill is designed to be called by `stitch-ui-designer`. It does NOT execute; it returns a prompt only.
````

### Step 4: Write `examples/usage.md`
Provide at least 2 distinct examples of how this skill transforms a vague request into a detailed prompt.

## Best Practices for New Skills

1.  **Domain Specificity**: The value of a Scenario Skill is in its *specific knowledge*.
    *   *Bad*: "A page with text."
    *   *Good (Music)*: "A player view with a scrubbing bar, album art, and waveform visualization."
2.  **Device Awareness**: Ensure the template supports Mobile (default) and Desktop.
3.  **No Direct Execution**: The Scenario Skill must not call any MCP tool. It produces the prompt that the Orchestrator uses.

## References

- [Examples](examples/usage.md)
- [Workflows](references/workflows.md)
- [Output Patterns](references/output-patterns.md)
- [Init Script](scripts/init_stitch_skill.py)
