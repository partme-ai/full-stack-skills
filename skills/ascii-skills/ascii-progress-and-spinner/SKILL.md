---
name: ascii-progress-and-spinner
description: Design ASCII progress bars and spinners for CLI UX (determinate/indeterminate, TTY single-line refresh, non-interactive log fallback) with copy-pastable style specs.
license: Complete terms in LICENSE.txt
dependencies:
  - python>=3.8
---


## When to use this skill
**CRITICAL TRIGGER RULE**
- Use this skill ONLY when the user explicitly mentions the exact skill name: `ascii-progress-and-spinner`.

**Trigger phrases include:**
- "ascii-progress-and-spinner"
- "use ascii-progress-and-spinner"
- "用 ascii-progress-and-spinner 生成 ASCII 进度条"
- "使用 ascii-progress-and-spinner 做 spinner / loading"

## Boundary
- Do not integrate a specific UI framework; output styles + refresh rules + fallback protocol + examples.
- Must cover:
  - determinate progress bars
  - indeterminate spinners
  - non-TTY / redirected-output fallback (log lines, no carriage-return updates)

## How to use this skill
### Inputs
- mode (determinate | indeterminate)
- width (default 40)
- showPercent (default true)
- showEta (optional)
- multiTask (optional)
- colorMode (none | ansi256, default none)

### Outputs (required)
- progressBarStyles (>= 3)
- spinnerStyles (>= 2)
- renderRules (TTY single-line refresh vs logLines)
- fallbackRules (non-interactive / redirected output)

### Recommended render rules
- **TTY (interactive):** single-line refresh (overwrite previous line), avoid log spam
- **Non-TTY (logs):** print log lines (no overwrite). Each line may include task name + percent.

## Script
- `scripts/demo.py`: local demo for progress bar + spinner shapes

## Examples
- `examples/styles.md`

## Quality checklist
1. Fixed width (percent field is fixed-width to avoid jitter)
2. Log mode is grep-friendly (no overwrite)
3. ASCII-only defaults are available (avoid ambiguous-width Unicode)

## Keywords
**English:** ascii-progress-and-spinner, progress bar, spinner, loading, tty, non-interactive, log output, ascii
**中文:** ascii-progress-and-spinner, 进度条, Spinner, Loading, 终端, TTY, 日志降级, ASCII
