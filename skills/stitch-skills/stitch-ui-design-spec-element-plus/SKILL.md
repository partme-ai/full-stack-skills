---
name: stitch-ui-design-spec-element-plus
description: Element Plus design spec for Stitch. Outputs hard-constraints prefix or selector JSON and assembled prompt.
---


# Element Plus Design Spec (Element Plus / Vue 3)

**Constraint**: Only use this skill when the user explicitly mentions "Stitch".

## Purpose

This skill makes the Element Plus design spec executable in two modes:

1) **Prefix mode**: output a paste-ready **Hard constraints prefix** for Stitch `[Context]`.
2) **Selector mode**: output `CONTRACT_SELECTION_JSON_V1` and then an assembled Stitch prompt that injects only the required component/state snippets.

## Trigger Keywords

Prefer this skill when the user request includes any of:

- `element`, `element-plus`, `el-plus`, `element-ui`

Chinese trigger keywords (only for triggering):

- `element 风格`
- `饿了么组件库`
- `后台管理系统` (if context implies Element Plus)

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
- Framework: Element Plus (Vue 3).
- Design Tokens:
  - Colors: Primary=#409EFF (Blue), Success=#67C23A, Warning=#E6A23C, Danger=#F56C6C, Info=#909399.
  - Typography: Font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", Arial, sans-serif.
  - Radius: Small=2px, Base=4px, Round=20px.
- Component Contracts:
  - Layout: Use <el-row :gutter="20"> and <el-col :span="...">. Container: <el-container>, <el-header>, <el-main>.
  - Buttons: Use <el-button type="primary" plain/round>.
  - Forms: Use <el-form>, <el-form-item>, <el-input>, <el-select>, <el-switch>, <el-checkbox>.
  - Data: <el-table>, <el-descriptions>, <el-timeline>, <el-carousel>, <el-empty>.
  - Cards: Use <el-card shadow="hover"> with #header slot.
  - Icons: Use <el-icon><Edit /></el-icon> (from @element-plus/icons-vue).
  - Navigation: <el-menu>, <el-breadcrumb>, <el-tabs>, <el-steps>.
  - Feedback: Use ElMessage.success() for JS feedback, <el-alert>, <el-dialog>, <el-drawer>.
- Layout Invariants:
  - Always use 24-column grid system.
  - Use el-space for inline spacing.
```

### Selector mode

Return exactly two code blocks, in this order, with no extra prose:

1) Contract selection JSON:

```json
{
  "version": "CONTRACT_SELECTION_JSON_V1",
  "designSystem": "element-plus",
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
(Describe the macro layout structure, e.g., "Admin Dashboard Layout with Sidebar")

[Components]
(Inject component snippets matching the JSON selection above)
```

## References

- [Contract](references/contract.md)
- [Examples](references/examples.md)
- [Official Docs](references/official.md)
