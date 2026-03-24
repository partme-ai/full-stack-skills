# Output Patterns

Use these patterns to keep newly created pencil-ui-design-system-* skills consistent and executable.

## PENCIL_PLAN output format (STRICT)

A `pencil-ui-design-system-*` skill must output a **PENCIL_PLAN** that the Agent can execute by calling Pencil MCP tools in order.

### Step list format

Each step must specify: **tool** + **intent** + **key parameters**.

Example:

```text
Step 1: open_document(filePathOrTemplate: 'new')
Step 2: get_editor_state(include_schema: true)
Step 3: set_variables(variables: { ... })
Step 4: batch_design(operations: "root=I(document, { type: 'frame', layout: 'vertical', ... })")
Step 5: get_screenshot(nodeId: <root-id>)
```

### Variables block (Step 1 for design-system init)

Variables must follow .pen file schema. Format: variable name -> value (hex for colors, px for sizes).

```text
Step 1: set_variables
- primary: #2979ff
- primary-dark: #2b85e4
- font-md: 14px
- radius: 4px
...
```

### Component overview block (Step 2 for design-system init)

List of frames/categories to create via `batch_design`. Each category is a frame; list component names under each.

```text
Step 2: batch_design – create "Components Overview" frame with sections:
1. Basic Components: Color, Icon, Button, Layout, ...
2. Form Components: Form, Input, Textarea, ...
3. Data Components: Table, Progress, ...
...
```

Hard requirements:

- Do not call MCP tools from the skill; output the plan only.
- Preserve the two-step structure for design-system init: Variables, then Component overview.
- Variable names must be valid for .pen schema (no leading $ required).

## Creator skill output (recommended)

When `pencil-skill-creator` (or the init script) scaffolds a new skill, report the created artifacts:

```markdown
# Pencil Design System Skill Created

## Path
- skills/pencil-ui-design-system-<name>

## Files
- SKILL.md
- LICENSE.txt
- references/contract.md
- references/official.md
- references/examples.md

## Next steps
1. Fill design tokens in Step 1 Variables from official docs.
2. Fill component categories in Step 2 Component overview.
3. Add links and excerpts in references/official.md.
4. Add example PENCIL_PLAN in references/examples.md.
```
