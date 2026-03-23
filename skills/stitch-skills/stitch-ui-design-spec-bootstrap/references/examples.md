# Example: Bootstrap-Vue Design Contract (Stitch Integration)

## Trigger Keywords

- Mention "Stitch" AND `bootstrap` / `bootstrap-vue` / `bs-vue` keywords.
- Examples (Chinese):
  - 使用 Stitch 和 Bootstrap 风格设计一个后台管理系统的仪表盘
  - 使用 Stitch 和 bootstrap-vue 风格 实现 `docs/登录_PRD.md` 文档要求的设计工作
  - 使用 Stitch 和 Bootstrap 风格设计一个响应式的登录页
- Examples (English):
  - Use Stitch in Bootstrap-Vue style to design a Dashboard.
  - Create a responsive landing page using Stitch and Bootstrap 5 style.

## References

- Full Contract & Constraints: [references/contract.md](./contract.md)
- Official References: [references/official.md](./official.md)

## Expected Behavior

1. This skill outputs Bootstrap hard constraints prefix (tokens/primary=#0d6efd/spacing/radius, etc.).
2. The orchestrator appends it as `[Context]` prefix to the Stitch Prompt.
3. Subsequent generation / refinement maintains consistency with Bootstrap style and uses utility classes.

## Scenario 1: Responsive Login Page

**User Input:**
> 使用 Stitch 和 Bootstrap 风格设计一个响应式的登录页

**Skill Output (Contract):**

```text
[Context]
Design System: Bootstrap-Vue (Bootstrap 5)
Constraint Level: Strict

# Design Tokens
- Colors: Primary=#0d6efd, Secondary=#6c757d, Success=#198754, Danger=#dc3545
- Spacing: 1=0.25rem, 2=0.5rem, 3=1rem (default), 4=1.5rem, 5=3rem
- Radius: rounded (0.25rem), rounded-pill (50rem)
- Shadows: shadow-sm, shadow, shadow-lg

# Component Contract
- Layout: Use <b-container>, <b-row>, <b-col> (e.g., <b-col cols="12" md="6">).
- Buttons: Use <b-button variant="primary">. Do NOT use <button class="btn">.
- Forms: Wrap inputs in <b-form-group>. Use <b-form-input>, <b-form-checkbox>.
- Cards: Use <b-card> for content containers.

# Layout Rules
- Center the login form using Flexbox utilities (d-flex justify-content-center align-items-center) or Grid offsets.
- Ensure full viewport height (vh-100) for the background container.
```
