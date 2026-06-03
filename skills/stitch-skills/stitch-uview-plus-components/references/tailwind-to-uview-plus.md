# Tailwind → uview-plus Mapping

Convert Tailwind-heavy Stitch HTML into `uview-plus` structure, `rpx`, and theme variables. Do not emit Tailwind classes in the final page unless the target project explicitly uses Tailwind.

## 1. Spacing

| Tailwind | Approx px | Use in output |
|---|---:|---|
| `p-2` | 8 | `16rpx` |
| `p-3` | 12 | `24rpx` |
| `p-4` | 16 | `32rpx` |
| `p-5` | 20 | `40rpx` |
| `px-4` | 16 | `padding-left/right: 32rpx` |
| `py-3` | 12 | `padding-top/bottom: 24rpx` |
| `gap-2` | 8 | `16rpx` or `up-gap` |
| `gap-4` | 16 | `32rpx` or `up-gap` |
| `space-y-4` | 16 | child margin or `up-gap` |

## 2. Typography

| Tailwind | Approx px | Use in output |
|---|---:|---|
| `text-xs` | 12 | `24rpx` |
| `text-sm` | 14 | `28rpx` |
| `text-base` | 16 | `30rpx` |
| `text-lg` | 18 | `36rpx` |
| `font-medium` | 500 | `font-weight: 500` |
| `font-bold` | 700 | `font-weight: 700` |

Prefer `var(--up-content-color)` / `var(--up-main-color)` / related theme variables instead of hardcoded text colors.

## 3. Colors

| Tailwind / Stitch token | Prefer in output |
|---|---|
| `bg-white` | card/container background or `up-card` |
| `bg-gray-50` | `var(--up-bg-color)` or a themed container |
| `text-primary` / brand blue | `var(--up-primary)` when applicable |
| `text-gray-500` | `var(--up-tips-color)` or `var(--up-content-color)` |
| `border-gray-200` | `var(--up-border-color)` |

## 4. Radius and shadows

| Tailwind | Use in output |
|---|---|
| `rounded` | `8rpx` |
| `rounded-lg` | `16rpx` |
| `rounded-xl` | `20rpx` |
| `rounded-full` | pill / circle |
| `shadow-sm` / `shadow-soft` | prefer `up-card`, otherwise a lightweight box shadow |

## 5. Structural conversions

| Tailwind pattern | uview-plus rewrite |
|---|---|
| `sticky top-0` | `up-navbar` or `up-status-bar` + custom header |
| `sticky bottom-0` | `up-safe-bottom` |
| `grid grid-cols-2` | `up-row` + `up-col` or explicit flex grid |
| `divide-y` | `up-line` / `up-divider` |
| dashed upload box | `up-upload` |
| tab strip | `up-tabs` / `up-subsection` |

## 6. Theme guidance

- Prefer `var(--up-*)` in page styles.
- If the generated output needs a note about runtime theming, reference `setConfig({ color })`.
- If the design contains dark-mode intent, keep the page styles token-based so they naturally follow the active theme.
