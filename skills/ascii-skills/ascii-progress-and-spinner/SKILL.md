---
name: ascii-progress-and-spinner
description: "Design ASCII progress bars and spinners for CLI UX (determinate/indeterminate, TTY single-line refresh, non-interactive log fallback) with copy-pastable style specs. Use when the user needs terminal progress indicators, loading animations, or CLI feedback elements."
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

### Inline Style Examples

**Progress bar styles:**
```
Style 1 (block):   [████████░░░░░░░░░░░░]  42%  ETA 3s
Style 2 (hash):    [########............]  42%  ETA 3s
Style 3 (arrow):   [========>-----------]  42%  ETA 3s
```

**Spinner styles:**
```
Style 1 (braille): ⠋ Loading...  →  ⠙ Loading...  →  ⠹ Loading...
Style 2 (pipe):    | Loading...  →  / Loading...  →  - Loading...
```

**Non-TTY log fallback:**
```
[task-1] 25% complete
[task-1] 50% complete
[task-1] 75% complete
[task-1] 100% complete - done (4.2s)
```

### Workflow

1. Determine mode: `determinate` (known total) or `indeterminate` (spinner)
2. Select styles from the style gallery (>= 3 progress, >= 2 spinner)
3. Define render rules: TTY uses single-line refresh, non-TTY uses log lines
4. Define fallback rules for redirected output (no carriage returns)
5. **Validate**: Fixed-width percent field, no jitter, grep-friendly log mode

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
