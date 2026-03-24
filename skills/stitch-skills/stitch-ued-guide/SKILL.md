---
name: stitch-ued-guide
description: UED guidelines, visual vocabulary, and prompt structure for Stitch. Use when the user asks about layout/style terms, device constraints, or when structuring/improving Stitch prompts; combine with stitch-ui-prompt-architect for vague→concrete prompts.
allowed-tools:
  - "Read"
  - "Write"
---


# Stitch UED Guidelines

This skill serves as a reference for User Experience Design (UED) guidelines when working with Stitch. It includes interaction principles, visual vocabulary, and prompt engineering strategies.

## When to use this skill

Use this skill when:

*   The user asks about **layout or style terms** (e.g. Masonry, Glassmorphism, Sidebar) or **device constraints** (mobile vs desktop width, touch targets).
*   You need to **structure or improve a Stitch prompt** (Context → Layout → Component → Content) or ensure consistent UED wording.
*   You are coordinating with **stitch-ui-designer** and need UED/accessibility/design-system alignment alongside Stitch generation.

For **transforming vague ideas into a full Stitch prompt**, use **stitch-ui-prompt-architect**; combine both when you want structure + vocabulary (this skill) and concrete prompt output (prompt-architect).

## Design Modes (Model Selection)

Stitch operates in two distinct modes, which you should choose based on the user's need for speed vs. fidelity:

*   **Standard Mode (Gemini 2.5 Flash)**
    *   **Best for**: Rapid iteration, wireframing, exploring multiple layout ideas quickly.
    *   **Features**: Fast generation, Text-to-UI, Theme editing.
    *   **Use Case**: "Show me 3 different layout options for a login screen."

*   **Experimental Mode (Gemini 2.5 Pro)**
    *   **Best for**: High-fidelity design, complex logic, visual references.
    *   **Features**: Image-to-UI (Sketch/Screenshot upload), richer details, smarter component logic.
    *   **Use Case**: "Turn this napkin sketch into a production-ready dashboard."

## Prompt Engineering Strategy

A perfect Stitch prompt follows this structure:
`[Context & Style]` + `[Layout Structure]` + `[Component Details]` + `[Content & Data]`

### 1. Context & Style
*   **Context**: "Mobile fitness app for gym goers."
*   **Style**: "Dark mode with neon green accents (Cyberpunk). Rounded corners."
*   **Reference**: "Similar to Spotify's dark theme but for fitness."

### 2. Layout Structure
*   **Mobile**: "Bottom navigation bar, scrollable feed."
*   **Desktop**: "Left sidebar navigation, top header, main content area with data grid."
*   **Grid**: "3-column card grid with responsive behavior."

### 3. Component Details
*   **Don't say**: "A list."
*   **Do say**: "A vertical list of 'Workout Cards', each containing a map thumbnail, duration (e.g., '30 min'), and a 'Start' button."

### 4. Content & Data
*   **Realism**: Ask for realistic data. "User 'Alice', 'Morning Yoga', '300 kcal'."
*   **State**: "Active state for the 'Home' tab."

**Quick checklist (before calling generate_screen_from_text):**

*   [ ] **Context & style** defined? (device, app type, theme)
*   [ ] **Layout** defined? (nav position, main area structure)
*   [ ] **Key components** specific? (avoid "a list"; use e.g. "Workout Cards with map thumbnail, duration, Start button")
*   [ ] **Sample content / state** included? (real copy, active state)

## Visual Vocabulary

Use these terms to control the look and feel:

### Layout Patterns
*   **Hero Section**: Top area with main headline/image.
*   **Split Screen**: Left/Right division (common in Desktop Auth).
*   **Masonry**: Waterfall layout (Pinterest style).
*   **Sidebar Navigation**: Vertical nav on the left (SaaS standard).

### Style Modifiers
*   **Flat**: No shadows, high saturation.
*   **Material**: Shadows, layers, paper metaphor.
*   **Neomorphism**: Soft shadows, extruded shapes.
*   **Glassmorphism**: Blurred transparency, frosted glass.
*   **Brutalism**: Raw, bold, high contrast, large typography.

## Color & Theme Prompts

