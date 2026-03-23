---
name: ascii-cli-logo-banner-figletjs
description: Generate TAAG/FIGlet-style ASCII art banners using figlet.js (FIGfont spec), with layout controls (horizontal/vertical layout, width, whitespaceBreak) and optional ANSI 256 coloring.
license: Complete terms in LICENSE.txt
dependencies:
  - node>=18
  - npm
  - figlet (npm, powered by figlet.js)
---


## When to use this skill
**CRITICAL TRIGGER RULE**
- Use this skill ONLY when the user explicitly mentions the exact skill name: `ascii-cli-logo-banner-figletjs`.

**Trigger phrases include:**
- "ascii-cli-logo-banner-figletjs"
- "use ascii-cli-logo-banner-figletjs"
- "用 ascii-cli-logo-banner-figletjs 生成 TAAG/FIGlet 大字"
- "使用 ascii-cli-logo-banner-figletjs 调 horizontalLayout / verticalLayout"

## Boundary
- Output copy-pastable text and layout rules only. Do not modify project code.
- FIGlet/TAAG style is driven by FIGfont (.flf) rendering and layout “smushing/kerning” options.
- ANSI coloring is optional and MUST not break alignment (spaces are not colorized).
- Dependency note: `figlet` npm package is commonly used as the Node interface and is powered by `figlet.js`.

## How to use this skill
### Inputs (recommended)
- brand (required)
- width (default 80; if `< 60` use compact mode)
- font (default Standard)
- horizontalLayout (default | full | fitted | controlled smushing | universal smushing)
- verticalLayout (default | full | fitted | controlled smushing | universal smushing)
- whitespaceBreak (true|false, default true)
- slogan/hint (optional; centered lines under the logo)
- center (default true)
- rule (default true; set false for hero output)
- version/repo/docs/author (optional; only used when `rule=true`)
- colorMode (none | ansi256, default none; logo only)
- colorStart/colorEnd (0-255, defaults 33/129; only when `colorMode=ansi256`)

### Outputs (required)
- bannerPlain: banner text (no-color)
- coloredText: when `colorMode=ansi256`, provide colored logo output
- plainTextFallback: when colored, also provide a no-color fallback (same layout)

## Script
- `scripts/figlet_banner.mjs`

## Examples
- `examples/taag-figlet.md`
- `examples/color-ansi256.md`

## Quality checklist
1. Layout options are honored (horizontal/vertical layout)
2. 80-column output does not wrap; no trailing spaces
3. Color mode does not break alignment (spaces are not colorized)
4. Never prints secrets (tokens, internal URLs, personal data)

## Keywords
**English:** ascii-cli-logo-banner-figletjs, figlet, figlet.js, FIGfont, taag, ascii, banner, smushing, kerning, ansi256
**中文:** ascii-cli-logo-banner-figletjs, FIGlet 大字, TAAG, FIGfont 字体, 横向布局, 纵向布局, ANSI256 上色
