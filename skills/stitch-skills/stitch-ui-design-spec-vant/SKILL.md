---
name: stitch-ui-design-spec-vant
description: Vant 4 design spec for Stitch. Outputs hard-constraints prefix or selector JSON and assembled prompt.
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
---


# Vant Design Spec (Vant 4 / Vue 3)

**Constraint**: Only use this skill when the user explicitly mentions "Stitch".

## Purpose

This skill makes the Vant 4 design spec executable in two modes:

1) **Prefix mode**: output a paste-ready **Hard constraints prefix** for Stitch `[Context]`.
2) **Selector mode**: output `CONTRACT_SELECTION_JSON_V1` and then an assembled Stitch prompt that injects only the required component/state snippets.

## Trigger Keywords

Prefer this skill when the user request includes any of:

- `vant`, `vant4`, `vant-ui`, `vant ui`

Chinese trigger keywords (only for triggering):

- `vant 风格`
- `vant 组件库`

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
- Framework: Vant 4 (Vue 3 / Mobile).
- Design Tokens:
  - Colors: Primary=#1989fa (Blue), Success=#07c160, Warning=#ff976a, Danger=#ee0a24.
  - Background: Page=#f7f8fa, Card=#ffffff.
  - Typography: Base 14px.
  - Radius: sm=2px, md=4px, lg=8px.
- Component Contracts:
  - Layout: Use <van-row>, <van-col span="...">. Container: <van-config-provider>.
  - List/Card: Use <van-cell-group inset> for card style groups.
  - Buttons: Use <van-button type="primary" round block>.
  - Forms: Use <van-form>, <van-field>, <van-search>, <van-picker>, <van-date-picker>.
  - Business: <van-card> (Product), <van-submit-bar>, <van-address-list>, <van-coupon-list>.
  - Navigation: <van-nav-bar>, <van-tabbar>, <van-sidebar>, <van-tabs>.
  - Feedback: <van-action-sheet>, <van-swipe-cell>, <van-empty>.
- Layout Invariants:
  - Mobile First (375px base).
  - Use Flexbox for alignment.
  - Respect Safe Area.
```

### Selector mode

Return exactly two code blocks, in this order, with no extra prose:

1) Contract selection JSON:

```json
{
  "version": "CONTRACT_SELECTION_JSON_V1",
  "designSystem": "vant4",
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