When describing **Context & Style**, use a clear color structure so Stitch produces consistent palettes. A strong pattern (inspired by [AI配色提示词-UI配色指南](https://mp.weixin.qq.com/s/1SDFd7ZOPkbhpvHsmTJQjQ)):

**Structure**: `[App type]` + `[Background hex]` + `[Primary hex]` + `[Secondary hex]` + `[Accent hex]` + `[Design system]` + `[Mood]`. Optionally add **semantic colors**: success green, alert red, warning yellow.

**Example — Dark productivity:**
> Modern productivity app dark theme, charcoal grey background #1a1a1a, primary blue #4A90E2, secondary teal #26D0CE, neutral greys #2d2d2d to #f5f5f5, accent orange #FF6B35 for CTAs, Material Design 3 inspired, high contrast for readability, professional and focused atmosphere.

**Example — Bright desktop tool:**
> Project management app bright theme, clean white background #FFFFFF, primary royal blue #2563EB, secondary purple #7C3AED, soft grey cards #F9FAFB, green success #22C55E, red alerts #DC2626, yellow warnings #F59E0B, minimal design with subtle shadows, organized and efficient visual hierarchy.

**Quick color checklist**: Background defined? Primary/secondary/accent with hex? Semantic colors (success/alert/warning) if needed? Design system (Material 3, Fluent) or style (glassmorphism, minimal) mentioned?

More ready-to-use prompts: see [docs/color-prompt-guide.md](../../docs/color-prompt-guide.md) in this repo, or the [original article](https://mp.weixin.qq.com/s/1SDFd7ZOPkbhpvHsmTJQjQ) for 20 curated prompts.

## Device Guidelines

*   **Mobile**: ~375px width. Focus on thumb-friendly bottom navigation. Vertical scrolling is expected.
*   **Desktop/Web**: ~1440px width. Use horizontal space. Multi-column layouts.
*   **Tablet**: Hybrid. Often resembles desktop but with touch targets.

## Accessibility & Inclusive Design

*   **Contrast & readability**: Prefer sufficient contrast (dark/light); avoid low-contrast text. In prompts, you can add "high contrast" or "clear text hierarchy."
*   **Touch targets**: For mobile/tablet, ask for touch-friendly controls (e.g. "buttons at least 44px tap area"). In Context or Component details, add "touch-friendly" when relevant.
*   **Focus & keyboard**: For desktop, mention "clear focus states" or "keyboard-navigable" when the design should support accessibility.
*   **In prompts**: Add phrases like "high contrast," "clear focus states," "touch-friendly buttons" in Context/Style or Component Details when UED or accessibility alignment is needed.

## Controls & Variants

*   **Variants**: Stitch generates multiple options. You can ask to "Generate variants for the hero section" to A/B test designs.
*   **Controls**: Use the **Interactive Chat** to refine designs ("Make the button blue", "Move the logo to the center").

## Related resources

- **Stitch Effective Prompting Guide**: https://stitch.withgoogle.com/docs/learn/prompting/ — official best practices; consult for up-to-date recommendations.
- **Division of labor**: **stitch-ued-guide** = structure and vocabulary (how to phrase, what terms to use). **stitch-ui-prompt-architect** = transform vague ideas into a full, executable Stitch prompt (with DESIGN.md, framework contracts). Use both when you need consistent UED wording and concrete prompt output.
- **Vague → enhanced prompt**: Use **stitch-ui-prompt-architect** (Path A: enhance vague UI ideas with specificity, UI/UX keywords, DESIGN.md context). Use with **stitch-design-md** for DESIGN.md and **stitch-ui-design-spec-generator** for full flow.
- **Stitch skills in this repo** (prefer these over official): design-md → **stitch-design-md**; enhance-prompt → **stitch-ui-prompt-architect** (two paths + framework contracts); react-components → **stitch-react-components**; stitch-loop → **stitch-loop**; remotion → **stitch-remotion**; shadcn-ui → **stitch-shadcn-ui**. Plus **stitch-mcp-*** (one skill per MCP tool: create-project, get-project, list-projects, generate-screen-from-text, get-screen, list-screens), **stitch-ui-design-spec-*** (Bootstrap, Element Plus, Layui, uView, uView Pro, Vant), **stitch-ui-designer** (orchestrator), and six Stitch→framework conversion skills (Vue + Element/Bootstrap/Layui/Vant, uni-app + uView/uView Pro). These skills reference each other and the same MCP; use stitch-mcp-<tool> names (e.g. get_screen → stitch-mcp-get-screen).

## References

- [Examples](examples/usage.md)
