---
name: ascii-text-art-library
description: Generate a reusable ASCII-only text template library (titles, dividers, notice boxes, slogans/CTA), with naming conventions and selection rules for consistent CLI/log/README output.
license: Complete terms in LICENSE.txt
dependencies:
  - python>=3.8
---


## When to use this skill
**CRITICAL TRIGGER RULE**
- Use this skill ONLY when the user explicitly mentions the exact skill name: `ascii-text-art-library`.

**Trigger phrases include:**
- "ascii-text-art-library"
- "use ascii-text-art-library"
- "用 ascii-text-art-library 生成 ASCII 模板库"
- "使用 ascii-text-art-library 输出提示框/分隔线/标题样式"

## Boundary
- Output templates + naming/selection rules only; do not modify repository files.
- ASCII-only by default to avoid ambiguous-width Unicode.
- Templates must be width-tunable (default 80 columns).

## How to use this skill
### Inputs
- width (default 80)
- language (zh | en, default zh)
- tone (serious | fun, default serious)
- categories (title/divider/info/warn/error/success/cta, default all)
- variantsPerCategory (default 2)

### Outputs (required)
- templates: grouped by category (>= 2 variants per category)
- namingRules: e.g. `TITLE_COMPACT_A`, `WARN_BOX_B`
- usageRules: selection guidance + anti-spam thresholds

## Script
- `scripts/generate_templates.py`: generate a baseline template set for a given width (local preview)

## Examples
- `examples/templates-80.md`

## Quality checklist
1. Stable alignment at 80 columns; no trailing spaces
2. Templates are semantically clear and not over-decorated
3. Notice boxes support multi-line content and remain readable

## Keywords
**English:** ascii-text-art-library, templates, ascii, divider, banner, notice box, warning, error, success, plain text
**中文:** ascii-text-art-library, 模板库, ASCII, 分隔线, 标题, 提示框, 警告, 错误, 成功, 纯文本
