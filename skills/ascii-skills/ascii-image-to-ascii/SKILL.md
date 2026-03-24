---
name: ascii-image-to-ascii
description: Convert an image into ASCII art (readable + detail variants, width/charset controls, optional ANSI), for terminal previews and plain-text “image substitutes”.
license: Complete terms in LICENSE.txt
dependencies:
  - python>=3.8
  - pillow
---


## When to use this skill
**CRITICAL TRIGGER RULE**
- Use this skill ONLY when the user explicitly mentions the exact skill name: `ascii-image-to-ascii`.

**Trigger phrases include:**
- "ascii-image-to-ascii"
- "use ascii-image-to-ascii"
- "用 ascii-image-to-ascii 把图片转字符画"
- "使用 ascii-image-to-ascii 生成可读优先/细节优先两版"

## Boundary
- Default output is ASCII-only; ANSI coloring is optional.
- The bundled script is for local conversion/verification only. Do not fetch/upload images on the user’s behalf.
- Always give pre-processing advice (crop subject, raise contrast, simplify background) before generating the final ASCII art.

## How to use this skill
### Inputs
- imagePath (local path, required)
- width (default 100; common: 80/100/120)
- charset (default ` .:-=+*#%@`, from light to dark)
- mode (readable | detail; if outputting both, this can be ignored)
- background (light | dark | unknown, default unknown)
- colorMode (none | ansi256, default none)

### Outputs (required)
- asciiReadable: readable-first (less noise, clearer silhouette)
- asciiDetail: detail-first (more levels, richer texture)
- paramsGuide: recommended width/charset + pre-processing tips
- pitfalls: 3-5 common failure modes with fixes

### Steps
1. Pre-processing advice (required):
   - Crop the subject, remove irrelevant background
   - Increase contrast to reduce gradient noise
   - Target width usually 80–120 columns
2. Charset + mapping direction:
   - Space is the lightest, `@` is the darkest (or invert consistently)
3. Generate two variants:
   - readable: fewer levels (less noise)
   - detail: more levels (more texture)
4. Optional ANSI:
   - Use color only as a hint; keep the silhouette readable
   - Always provide a no-color fallback

## Script
- `scripts/image_to_ascii.py`
  - Requires Python + Pillow (`pip install pillow`)
  - Supports: readable/detail variants, optional `--ansi256`

## Examples
- `examples/readable-vs-detail.md`

## Quality checklist
1. Lines are consistent and `<= width`
2. The readable variant must preserve the main silhouette
3. No trailing spaces (copy/paste safe)

## Keywords
**English:** ascii-image-to-ascii, image to ascii, ascii art, terminal preview, charset, grayscale, dithering, ansi
**中文:** ascii-image-to-ascii, 图片转字符画, ASCII 字符画, 终端预览, 字符集, 灰度映射, 降噪, ANSI 彩色
