# Output Patterns

Use these patterns to keep newly created Stitch Scenario Skills consistent and safe.

## Scenario Skill Output (STRICT)

A `stitch-ui-<scenario>-designer` skill must return exactly one code block and no extra prose.

It must follow this structure:

```text
[Context]
...

[Layout]
...

[Components]
...
```

Hard requirements:

- Do not call any MCP tool (design-only).
- Do not output multiple alternatives unless the user explicitly asks for variants.
- Preserve the prompt sections exactly: `[Context]`, `[Layout]`, `[Components]`.

## Creator Skill Output (Recommended)

When `stitch-skill-creator` scaffolds a new skill, report the created artifacts concisely:

```markdown
# Stitch Skill Created

## Path
- skills/stitch-ui-<scenario>-designer

## Files
- SKILL.md
- LICENSE.txt
- examples/usage.md

## Next steps
1. Fill domain-specific UI structure in `[Layout]` and `[Components]`.
2. Replace placeholders in `examples/usage.md` with real input/output pairs.
3. Re-run validation checklist.
```
