---
name: skill-awesome
description: The canonical knowledge base for designing Agent Skills. Contains distilled Agent Skills specifications (naming conventions, frontmatter rules, directory structure, progressive disclosure), official best practices, description optimization techniques, script safety guidelines, and evaluation frameworks (TRACE). Use when designing a new skill, reviewing an existing skill for compliance, needing to know what makes a good skill, wondering about frontmatter rules or naming conventions, or when the user mentions "设计技能", "创建技能", "技能规范", "技能命名规则", "SKILL.md 怎么写", "frontmatter 规范", "技能最佳实践", "技能目录结构", "渐进式披露", "Agent Skills 规范".
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when you need to know:**
- What the Agent Skills specification requires (directory structure, SKILL.md format, frontmatter fields)
- What naming conventions to follow for a skill (`name` must match directory, lowercase + hyphens only, etc.)
- What frontmatter fields are required vs optional, and their constraints
- What progressive disclosure means and how to structure a skill to use it
- What the official best practices say about scope, context budgeting, gotchas, and checklists
- How to write a good `description` that triggers reliably
- What script safety rules apply (non-interactive, `--help`, no secrets, structured output)
- How the TRACE evaluation framework judges skill quality
- What a well-structured skill looks like (reference examples)
- "设计技能" (design a skill), "创建技能" (create a skill), "技能规范" (skill specification)
- "技能命名规则" (skill naming rules), "技能命名规范" (skill naming conventions)
- "SKILL.md 怎么写" (how to write SKILL.md), "frontmatter 规范" (frontmatter specification)
- "技能最佳实践" (skill best practices), "技能目录结构" (skill directory structure)
- "渐进式披露" (progressive disclosure), "Agent Skills 规范" (Agent Skills spec)
- "怎么写 description" (how to write description), "skill description 怎么写"
- "技能脚本安全" (skill script safety), "技能触发条件" (skill trigger conditions)

**Trigger phrases include:**
- "我要设计一个新的 Skill，告诉我规范" (I want to design a new skill, tell me the spec)
- "SKILL.md 的 frontmatter 有哪些字段" (what fields are in SKILL.md frontmatter)
- "技能的 name 有什么命名规则" (what are the naming rules for skill name)
- "怎么让技能的 description 触发更准确" (how to make skill description trigger more accurately)
- "技能的最佳实践有哪些" (what are the best practices for skills)
- "渐进式披露怎么用" (how to use progressive disclosure)
- "设计一个 Skill 需要注意什么" (what to pay attention to when designing a skill)
- "tell me the Agent Skills specification", "what makes a good skill"
- "how should I structure a skill directory", "skill frontmatter rules"

---

## 1. Agent Skills Specification

### 1.1 Directory Structure

Every skill is a folder containing at minimum a `SKILL.md` file:

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation loaded on demand
├── assets/           # Optional: templates, images, data files
└── LICENSE.txt       # Optional: license file
```

### 1.2 SKILL.md Format

The `SKILL.md` file must contain **YAML frontmatter** followed by **Markdown body**.

#### Required frontmatter fields

| Field | Required | Constraints |
|-------|:-------:|-------------|
| `name` | Yes | Max 64 characters. Lowercase letters (`a-z`), digits (`0-9`), and hyphens (`-`) only. Must NOT start or end with a hyphen. Must NOT contain consecutive hyphens (`--`). **Must match the parent directory name.** |
| `description` | Yes | Max 1024 characters. Non-empty. Must describe BOTH what the skill does AND when to use it. This is the primary mechanism the agent uses to decide whether to activate the skill. |

#### Optional frontmatter fields

| Field | Constraints |
|-------|-------------|
| `license` | License name or reference to a bundled license file (e.g., `LICENSE.txt`). Keep it short. |
| `compatibility` | Max 500 characters. Indicates environment requirements (intended product, system packages, network access). Only include if your skill has specific requirements. |
| `metadata` | Arbitrary key-value mapping for additional metadata. Use reasonably unique key names to avoid conflicts. |
| `allowed-tools` | Space-separated string of pre-approved tools the skill may use. Experimental — support varies between agent implementations. |

#### Name field rules (detailed)

```text
VALID names:
  mermaid              ✅ lowercase only
  roll-dice            ✅ lowercase + hyphen
  skill-awesome        ✅ lowercase + hyphen

