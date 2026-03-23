---
name: stitch-ui-design-spec-uview
description: uView 2 design spec for Stitch. Outputs hard-constraints prefix or selector JSON and assembled prompt.
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
---


# uView Design Spec (uView 2.0 / uni-app / Vue2)

**Constraint**: Only use this skill when the user explicitly mentions "Stitch".

## Purpose

This skill makes the uView 2.0 design spec executable in two modes:

1) **Prefix mode**: output a paste-ready **Hard constraints prefix** for Stitch `[Context]`.
2) **Selector mode**: output `CONTRACT_SELECTION_JSON_V1` and then an assembled Stitch prompt that injects only the required component/state snippets.

## Trigger Keywords

Prefer this skill when the user request includes any of:

- `uview`, `uview2`, `uview2.0`, `u-view`

**Negative Constraint**: If the user says "uView Pro" or "uviewpro", DO NOT use this skill. Use `stitch-ui-design-spec-uviewpro` instead.

Chinese trigger keywords (only for triggering):

- `uview 风格`
- `美化`
- `优化`

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
- Framework: uView 2.0 (uni-app / Vue 2).
- Design Tokens:
  - Colors: Primary=#3c9cff, Success=#5ac725, Warning=#f9ae3d, Error=#f56c6c, Info=#909399.
  - Background: #f3f4f6. Border: #dadbde.
  - Spacing: 4, 8, 12, 16, 20, 24, 32, 40 (px).
  - Radius: 8, 12, 999 (px).
- Component Contracts:
  - Layout: Use <u-row> and <u-col span="...">.
  - Forms: Use <u--form> (note double dash), <u--input border="surround">.
  - Buttons: Use <u-button type="primary">.
  - Navbar: Use <u-navbar title="..." :autoBack="true">.
  - List: <u-swipe-action>, <u-index-list>, <u-waterfall>.
  - Feedback: Use this.$refs.uToast.show({...}), <u-code> (SMS).
- Layout Invariants:
  - No gradients as default style.
  - Minimal shadows.
  - Transitions: 200ms ease-out.
```

### Selector mode

Return exactly two code blocks, in this order, with no extra prose:

1) Contract selection JSON:

```json
{
  "version": "CONTRACT_SELECTION_JSON_V1",
  "designSystem": "uview2",
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
(Describe the macro layout structure, e.g., "Mobile Column Layout with Navbar")

[Components]
(Inject component snippets matching the JSON selection above)
```

## References

- [Contract](references/contract.md)
- [Examples](references/examples.md)
- [Official Docs](references/official.md)
