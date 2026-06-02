---
name: skill-official-evaluation
description: >
    Evaluate any Agent Skill against the official Agent Skills specification (agentskills.io) and best practices, and produce an official-style assessment report. This skill checks: SKILL.md frontmatter compliance (name, description, license fields), directory structure conventions, progressive disclosure quality, description triggering accuracy, script safety (non-interactive, --help, structured output, no secrets), and security hygiene. The evaluation conclusion is explicitly based on the official specification and best practices published at agentskills.io, not subjective opinion. Use when the user asks to review a skill for spec compliance, check skill structure, audit skill quality against official standards, assess description triggering quality, inspect script safety, or generate an official evaluation report. Also use when the user mentions "审查技能合规", "官方规范评估", "Skill 规范检查", "技能安全审计", "检查 SKILL.md 格式", "生成官方评估报告", "根据官方规范评估技能".
license: Apache-2.0
---

## When to use this skill

**ALWAYS use this skill when the user asks to:**
- Review a skill for compliance with the official Agent Skills specification
- Check whether a skill's frontmatter, directory structure, or naming follows the rules
- Evaluate a skill's description triggering quality against official best practices
- Audit a skill's script safety (non-interactive, `--help`, secrets, structured output)
- Generate an official-style evaluation report with Pass/Needs-improvement conclusions
- Verify progressive disclosure is implemented correctly
- Scan for security issues (hardcoded secrets, suspicious instructions)
- "审查技能合规" (review skill compliance), "官方规范评估" (official spec evaluation)
- "Skill 规范检查" (skill spec check), "技能安全审计" (skill security audit)
- "检查 SKILL.md 格式" (check SKILL.md format), "检查技能结构" (check skill structure)
- "生成官方评估报告" (generate official evaluation report)
- "根据官方规范评估技能" (evaluate skill against official spec)
- "这个 Skill 符合规范吗" (does this skill comply with the spec)

