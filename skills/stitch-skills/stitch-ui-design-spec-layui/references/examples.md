# Example: Layui-Vue Design Contract (Stitch Integration)

## Trigger Keywords

- Mention "Stitch" AND `layui` / `layui-vue` keywords.
- Examples (Chinese):
  - 使用 Stitch 和 Layui 风格设计一个后台管理系统的仪表盘
  - 使用 Stitch 和 layui 风格 实现 `docs/登录_PRD.md` 文档要求的设计工作
- Examples (English):
  - Use Stitch in Layui-Vue style to design a Dashboard.

## References

- Full Contract & Constraints: [references/contract.md](./contract.md)
- Official References: [references/official.md](./official.md)

## Expected Behavior

1. This skill outputs Layui hard constraints prefix (tokens/radius=2px/primary=#16baaa, etc.).
2. The orchestrator appends it as `[Context]` prefix to the Stitch Prompt.
3. Subsequent generation / refinement maintains consistency with Layui style.

## Scenario 1: Admin Data Table

**User Input:**
> 使用 Stitch 和 Layui 风格设计一个用户管理列表页

**Skill Output (Contract):**

```text
[Context]
Design System: Layui-Vue
Constraint Level: Strict

# Design Tokens
- Colors: Primary=#16baaa, Danger=#FF5722, Border=#e2e2e2
- Radius: 2px (Small/Sharp)
- Spacing: Compact

# Component Contract
- Layout: <lay-container fluid>, <lay-row space="10">.
- Search Bar: <lay-card> containing <lay-form layout="inline">.
- Table: <lay-table :columns="columns" :dataSource="dataSource">.
- Pagination: <lay-page :total="100" theme="green">.
- Actions: <lay-button type="primary" size="sm">Edit</lay-button>.

# Layout Rules
- Header: Breadcrumb + Page Title.
- Content: White card background for table area.
- Table header background: #f2f2f2.
```