INVALID names:
  My-Skill             ❌ uppercase
  -skill               ❌ starts with hyphen
  skill-               ❌ ends with hyphen
  skill--awesome       ❌ consecutive hyphens
  skill_name           ❌ underscore
  123skill             ❌ starts with digit (no, actually digits ARE allowed)
```

#### Body content rules

- No format restrictions — write whatever helps the agent perform the task.
- **Keep SKILL.md under 500 lines / 5000 tokens.** Move detailed reference material to `references/`.
- Recommended sections: step-by-step instructions, examples of inputs and outputs, common edge cases.

### 1.3 Progressive Disclosure

Agents load skills progressively in three stages:

| Stage | What loads | Token cost | When |
|-------|-----------|-----------|------|
| **Discovery** | Only `name` + `description` | ~100 tokens | Agent startup |
| **Activation** | Full `SKILL.md` body | <5000 tokens (recommended) | Task matches description |
| **Execution** | `references/`, `scripts/`, `assets/` | On demand | As needed during execution |

**Key implications for skill design:**
- The `description` carries the entire burden of triggering — if it doesn't convey when the skill is useful, the agent won't know to reach for it.
- Keep `SKILL.md` focused on core instructions. Tell the agent **when to load** reference files, not just that they exist: "Read `references/api-errors.md` if the API returns a non-200 status code."
- Avoid deeply nested reference chains — keep references one level deep from SKILL.md.

---

## 2. Best Practices for Skill Design

### 2.1 Start from Real Expertise

Do NOT ask an LLM to generate a skill from its general training knowledge — this produces vague, generic procedures. Ground skills in real, domain-specific context:

- **Extract from a hands-on task**: Complete a real task, then extract the reusable pattern. Capture steps that worked, corrections you made, input/output formats, and project-specific context.
- **Synthesize from existing project artifacts**: Internal documentation, runbooks, API specifications, code review comments, version control history, real-world failure cases.

### 2.2 Spend Context Wisely

Every token in your skill competes for the agent's attention.

| Do | Don't |
|----|-------|
| Add what the agent lacks (project conventions, domain procedures, edge cases) | Explain what the agent already knows (what a PDF is, how HTTP works) |
| Design coherent units (one skill = one cohesive workflow) | Scope too narrowly (many skills for one task) or too broadly (hard to trigger precisely) |
| Aim for moderate detail (concise stepwise guidance + working examples) | Be overly comprehensive (agent struggles to extract what's relevant) |
| Structure large skills with progressive disclosure | Put everything in SKILL.md |

Ask yourself about each piece of content: **"Would the agent get this wrong without this instruction?"** If no, cut it.

### 2.3 Calibrate Control

Match the specificity of instructions to the fragility of the task:

| Situation | Strategy |
|-----------|----------|
| Multiple valid approaches, task tolerates variation | Give the agent freedom. Explain *why* rather than rigid directives. |
| Operations are fragile, consistency critical, specific sequence required | Be prescriptive. Use exact commands, explicit sequences. |
| Multiple tools/approaches could work | Pick a default and mention alternatives briefly. Provide defaults, not menus. |
| Teaching a class of problems | Favor procedures ("how to approach") over declarations ("what to produce for one instance"). |

### 2.4 Effective Instruction Patterns

**Gotchas sections** — the highest-value content in many skills. Environment-specific facts that defy reasonable assumptions:

```markdown
## Gotchas
- The `users` table uses soft deletes. Queries must include `WHERE deleted_at IS NULL`.
- The user ID is `user_id` in the database, `uid` in the auth service, and `accountId` in the billing API. All three refer to the same value.
```

**Output format templates** — more reliable than prose descriptions. Agents pattern-match well against concrete structures:

```markdown
## Report structure
Use this template, adapting sections as needed:

