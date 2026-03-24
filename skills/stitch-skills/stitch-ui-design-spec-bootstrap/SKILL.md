---
name: stitch-ui-design-spec-bootstrap
description: Bootstrap-Vue design spec for Stitch. Outputs hard-constraints prefix or selector JSON and assembled prompt.
---


# Bootstrap Design Spec (Bootstrap 5 / Vue)

**Constraint**: Only use this skill when the user explicitly mentions "Stitch".

## Purpose

This skill makes the Bootstrap design spec executable in two modes:

1) **Prefix mode**: output a paste-ready **Hard constraints prefix** for Stitch `[Context]`.
2) **Selector mode**: output `CONTRACT_SELECTION_JSON_V1` and then an assembled Stitch prompt that injects only the required component/state snippets.

## Trigger Keywords

Prefer this skill when the user request includes any of:

- `bootstrap`, `bootstrap-vue`, `bs-vue`, `bs5`

Chinese trigger keywords (only for triggering):

- `bootstrap 风格`
- `响应式布局` (if context implies Bootstrap)

## Source of Truth

- `references/contract.md`
- `references/examples.md`
- `references/official.md`

## Output (STRICT)

Decide the mode by the user intent:

- If the user asks for **beautify/polish/refine an existing screen**, or asks for **selector / JSON / contracts.include / states.include** → use **Selector mode**.
- Otherwise → use **Prefix mode**.

### Prefix mode

Return exactly one code block:

```text
[Hard constraints prefix]
- Framework: BootstrapVue (Vue 3 compatible / Bootstrap 5).
- Design Tokens:
  - Colors: Primary=#0d6efd, Secondary=#6c757d, Success=#198754, Danger=#dc3545, Warning=#ffc107, Info=#0dcaf0.
  - Spacing: STRICTLY use utility classes (m-*, p-*, gap-*). Scale: 1=0.25rem, 2=0.5rem, 3=1rem (default), 4=1.5rem, 5=3rem.
  - Radius: rounded (0.25rem), rounded-pill, rounded-circle.
  - Shadows: shadow-sm, shadow, shadow-lg.
- Component Contracts:
  - Layout: Use <b-container>, <b-row>, <b-col cols="..." md="...">. NO raw CSS grid.
  - Buttons: Use <b-button variant="primary" size="sm/lg">. NO <button class="btn">.
  - Forms: Use <b-form-group>, <b-form-input>, <b-form-select>.
  - Cards: Use <b-card title="..." img-src="...">.
  - Tables: Use <b-table striped hover :items="...">.
- Layout Invariants:
  - Mobile-first responsive classes (e.g., col-12 col-md-6).
  - Use d-flex utilities for alignment.
```

### Selector mode

Return exactly two code blocks, in this order, with no extra prose:

1) Contract selection JSON:

```json
{
  "version": "CONTRACT_SELECTION_JSON_V1",
  "designSystem": "bootstrap-vue",
  "mode": "selector",
  "contracts": { "include": [] },
  "states": { "include": [] }
}
```

2) Final Stitch prompt:

```text
[Context]
(Paste Hard Constraints Prefix here)
(Add "Layout Invariants" from contract.md if beautifying)

[Layout]
(Describe the macro layout structure, e.g., "Responsive Grid System with Container")

[Components]
(Inject component snippets matching the JSON selection above)
```

## References

- [Contract](references/contract.md)
- [Examples](references/examples.md)
- [Official Docs](references/official.md)
