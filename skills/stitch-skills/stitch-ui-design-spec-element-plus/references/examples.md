# Example: Element Plus Design Contract (Stitch Integration)

## Trigger Keywords

- Mention "Stitch" AND `element` / `element-plus` / `el-plus` keywords.
- Examples (Chinese):
  - 使用 Stitch 和 Element Plus 风格设计一个企业级后台管理系统
  - 使用 Stitch 和 Element Plus 风格重构登录页面
- Examples (English):
  - Use Stitch in Element Plus style to design a CRM dashboard.
  - Create a user settings form using Stitch and Element Plus.

## References

- Full Contract & Constraints: [references/contract.md](./contract.md)
- Official References: [references/official.md](./official.md)

## Expected Behavior

1. This skill outputs Element Plus hard constraints prefix (tokens/primary=#409EFF/radius/typography, etc.).
2. The orchestrator appends it as `[Context]` prefix to the Stitch Prompt.
3. Subsequent generation uses `el-*` components and the 24-column grid system.

## Scenario 1: Admin Dashboard

**User Input:**
> 使用 Stitch 和 Element Plus 风格设计一个企业级后台管理系统首页

**Skill Output (Contract):**

```text
[Context]
Design System: Element Plus (Vue 3)
Constraint Level: Strict

# Design Tokens
- Colors: Primary=#409EFF, Success=#67C23A, Warning=#E6A23C, Danger=#F56C6C
- Background: Page=#F2F3F5, Card=#FFFFFF
- Typography: Font-family="Helvetica Neue"

# Component Contract
- Layout: Use <el-container> with <el-aside>, <el-header>, <el-main>.
- Navigation: <el-menu mode="vertical"> for sidebar, <el-breadcrumb> for top bar.
- Data: <el-row :gutter="20"> for KPI cards. <el-table> for recent activities.
- Cards: <el-card shadow="hover">.

# Layout Rules
- Sidebar width fixed (e.g., 200px).
- Header height fixed (e.g., 60px).
- Use el-space for gap control.
```
