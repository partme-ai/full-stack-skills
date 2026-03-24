---
name: stitch-ui-prompt-architect
description: Builds Stitch-ready prompts from vague UI ideas or from Design Spec and User Request. Outputs sectioned Context, Layout, and Components. Supports DESIGN.md and framework contract prefix.
allowed-tools:
  - "Read"
  - "Write"
---


# Stitch UI Prompt Architect

**Constraint**: Only use this skill when the user explicitly mentions "Stitch" or when orchestrating a Stitch design task.

This skill acts as a **Senior UX Designer** and **Prompt Engineer**. It supports two paths so that local behavior is strictly stronger than a single-path prompt skill:

- **Path A — Enhance vague prompt**: Transform rough or vague UI ideas into polished, Stitch-optimized prompts (specificity, UI/UX keywords, design system context, numbered structure). Use when the user gives a short or unclear prompt.
- **Path B — Spec → prompt**: Merge the User Request and the Design Spec (from `stitch-ui-design-spec-generator`) into a final sectioned Stitch prompt. Use when a structured spec already exists.

## Prerequisites

- **Stitch Effective Prompting Guide**: https://stitch.withgoogle.com/docs/learn/prompting/ — consult for latest best practices; they may supersede or complement the patterns below.

## Official Documentation (by Framework)

When injecting framework contract prefix (Path B) or translating component keywords, prefer the following authoritative docs:

