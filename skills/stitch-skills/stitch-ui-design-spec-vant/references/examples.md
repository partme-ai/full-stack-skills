# Example: Vant Design Contract (Stitch Integration)

## Trigger Keywords

- Mention "Stitch" AND `vant` / `vant4` / `vant-ui` keywords.
- Examples (Chinese):
  - 使用 Stitch 和 Vant 风格设计一个移动端购物车页面
  - 基于 Vant 4 规范设计一个用户个人中心
- Examples (English):
  - Use Stitch in Vant style to design a mobile Login screen.

## References

- Full Contract & Constraints: [references/contract.md](./contract.md)
- Official References: [references/official.md](./official.md)

## Expected Behavior

1. This skill outputs Vant hard constraints prefix (tokens/primary=#1989fa/spacing/radius, etc.).
2. The orchestrator appends it as `[Context]` prefix to the Stitch Prompt.
3. Subsequent generation / refinement maintains consistency with Vant style.

## Scenario 1: Mobile Login Page

**User Input:**
> 使用 Stitch 和 Vant 风格设计一个移动端登录页

**Skill Output (Contract):**

```text
[Context]
Design System: Vant 4 (Vue 3)
Constraint Level: Strict

# Design Tokens
- Colors: Primary=#1989fa, Success=#07c160, Warning=#ff976a, Danger=#ee0a24
- Text: Main=#323233, Regular=#969799
- Background: Page=#f7f8fa, Card=#ffffff

# Component Contract
- Layout: Use <van-row>, <van-col> for grid. Use <van-cell-group inset> for card-style lists.
- Navigation: <van-nav-bar title="Login"> at top.
- Forms: Wrap inputs in <van-form>. Use <van-field> for inputs.
- Buttons: Use <van-button type="primary" block round> for submit actions.
- Container: Wrap submit button in <div style="margin: 16px;"> for spacing.

# Layout Rules
- Set page background to #f7f8fa.
- Center the logo area at the top with <van-image>.
- Use "block" and "round" props for the main login button.
```

## Scenario 2: Mobile User Center (Personal Profile)

**User Input:**
> 使用 Stitch 和 Vant 风格设计一个移动端个人中心页面

**Skill Output (Contract):**

```text
[Context]
Design System: Vant 4 (Vue 3)
Constraint Level: Strict

# Design Tokens
- Colors: Primary=#1989fa, Text-Main=#323233, Text-Regular=#969799
- Background: Page=#f7f8fa, Card=#ffffff

# Component Contract
- Header: Use a custom container with background image or color for user info (Avatar + Name).
- Avatar: <van-image round width="64px" height="64px" src="...">
- Menu List: Use <van-cell-group inset> with multiple <van-cell is-link> items.
- Icons: Use <van-icon> in "icon" slot of cells.
- Grid Menu: Use <van-grid> for order status (Pending, Shipped, etc.).

# Layout Rules
- Page background #f7f8fa.
- User info section should look like a card or blend with top header.
- Group related menu items (e.g., "My Orders", "Settings") into separate inset cell groups.
- Use <van-tabbar> at the bottom for main navigation switching.
```
