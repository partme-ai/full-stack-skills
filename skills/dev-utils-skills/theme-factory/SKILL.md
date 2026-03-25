---
name: theme-factory
description: "Applies professional color and font themes to slides, documents, reports, and HTML pages. Includes 10 pre-set themes (Ocean Depths, Sunset Boulevard, Modern Minimalist, etc.) with hex palettes and font pairings, plus on-the-fly custom theme generation. Use when the user wants to style or re-theme any visual artifact."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Apply a consistent color/font theme to a slide deck, document, report, or landing page
- Preview available themes before choosing one
- Generate a custom theme from a description (e.g., "warm corporate" or "playful startup")
- Re-theme an existing artifact with a different visual identity

## How to use this skill

### Workflow

1. **Show the theme showcase** - Display `theme-showcase.pdf` so the user can visually compare all 10 themes
2. **Ask for their choice** - Let the user pick a theme or describe a custom one
3. **Wait for confirmation** - Get explicit approval before applying
4. **Apply the theme** - Read the theme file from `themes/` and apply colors/fonts consistently

### Available Themes

| # | Theme | Style | Primary Color |
|---|-------|-------|--------------|
| 1 | Ocean Depths | Professional, calming | Maritime blues |
| 2 | Sunset Boulevard | Warm, vibrant | Orange/coral |
| 3 | Forest Canopy | Natural, grounded | Earth greens |
| 4 | Modern Minimalist | Clean, contemporary | Grayscale |
| 5 | Golden Hour | Rich, warm | Autumnal golds |
| 6 | Arctic Frost | Cool, crisp | Winter blues |
| 7 | Desert Rose | Soft, sophisticated | Dusty pinks |
| 8 | Tech Innovation | Bold, modern | Electric blues |
| 9 | Botanical Garden | Fresh, organic | Garden greens |
| 10 | Midnight Galaxy | Dramatic, cosmic | Deep purples |

### Applying a Theme (example)

```css
/* Example: Ocean Depths theme applied via CSS variables */
:root {
  --color-primary: #1B4F72;
  --color-secondary: #2E86C1;
  --color-accent: #AED6F1;
  --color-background: #EBF5FB;
  --color-text: #1C2833;
  --font-heading: 'Playfair Display', serif;
  --font-body: 'Source Sans Pro', sans-serif;
}
```

### Custom Theme Generation

When no preset fits, create a custom theme:
1. Ask the user for a mood/description (e.g., "energetic tech startup")
2. Generate a palette of 4-5 harmonious hex colors
3. Select complementary heading and body fonts
4. Name the theme descriptively
5. Show for review, then apply

## Best Practices

1. **Contrast check** - Ensure text/background combinations meet WCAG AA contrast ratios
2. **Consistency** - Apply the same theme tokens to every slide/page, never mix themes
3. **Font pairing** - Use one display font for headings and one readable font for body text
4. **Accent sparingly** - Use accent colors for highlights and CTAs, not large surfaces

## Keywords

theme, styling, color palette, font pairing, slides, presentation, design, visual identity, 主题, 配色, 样式