# [Analysis Title]
## Executive summary
[One-paragraph overview]
## Key findings
- Finding 1 with supporting data
## Recommendations
1. Specific actionable recommendation
```

**Checklists for multi-step workflows** — helps the agent track progress and avoid skipping steps:

```markdown
## Workflow
- [ ] Step 1: Analyze input
- [ ] Step 2: Create plan
- [ ] Step 3: Validate plan
- [ ] Step 4: Execute
- [ ] Step 5: Verify output
```

**Validation loops** — instruct the agent to validate before proceeding:

```markdown
1. Make your edits
2. Run validation: `python scripts/validate.py output/`
3. If validation fails: review error, fix issues, re-run validation
4. Only proceed when validation passes
```

### 2.5 "When to use" / "When NOT to use" sections

Include a clear "When NOT to use" section with near-miss boundaries — scenarios that share keywords or concepts with your skill but need a different skill. This prevents false triggering.

---

## 3. Description Optimization

### 3.1 Principles for Effective Descriptions

| Principle | Explanation |
|-----------|-------------|
| **Use imperative phrasing** | "Use this skill when..." not "This skill does..." The agent is deciding whether to act. |
| **Focus on user intent, not implementation** | Describe what the user is trying to achieve, not the skill's internal mechanics. |
| **Err on the side of being pushy** | Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly. |
| **Keep it concise** | A few sentences to a short paragraph. Hard limit: 1024 characters. |

### 3.2 Testing Description Triggering

Create **eval queries** (~20) — realistic user prompts labeled with whether they should or shouldn't trigger your skill. Design:

- **Should-trigger queries**: Vary phrasing (formal/casual/typos), explicitness (naming the domain vs describing the need), detail level, and complexity.
- **Should-not-trigger queries**: Focus on **near-misses** — queries that share keywords with your skill but actually need something different. These are the most valuable negative test cases.

Run each query 3+ times (model behavior is nondeterministic) and compute a **trigger rate**. Use a train/validation split (60%/40%) to avoid overfitting.

---

## 4. Script Safety Guidelines

When a skill bundles executable scripts in `scripts/` or instructs the agent to run shell commands:

### Required

| Rule | Description |
|------|-------------|
| **Non-interactive** | No prompts waiting for stdin/TTY. All inputs via flags, environment variables, or stdin explicitly. |
| **`--help` available** | Prints usage instructions and examples. This is the primary way an agent learns the script's interface. |
| **Clear error messages** | Say what failed, what was expected, and what to try next. "Error: `--format` must be one of: json, csv, table. Received: 'xml'" |
| **No secrets** | No hardcoded tokens, keys, or passwords. No logging of secrets. |
| **Safe defaults** | Destructive operations require explicit `--force` or `--confirm` flags. |

### Recommended

| Rule | Description |
|------|-------------|
| **Structured output** | `--format json` option. Data to stdout, diagnostics to stderr. |
| **Idempotency** | Repeated runs do not corrupt state. "Create if not exists" over "create and fail on duplicate". |
| **`--dry-run` support** | For destructive or stateful operations, let the agent preview what will happen. |
| **Predictable output size** | Default to summary; support pagination flags if output can be large. |
| **Meaningful exit codes** | Distinct exit codes for different failure types. Document them in `--help`. |

### Self-contained scripts (recommended pattern)

Use inline dependency declarations so scripts can run with a single command:

- **Python (PEP 723)**: `# /// script` / `# dependencies = [...]` / `# ///` → run with `uv run`
- **Deno**: `import from "npm:package@version"` → run with `deno run`
- **Bun**: `import from "package@version"` → run with `bun run`

---

## 5. Evaluation Frameworks

### 5.1 Official Rubric (agentskills.io)

Five inspection dimensions from the official specification:

| Dimension | What it checks | Severity |
|-----------|---------------|----------|
| **Spec compliance** | Frontmatter fields, name/directory match, field format validity | Must |
| **Progressive disclosure** | SKILL.md conciseness, references with trigger conditions, no deep chains | Should |
| **Description quality** | User-intent language, trigger/not-trigger boundaries | Should |
| **Script readiness** | Non-interactive CLI, `--help`, structured output, safe defaults | Conditional |
| **Security hygiene** | No hardcoded secrets, no suspicious download/exfiltration instructions | Must |

