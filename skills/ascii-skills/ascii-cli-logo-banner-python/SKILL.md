---
name: ascii-cli-logo-banner-python
description: Generate copy-pastable ASCII banners with a built-in font (no external font deps), including compact fallback and optional ANSI 256 coloring for the logo.
license: Complete terms in LICENSE.txt
dependencies:
  - python>=3.8
---


## When to use this skill
**CRITICAL TRIGGER RULE**
- Use this skill ONLY when the user explicitly mentions the exact skill name: `ascii-cli-logo-banner-python`.

**Trigger phrases include:**
- "ascii-cli-logo-banner-python"
- "use ascii-cli-logo-banner-python"
- "用 ascii-cli-logo-banner-python 生成启动 Banner"
- "使用 ascii-cli-logo-banner-python 输出 ASCII Logo + slogan（居中）"

## Boundary
- Output copy-pastable text and layout rules only. Do not modify project code.
- Default output is width-safe and copy/paste safe (no trailing spaces).
- ANSI coloring is optional and MUST be applied to visible characters only (spaces are not colorized).
- This skill uses a built-in 5x5 font. It is not a full FIGlet engine.

## How to use this skill
### Inputs (recommended)
- brand (required)
- width (default 80; if `< 60` use compact mode)
- slogan (optional; centered line under the logo)
- hint (optional; centered line under the slogan)
- glyph (ascii | block, default ascii)
- center (default true)
- rule (default true; set false for hero output)
- version/repo/docs/author (optional; only used when `rule=true`)
- colorMode (none | ansi256, default none; logo only)
- colorStart/colorEnd (0-255, defaults 33/129; only when `colorMode=ansi256`)

### Outputs (required)
- bannerPlain: banner text (ASCII-only when colorMode=none)
- compactPlain: compact banner when width < 60
- plainTextFallback: if colorMode is enabled, also provide a no-color fallback (same layout)

## Script
- `scripts/generate_banner.py`

## Examples
- `examples/banner-80.md`
- `examples/banner-compact.md`
- `examples/banner-slogan-centered.md`
- `examples/color-ansi256.md`

## Quality checklist
1. 80-column output does not wrap; no trailing spaces
2. Width < 60 uses compact mode
3. Color mode does not break alignment (spaces are not colorized)
4. Never prints secrets (tokens, internal URLs, personal data)

## Keywords
**English:** ascii-cli-logo-banner-python, ascii, banner, logo, cli, terminal, startup, slogan, ansi256
**中文:** ascii-cli-logo-banner-python, ASCII 启动横幅, 终端 Banner, 居中标语, ANSI256 上色
