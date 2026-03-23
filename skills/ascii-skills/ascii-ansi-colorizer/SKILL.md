---
name: ascii-ansi-colorizer
description: Add an ANSI color layer to existing ASCII/plain-text output (gradient/rainbow/highlights) with alignment-safe rules and a required no-color fallback.
license: Complete terms in LICENSE.txt
dependencies:
  - python>=3.8
---


## When to use this skill
**CRITICAL TRIGGER RULE**
- Use this skill ONLY when the user explicitly mentions the exact skill name: `ascii-ansi-colorizer`.

**Trigger phrases include:**
- "ascii-ansi-colorizer"
- "use ascii-ansi-colorizer"
- "用 ascii-ansi-colorizer 给 ASCII 上色"
- "使用 ascii-ansi-colorizer 做 ANSI 渐变/彩虹"

## Boundary
- This skill only adds color to existing text. It does not generate the ASCII art itself (pair with `ascii-cli-logo-banner` if needed).
- Required outputs: `coloredText` + `plainTextFallback`.
- ANSI must not break alignment: do not colorize spaces by default; colorize visible characters only.

## How to use this skill
### Inputs
- textOrAscii (required)
- palette (rainbow | gradient | brandColors)
- direction (leftToRight | topToBottom, default leftToRight)
- colorDepth (ansi16 | ansi256 | truecolor, default ansi256)
- scope (logoOnly | highlightsOnly | fullText, default logoOnly)

### Outputs (required)
- coloredText: ANSI-colored output
- plainTextFallback: no-color fallback (identical content, no ANSI)
- compatNotes: copy/paste and redirection guidance (NO_COLOR / --no-color suggestions)

### Steps
1. Pick `colorDepth` (default: ansi256).
2. Choose a stable coloring strategy:
   - Column-wise gradients (leftToRight) are usually the safest
   - Colorize non-space characters only
3. Output both `coloredText` and `plainTextFallback`.
4. Provide no-color guidance (semantic suggestions): `NO_COLOR` / `--no-color`.

## Script
- `scripts/colorize.py`: apply ANSI 256 gradient or rainbow to stdin

## Examples
- `examples/gradient.md`

## Quality checklist
1. Removing ANSI keeps the same readable content (`plainTextFallback`).
2. Alignment does not change after coloring.
3. Colors should not overpower the informational lines.

## Keywords
**English:** ascii-ansi-colorizer, ansi, color, gradient, rainbow, terminal, no-color, plain text, ascii
**中文:** ascii-ansi-colorizer, ANSI, 上色, 渐变, 彩虹, 终端, 无色回退, 纯文本, ASCII