### 5.2 TRACE Model (SkillHub)

Five-dimension quality model for evaluating skills:

| Dimension | Core question |
|-----------|--------------|
| **T · Trust** | "Can I safely use it?" — permissions, secrets, dependency risks, third-party scan evidence, China network compatibility |
| **R · Reliability** | "Can I use it consistently?" — input constraints, failure feedback, validation loops, repeatability |
| **A · Adaptability** | "Should I use it in this scenario?" — boundary clarity, trigger precision, near-miss handling |
| **C · Convention** | "Can it be understood, maintained, and reused?" — structure, progressive disclosure, templates, naming consistency |
| **E · Effectiveness** | "Did it actually solve the problem?" — output correctness, coverage, reusability, improvement over no-skill baseline |

---

## 6. Complete Skill Creation Checklist

When designing a new skill, verify all of the following:

### Structure
- [ ] Directory name uses lowercase letters, digits, and hyphens only
- [ ] `name` in frontmatter matches directory name exactly
- [ ] `SKILL.md` exists at the skill root
- [ ] Optional directories follow conventions (`scripts/`, `references/`, `assets/`)

### Frontmatter
- [ ] `name` is 1-64 characters, lowercase + hyphens only, no leading/trailing hyphens, no consecutive hyphens
- [ ] `description` is 1-1024 characters, describes both what AND when to use
- [ ] `description` uses imperative phrasing ("Use when...")
- [ ] `license` field present (short name or reference to bundled license file)

### Body content
- [ ] Under 500 lines / 5000 tokens
- [ ] Step-by-step instructions are clear and actionable
- [ ] Examples of inputs and outputs provided
- [ ] Common edge cases documented
- [ ] Gotchas section for non-obvious facts
- [ ] "When NOT to use" section with near-miss boundaries

### Progressive disclosure
- [ ] Long reference material moved to `references/`
- [ ] References linked with clear "when to read" triggers
- [ ] No deeply nested reference chains

### Scripts (if applicable)
- [ ] Non-interactive — no TTY prompts
- [ ] `--help` prints usage and examples
- [ ] Error messages say what failed and what to try
- [ ] No hardcoded secrets
- [ ] Destructive operations require `--force`/`--confirm`
- [ ] Structured output option (`--format json`)

### Trigger quality
- [ ] Description uses user-intent language
- [ ] Both "should trigger" and "should not trigger" scenarios considered
- [ ] Near-miss boundaries defined for adjacent skills

## References

This knowledge is distilled from official sources. For the full original content, see:
- [agentskills.io Specification](https://agentskills.io/specification)
- [Best practices for skill creators](https://agentskills.io/skill-creation/best-practices)
- [Optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)
- [Evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills)
- [Using scripts in skills](https://agentskills.io/skill-creation/using-scripts)
- [How to create custom Skills (Claude)](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [SkillHub TRACE Evaluation](https://skillhub.cn/tutorials#trace-evaluation)

For auto-generating an awesome list index from a skills repository, use the companion script:
```bash
python3 scripts/build_awesome.py --skills-root <path> --output AWESOME_AGENT_SKILLS.md
```

For a complete example of what an awesome list looks like, see [examples/sample-awesome.md](examples/sample-awesome.md).

## Keywords

**English keywords:**
agent-skills, skill-specification, skill-design, skill-creation, skill-development, skill-best-practices, skill-naming, skill-frontmatter, skill-directory-structure, progressive-disclosure, skill-description, skill-trigger, skill-evaluation, script-safety, trace-evaluation, official-rubric, skill-compliance, skill-checklist, skill-template, how-to-design-a-skill

**Chinese keywords (中文关键词):**
设计技能, 创建技能, 技能规范, 技能命名规则, 技能命名规范, SKILL.md 怎么写, frontmatter 规范, skill frontmatter, 技能最佳实践, 技能目录结构, 渐进式披露, 怎么写 description, skill description 怎么写, 技能触发条件, 技能脚本安全, 技能评估, TRACE 评测, 技能合规, 技能检查清单, Agent Skills 规范
