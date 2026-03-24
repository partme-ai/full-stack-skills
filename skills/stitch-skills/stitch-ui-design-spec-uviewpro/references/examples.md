# Example: uView Pro Design Contract (Stitch Integration)

## Trigger Keywords

- Mention "Stitch" AND `uview pro` / `uview-pro` / `uviewpro` keywords.
- Examples (Chinese):
  - 使用 Stitch 和 uView Pro 风格设计一个电商首页
  - 使用 Stitch 和 uView Pro 风格重构个人设置页
- Examples (English):
  - Use Stitch in uView Pro style to design a mobile dashboard.
  - Create a login form using Stitch and uView Pro components.

## References

- Full Contract & Constraints: [references/contract.md](./contract.md)
- Official References: [references/official.md](./official.md)

## Expected Behavior

1. This skill outputs uView Pro hard constraints prefix (tokens/primary=#3c9cff/u- prefix, etc.).
2. The orchestrator appends it as `[Context]` prefix to the Stitch Prompt.
3. Subsequent generation uses `u-*` components (same prefix as uView 2; package uview-pro), `uni.$u` utilities, and `rpx` units.

## Scenario 1: E-commerce Home Page

**User Input:**
> 使用 Stitch 和 uView Pro 风格设计一个电商首页

**Skill Output (Contract):**

```text
[Context]
Design System: uView Pro (Vue 3)
Constraint Level: Strict

# Design Tokens
- Colors: Primary=#3c9cff, Price=#f56c6c
- Unit: rpx

# Component Contract
- Search: <u-search placeholder="Search products">.
- Banner: <u-swiper :list="bannerList" height="300">.
- Grid Nav: <u-grid :col="4"><u-grid-item>...</u-grid-item></u-grid>.
- Product List: <u-waterfall v-model="flowList">.
  - Card: Custom <view class="demo-warter"> using <u-image> and <u-text>.

# Layout Rules
- Use <u-sticky> for search bar.
- Use <u-loadmore> at bottom.
- Use <u-back-top> for long lists.
```
