# Sample: Same Page With Target Framework (uView Pro)

When the user specifies a **target framework** (e.g. uView Pro), use **design-system refs** instead of raw frame/text for card, section, hints, divider, button, input. Numeric values (fill, padding, height) come from that framework's *-to-pencil-styles.md (sections 12 and 14).

This example maps the same minimal page (header + one card with title) to **refs** from pencil-ui-design-system-uviewpro. The .pen must have that design system loaded so refs resolve.

## Input (unchanged)

```html
<body class="min-h-screen bg-page">
  <header class="sticky top-0 bg-white border-b px-4 h-14 flex items-center">
    <span class="icon">back</span>
    <h1 class="text-lg font-semibold text-gray-900">Create Product</h1>
  </header>
  <main class="px-4 py-4 space-y-4">
    <section class="rounded-xl p-4 shadow-soft bg-white">
      <h2 class="text-sm font-bold text-gray-900">Basic Info</h2>
    </section>
  </main>
</body>
```

## Output (one batch_design, with refs)

- **Root / header / main**: Still primitive frames (layout structure).
- **Card / section**: Use **u-card** ref. Override title via `descendants` (exact node IDs depend on the design system; below uses placeholder IDs).
- **Header back icon / title**: Can stay primitive or use u-navbar ref if the design system exposes it; here kept as icon_font + text for clarity.

Tokens from [uviewpro-to-pencil-styles.md](../references/uviewpro-to-pencil-styles.md): primary `#3c9cff`, page bg `#f5f6fa`, card padding 16, radius 12, border `#e5e7eb`.

```javascript
root=I(document, {type: "frame", name: "Screen", layout: "vertical", width: 390, height: 844, fill: "#f5f6fa", placeholder: true})
header=I(root, {type: "frame", layout: "horizontal", width: "fill_container", height: 48, padding: [0, 16], alignItems: "center", gap: 12, fill: "#ffffff", stroke: {align: "inside", fill: "#e5e7eb", thickness: {bottom: 1}}})
backIcon=I(header, {type: "icon_font", iconFontFamily: "Material Symbols Rounded", iconFontName: "arrow_back", width: 24, height: 24, fill: "#303133"})
titleText=I(header, {type: "text", content: "Create Product", fontSize: 18, fontWeight: "600", fill: "#303133"})
main=I(root, {type: "frame", layout: "vertical", width: "fill_container", height: "fit_content(800)", padding: 16, gap: 16, placeholder: true})
card1=I(main, {type: "ref", ref: "u-card-id", width: "fill_container"})
// Override card title (node ID depends on design system; example):
// U("card1/titleSlot", {content: "Basic Info"})  // or descendants in I() if supported
```

If the design system's u-card has a **title** slot or descendant, use `U(card1+"/titleId", {content: "Basic Info"})` in the same or next batch. For **u-section** (title + right widget), use:

```javascript
section1=I(main, {type: "ref", ref: "u-section-id", width: "fill_container"})
U(section1+"/titleId", {content: "Basic Info"})
```

## Differences from agnostic (no target)

| Aspect | Agnostic (sample-batch-ops.md) | Target uView Pro (this sample) |
|--------|--------------------------------|--------------------------------|
| Card | Primitive `frame` with fill, cornerRadius, stroke | **ref** to u-card (or u-section); tokens from §12 |
| Height / padding | From Tailwind (e.g. h-14 → 56) | From framework (e.g. header 48, padding 16) |
| Button / Input | frame + text or primitive frame | Prefer **u-button**, **u-input** refs; see *-to-pencil-styles.md §15 |

See [uviewpro-to-pencil-styles.md](../references/uviewpro-to-pencil-styles.md) sections 0 (component mapping), 12 (tokens), and 15 (refs and constraints).