**Trigger phrases include:**
- "帮我审查这个 Skill 是否符合规范" (help me review whether this skill complies with spec)
- "检查这个技能的 SKILL.md 格式对不对" (check if this skill's SKILL.md format is correct)
- "这个技能的 frontmatter 合规吗" (is this skill's frontmatter compliant)
- "审计一下这个技能的脚本安全性" (audit this skill's script safety)
- "按照 agentskills.io 规范评估这个技能" (evaluate this skill against agentskills.io spec)
- "review this skill for official spec compliance"
- "check if my skill follows the official specification"
- "generate an official evaluation report for this skill"
- "does this skill meet the agentskills.io requirements"

**When NOT to use (near-miss boundaries):**
- User wants a multi-dimensional quality score with radar charts → use `skill-trace-evaluation` instead (TRACE model covers T/R/A/C/E, while official evaluation focuses on spec compliance)
- User wants to learn how to design a skill (know the rules, not evaluate a specific skill) → use `skill-awesome` instead
- User wants to organize skill documentation into an index → use `skill-awesome` instead
- User asks for general code review (not related to Agent Skills) → this skill is scoped to Agent Skills ecosystem only

**IMPORTANT: Official Evaluation vs TRACE Evaluation — Two Different Evaluation Models:**

This skill and `skill-trace-evaluation` evaluate skills using different frameworks:

- **Official Evaluation (this skill)**: Based on the official Agent Skills specification from agentskills.io. Checks structural compliance, naming rules, frontmatter correctness, and script safety. Answers "Does this skill follow the rules?"

- **TRACE Evaluation (different skill)**: Based on the SkillHub TRACE quality model. Scores across Trust, Reliability, Adaptability, Convention, and Effectiveness. Produces radar charts and per-dimension scores. Answers "How good is this skill?"

**When both skills could apply:**
- If the user says "evaluate this skill" or "review this skill" without specifying a framework, ask: "I can evaluate this skill using either the official specification (agentskills.io compliance) or the TRACE quality model (five-dimension scoring with radar charts). Which would you prefer?"
- If the user explicitly mentions "official spec", "agentskills.io", "compliance", "format check" → use this skill
- If the user explicitly mentions "TRACE", "quality score", "radar chart", "five dimensions" → use `skill-trace-evaluation`

## How to use this skill

**CRITICAL: This skill evaluates a target skill against the official Agent Skills specification. The evaluation conclusion is explicitly based on the official specification and best practices published at agentskills.io. Do not invent requirements not present in the official sources.**

To evaluate a skill:

### Step 1: Identify the target skill

- **Preferred input**: Path to the target skill directory
- The target must contain a `SKILL.md` file. If not found, report "SKILL.md not found" and stop.
- Also inspect optional directories: `scripts/`, `references/`, `assets/`.
- If the user provides a `.skill` or `.zip` archive, only unpack when explicitly asked; otherwise evaluate from provided excerpts.

### Step 2: Apply the official rubric

Use [references/official-rubric.md](references/official-rubric.md) as the evaluation checklist. The rubric has five inspection dimensions:

#### Dimension 1: Spec Compliance (MUST pass)

| Check | What to verify |
|-------|---------------|
| **SKILL.md exists** | The skill root must contain a `SKILL.md` file |
| **Frontmatter present** | YAML frontmatter delimited by `---` at the top of SKILL.md |
| **`name` field** | Must match the parent directory name. Lowercase letters, digits, and hyphens only. 1-64 characters. No leading/trailing hyphens, no consecutive `--`. |
| **`description` field** | Non-empty, max 1024 characters. Must describe both what the skill does AND when to use it. Should not be overly broad. |
| **Optional fields format** | If `license`, `compatibility`, `metadata`, or `allowed-tools` are present, verify their formatting is valid. |
| **Directory structure** | Optional directories must follow conventions: `scripts/` for executable code, `references/` for on-demand docs, `assets/` for templates and resources. |

#### Dimension 2: Progressive Disclosure Quality (SHOULD meet)

| Check | What to verify |
|-------|---------------|
| **SKILL.md conciseness** | Body stays concise and actionable. Ideally under 500 lines / 5000 tokens. |
| **Details in references/** | Long explanations, reference tables, and supplementary content moved to `references/`. |
| **Clear reference triggers** | When a reference file is mentioned, the skill tells the agent WHEN to load it ("Read `references/api-errors.md` if the API returns a non-200 status code"). |
| **No deep reference chains** | References should be one level deep from SKILL.md. Avoid references that point to other references. |

#### Dimension 3: Description Triggering Quality (SHOULD meet)

| Check | What to verify |
|-------|---------------|
| **User-intent language** | Description uses words users would naturally say, not implementation jargon. |
| **Not implementation-only** | Description goes beyond "Processes X files" — it tells the agent when the user needs X processed. |
| **Trigger boundaries** | Description contains both "should trigger" and "should not trigger" signals where applicable. |

#### Dimension 4: Script Readiness (CONDITIONAL — only if `scripts/` exists)

Use [references/script-safety-checklist.md](references/script-safety-checklist.md) to verify:

| Check | Requirement |
|-------|-------------|
| **Non-interactive** | No TTY prompts. All inputs via flags, env vars, or stdin. |
| **`--help` available** | Prints usage, options, and examples. |
| **Clear error messages** | Errors say what failed, what was expected, and what to try next. |
| **No secrets** | No hardcoded tokens, keys, or passwords. |
| **Safe defaults** | Destructive operations require `--force` or `--confirm`. |
| **Structured output** (recommended) | `--format json` option. Data to stdout, diagnostics to stderr. |
| **Idempotency** (recommended) | Repeated runs do not corrupt state. |

#### Dimension 5: Security Hygiene (MUST pass)

| Check | What to verify |
|-------|---------------|
| **No secrets in files** | Scan SKILL.md, scripts, and other text files for hardcoded tokens, API keys, passwords. |
| **No suspicious instructions** | The skill must not instruct the agent to download from untrusted sources, exfiltrate data, or execute obfuscated code. |
| **Risky operations guidance** | If the skill involves destructive operations, it must instruct the agent to get explicit user confirmation. |

### Step 3: Run the evaluator script (recommended)

The bundled script automates data collection and formatting:

```bash
python3 scripts/official_evaluate.py --help

# Generate a Markdown evaluation report
python3 scripts/official_evaluate.py --skill-dir <path> --format md

# Generate machine-readable JSON
python3 scripts/official_evaluate.py --skill-dir <path> --format json

# Write to a file
python3 scripts/official_evaluate.py --skill-dir <path> --format md --output report.md
```

The script performs automated checks for:
- SKILL.md presence and frontmatter parsing
- Name format validation (regex) and directory match
- Description length validation
- License field check
- Secret pattern scanning (AWS keys, API keys, token patterns)
- Non-interactive pattern detection in scripts

**After running the script**, you MUST supplement the automated results with qualitative assessment for:
- Progressive disclosure quality (is the body concise? are references well-triggered?)
- Description triggering quality (does it use user-intent language? are trigger boundaries clear?)
- Security hygiene beyond regex patterns (are there suspicious instructions?)

### Step 4: Produce the evaluation report

The report MUST include these sections, in order:

#### Report structure

```md
# Official Skill Evaluation Report

Target: `<path-to-skill-directory>`

## Conclusion

- Overall conclusion: **Pass** / **Needs improvement** / **Fail**
- Top issues:
  1. ...
  2. ...
  3. ...

## Compliance Checklist

| Item | Result | Evidence | Suggestion |
|------|--------|----------|------------|
| SKILL.md frontmatter present | Pass/Fail | ... | ... |
| name matches directory | Pass/Fail | ... | ... |
| name format valid | Pass/Fail | ... | ... |
| description present & valid | Pass/Fail | ... | ... |
| license field | Pass/Needs improvement | ... | ... |
| Optional directories organized | Pass | ... | ... |
| Progressive disclosure | Pass/Needs improvement | ... | ... |
| Description trigger quality | Pass/Needs improvement | ... | ... |
| Script safety (if applicable) | Pass/Fail/N/A | ... | ... |
| Security & secrets scan | Pass/Fail | ... | ... |

## Risks & Limitations

- ...

## Improvement Suggestions (prioritized)

1. ...
2. ...
3. ...
```

#### Conclusion levels

| Level | Criteria |
|-------|----------|
| **Pass** | All MUST items pass. SHOULD items are reasonably met. No security findings. |
| **Needs improvement** | All MUST items pass, but SHOULD items have significant gaps. No security findings. |
| **Fail** | One or more MUST items fail, OR security findings detected. |

#### Evidence rules

- Every Pass/Fail MUST include specific evidence: a file path, a field value, a line number, or a scan result.
- Do NOT use subjective language like "seems good" or "looks fine". Cite artifacts.
- If a check is N/A (e.g., no `scripts/` directory), state "N/A — no scripts/ directory" as evidence.

## Output format

After producing the evaluation report:

1. State the overall conclusion clearly: "**Pass**", "**Needs improvement**", or "**Fail**"
2. List the top 3 most important findings
3. Show the compliance checklist table with evidence
4. Provide prioritized, actionable improvement suggestions
5. Save the report if the user requests a file; otherwise display inline

## Rules

1. **Do not invent "official requirements"** not present in the official sources above. Every finding must be traceable to the official specification or best practices.
2. **Do not include secrets** or reproduce sensitive content in the report. If secrets are found, note their location without reproducing the secret value.
3. **Treat the rubric as the ground truth**. If [references/official-rubric.md](references/official-rubric.md) says a check is "Should", do not report it as a hard failure.
4. **The evaluation conclusion is explicitly based on the official specification**. The report should state this clearly in the opening paragraph.

## Keywords

**English keywords:**
official-evaluation, spec-compliance, skill-review, skill-audit, frontmatter-check, naming-validation, description-quality, script-safety, security-scan, progressive-disclosure, official-rubric, agentskills-spec, skill-assessment, compliance-report, skill-inspection, format-check, structure-review

**Chinese keywords (中文关键词):**
审查技能合规, 官方规范评估, Skill 规范检查, 技能安全审计, 检查 SKILL.md 格式, 检查技能结构, 生成官方评估报告, 根据官方规范评估技能, 技能合规检查, 技能评估报告, frontmatter 检查, 技能命名检查, 技能描述检查, 脚本安全检查, 渐进式披露检查, 官方规范审查