| Framework | Official / Guide | Components | Other |
|-----------|------------------|------------|--------|
| **Bootstrap Vue 3** | [bootstrap-vue.org](https://bootstrap-vue.org) · [docs](https://bootstrap-vue.org/docs) · [Vue 3](https://bootstrap-vue.org/vue3) | [components](https://bootstrap-vue.org/docs/components) | [GitHub](https://github.com/bootstrap-vue/bootstrap-vue) |
| **Element Plus** | [element-plus.org (zh-CN)](https://element-plus.org/zh-CN/) | [design](https://element-plus.org/en-US/guide/design) · [overview](https://element-plus.org/en-US/component/overview) | [GitHub](https://github.com/element-plus/element-plus) |
| **Layui-Vue** | [layui-vue.com](https://www.layui-vue.com/zh-CN/index) | [guide](https://www.layui-vue.com/zh-CN/guide/introduce) · [components](https://www.layui-vue.com/zh-CN/components) | [GitHub](https://github.com/layui-vue/layui-vue) |
| **Vant (Vue 3)** | [vant-ui.github.io](https://vant-ui.github.io/) | [Vant zh-CN](https://vant-ui.github.io/vant/#/zh-CN) | [GitHub](https://github.com/youzan/vant) |
| **uView 2.0 (Vue 2)** | [uviewui.com](https://www.uviewui.com/) | [guide/demo](https://www.uviewui.com/guide/demo.html) · [components](https://www.uviewui.com/components/intro.html) | [GitHub](https://github.com/umicro/uView2.0) |
| **uView Pro (Vue 3)** | [uviewpro.cn](https://uviewpro.cn/) | [guide](https://uviewpro.cn/zh/guide/intro.html) · [components](https://uviewpro.cn/zh/components/intro.html) · [tools](https://uviewpro.cn/zh/tools/intro.html) · [layout](https://uviewpro.cn/zh/layout/intro.html) | — |

## When to Use

- **Path A**: User wants to polish a UI prompt before sending to Stitch; improve a prompt that produced poor results; add design system consistency to a simple idea; structure a vague concept into an actionable prompt.
- **Path B**: Orchestrator has already produced a Design Spec (e.g. from `stitch-ui-design-spec-generator`) and needs a final [Context]/[Layout]/[Components] prompt; or user requests a prompt for a named framework (uView, Element Plus, Layui, Bootstrap, Vant).

---

## Path A: Enhance Vague Prompt

Follow these steps to turn a vague idea into a Stitch-ready prompt.

### Step 1: Assess the Input

Evaluate what's missing:

| Element | Check for | If missing... |
|---------|-----------|---------------|
| **Platform** | "web", "mobile", "desktop" | Add based on context or ask |
| **Page type** | "landing page", "dashboard", "form" | Infer from description |
| **Structure** | Numbered sections/components | Create logical page structure |
| **Visual style** | Adjectives, mood, vibe | Add descriptors (see [references/KEYWORDS.md](references/KEYWORDS.md)) |
| **Colors** | Specific values or roles | Add design system or suggest |
| **Components** | UI-specific terms | Translate to proper keywords |

### Step 2: Check for DESIGN.md

- **If DESIGN.md exists**: Read it; extract design system block (palette, typography, component styles); include as "DESIGN SYSTEM (REQUIRED)" in output.
- **If DESIGN.md does not exist**: Add a tip at the end: "For consistent designs across multiple screens, create a DESIGN.md using the `stitch-design-md` skill."

### Step 3: Apply Enhancements

- **UI/UX keywords**: Replace vague terms (e.g. "menu at the top" → "navigation bar with logo and menu items"; "button" → "primary call-to-action button"). Use [references/KEYWORDS.md](references/KEYWORDS.md) for component and adjective palettes.
- **Vibe**: Add descriptive adjectives ("modern" → "clean, minimal, with generous whitespace"; "dark mode" → "dark theme with high-contrast accents on deep backgrounds").
- **Structure**: Organize into numbered **Page Structure** (Header, Hero, Content Area, Footer, etc.).
- **Colors**: Format as `Descriptive Name (#hex) for functional role` (e.g. "Deep Ocean Blue (#1a365d) for primary buttons").

### Step 4: Format Output (Path A)

Structure the enhanced prompt as:

```markdown
[One-line description of the page purpose and vibe]

**DESIGN SYSTEM (REQUIRED):**
- Platform: [Web/Mobile], [Desktop/Mobile]-first
- Theme: [Light/Dark], [style descriptors]
- Background: [Color description] (#hex)
- Primary Accent: [Color description] (#hex) for [role]
- Text Primary: [Color description] (#hex)
- [Additional design tokens...]

**Page Structure:**
1. **[Section]:** [Description]
2. **[Section]:** [Description]
...
```

**Output options**: Return as text; or if the user requests, write to `next-prompt.md` (for `stitch-loop`) or a custom file.

---

## Path B: Spec + Request → Sectioned Prompt

Use when you have a **Design Spec** (from `stitch-ui-design-spec-generator`) and a **User Request**.

### Input

- **User Request**: e.g. "Login page with social auth".
- **Design Spec**: JSON with `deviceType`, `designMode`, `theme`, `styleKeywords`, etc.

### Output Format (Must)

Return a single prompt with:

```text
[Context]
...

[Layout]
...

[Components]
...
```

### Construction Logic

**1. Context & Style**  
Combine `deviceType`, `designMode`, `theme`, `styleKeywords`.  
Example: "Mobile High-Fidelity login screen. Cyberpunk aesthetic. Dark mode with neon blue accents."

**2. Design Contract Prefix (Hard Constraints)**  
If the user request includes a named style (e.g. "uview 风格"), prepend the corresponding contract to `[Context]`:

| Keyword | Use skill output as prefix |
|---------|----------------------------|
| `uview-pro`, `uviewpro` | `stitch-ui-design-spec-uviewpro` |
| `uview`, `uview2` | `stitch-ui-design-spec-uview` |
| `element`, `element-plus` | `stitch-ui-design-spec-element-plus` |
| `vant`, `vant4` | `stitch-ui-design-spec-vant` |
| `layui`, `layui-vue` | `stitch-ui-design-spec-layui` |
| `bootstrap`, `bs-vue` | `stitch-ui-design-spec-bootstrap` |

**3. Contract Selection JSON**  
When a named design system is present, generate `CONTRACT_SELECTION_JSON_V1` to decide which component contracts and UI state snippets to inject (include only what the current screen needs). Schema: `version`, `designSystem`, `mode`, `contracts.include`, `states.include`.

**4. Layout Structure**  
- Mobile: Header → Body (Stack) → Footer (Nav/Action).  
- Desktop: Sidebar/TopNav → Main Grid → Widgets.

**5. Component Details**  
Translate requirements into UI components (e.g. "Login" → Inputs, Primary Button, Forgot Pass link).

**6. Content**  
Use specific copy (e.g. "Welcome back, Agent") instead of placeholder "Text".

---

## Example (Path A: Vague → Enhanced)

**Input:** "make me a login page"

**Output:**

```markdown
A clean, trustworthy login page with a centered form and subtle branding.

**DESIGN SYSTEM (REQUIRED):**
- Platform: Web, Desktop-first
- Theme: Light, minimal, professional
- Background: Clean White (#ffffff)
- Surface: Soft Gray (#f9fafb) for form card
- Primary Accent: Deep Blue (#2563eb) for submit button and links
- Text Primary: Near Black (#111827) for headings
- Text Secondary: Medium Gray (#6b7280) for labels
- Buttons: Subtly rounded (8px), full-width on form
- Cards: Gently rounded (12px), soft shadow for elevation

**Page Structure:**
1. **Header:** Minimal logo, centered
2. **Login Card:** Centered form with email, password fields, "Forgot password?" link
3. **Submit Button:** Primary blue "Sign In" button
4. **Footer:** "Don't have an account? Sign up" link
```

---

## Example (Path B: Spec → Prompt)

> "Mobile login screen for a Fintech App. Clean minimalist aesthetic. Light mode.  
> Layout: Center-aligned vertical stack.  
> Header: Brand logo 'PayFast' and 'Welcome' title.  
> Form: Input field for 'Email' with mail icon. Input field for 'Password' with eye toggle.  
> Actions: Full-width primary blue button 'Sign In'. 'Forgot Password?' link.  
> Footer: 'Create Account' link."

---

## Tips

1. **Path choice**: Use Path A for short/vague prompts; Path B when a spec already exists or a framework name is given.
2. **Be specific early** for vague inputs; **match intent** — don’t over-design if the user wants something simple.
3. **Numbered sections** help Stitch understand hierarchy.
4. **Design system**: For multi-page consistency, use DESIGN.md (from `stitch-design-md`) or inject framework contract (Path B).
5. **Edits**: One change at a time; don’t bundle unrelated changes.

## Keywords

**English:** Stitch, prompt, enhance, vague, design spec, DESIGN.md, next-prompt, stitch-loop, uView, Element, Layui, Bootstrap, Vant.  
**中文关键词：** Stitch、提示词、增强、模糊需求、设计规范、DESIGN.md、next-prompt、stitch-loop、uView、Element、Layui、Bootstrap、Vant。

## References

- [KEYWORDS](references/KEYWORDS.md) — UI/UX keyword palettes for Path A.
- [Official documentation (by framework)](#official-documentation-by-framework) — Authoritative docs for BootstrapVue, Element Plus, Layui-Vue, Vant, uView 2, uView Pro.

## References

- [Examples](examples/usage.md)
- [Keywords](references/KEYWORDS.md)
