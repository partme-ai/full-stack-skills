---
name: ascii-motd-profile-banner
description: Generate ASCII-only MOTD / SSH login banner / shell profile welcome messages (short/long variants, quiet mode guidance, security notices).
license: Complete terms in LICENSE.txt
---


## When to use this skill
**CRITICAL TRIGGER RULE**
- Use this skill ONLY when the user explicitly mentions the exact skill name: `ascii-motd-profile-banner`.

**Trigger phrases include:**
- "ascii-motd-profile-banner"
- "use ascii-motd-profile-banner"
- "用 ascii-motd-profile-banner 生成 SSH 登录欢迎"
- "使用 ascii-motd-profile-banner 输出 MOTD（短版/长版）"

## Boundary
- Produce templates and placement guidance only; do not modify system files.
- Never include sensitive information (tokens, internal URLs, account details, personal data).
- Default output is ASCII-only; ANSI color is optional and must have a no-color fallback.

## How to use this skill
### Inputs
- title (required)
- messageBullets (1–5 bullet points, required)
- mode (short | long, default short)
- width (default 80)
- includeLinks (optional: Docs / Tickets / Repo)
- colorMode (none | ansi256, default none)
- quietHint (default true: recommend quiet output for non-interactive shells)

### Outputs (required)
- bannerShort (<= 12 lines)
- bannerLong (<= 30 lines)
- safetyNotes (>= 3 actionable security notes)
- toggleAdvice (interactive vs non-interactive display guidance)

## Examples
- `examples/ssh-short.md`
- `examples/ssh-long.md`

## Quality checklist
1. Short mode does not spam (<= 12 lines)
2. Copy/paste safe (no trailing spaces)
3. Security notes are clear, short, and actionable

## Keywords
**English:** ascii-motd-profile-banner, motd, ssh banner, profile, welcome message, security notice, terminal
**中文:** ascii-motd-profile-banner, MOTD, SSH Banner, 登录欢迎, Profile, 安全提示, 终端
