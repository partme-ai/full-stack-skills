# Example: uView 2.0 Design Contract (Stitch Integration)

## Trigger Keywords

- Mention "Stitch" AND `uview` keywords.
- Examples (Chinese):
  - 使用 Stitch 和 uview 风格 实现 `docs/登录_PRD.md` 文档要求的设计工作
- Examples (English):
  - Use Stitch in uView 2.0 style to design a mobile Login screen.

## References

- Full Contract & Constraints: [references/contract.md](./contract.md)
- Official References: [references/official.md](./official.md)

## Expected Behavior

1. This skill outputs uView hard constraints prefix (tokens/spacing/type/radius/shadows, etc.).
2. The orchestrator appends it as `[Context]` prefix to the Stitch Prompt.
3. Subsequent generation / refinement maintains consistency with uView style and avoids layout drift.

## Scenario 1: Mobile Login Page

**User Input:**
> 使用 Stitch 和 uView 2.0 风格设计一个登录页

**Skill Output (Contract):**

```text
[Context]
Design System: uView 2.0 (Vue 2)
Constraint Level: Strict

# Design Tokens
- Colors: Primary=#3c9cff, Text=#303133, Bg=#f3f4f6
- Radius: 8px (standard)

# Component Contract
- Layout: <view class="wrap"> with padding.
- Logo: <u-image width="100" height="100"> centered.
- Form: <u--form> (double dash).
- Input: <u--input border="surround" prefixIcon="account">.
- Button: <u-button type="primary" text="Login" shape="circle">.
- Actions: <u-row> for "Forgot Password" / "Register".

# Layout Rules
- Page background #f3f4f6.
- Inputs should have sufficient vertical spacing (margin-bottom: 20px).
```
