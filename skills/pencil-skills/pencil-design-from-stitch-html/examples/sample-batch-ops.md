# Sample: Minimal HTML → One batch_design

This example shows how a **minimal** Stitch-like HTML structure (root + header + main + one card with title) maps to a **single** `batch_design` call (under 25 ops). In practice, larger pages are split into multiple batches per the pencil-design-from-stitch-html [SKILL.md](../SKILL.md) section **Execution order and batch split**.

## Input (simplified HTML)

```html
<body class="min-h-screen bg-page">
  <header class="sticky top-0 bg-white border-b border-gray-200 px-4 h-14 flex items-center">
    <span class="icon">back</span>
    <h1 class="text-lg font-semibold text-gray-900">Create Product</h1>
  </header>
  <main class="px-4 py-4 space-y-4">
    <section class="rounded-xl p-4 shadow-soft bg-white">
      <h2 class="text-sm font-bold text-gray-900 mb-4">Basic Info</h2>
    </section>
  </main>
</body>
```

## Output (one batch_design, operations string)

Parent is `document`. Binding names: root, header, main, card1, card1Title.

```javascript
root=I(document, {type: "frame", name: "Screen", layout: "vertical", width: 390, height: 844, fill: "#f5f6fa", placeholder: true})
header=I(root, {type: "frame", layout: "horizontal", width: "fill_container", height: 56, padding: [0, 16], alignItems: "center", gap: 12, fill: "#ffffff", stroke: {align: "inside", fill: "#e5e7eb", thickness: {bottom: 1}}})
backIcon=I(header, {type: "icon_font", iconFontFamily: "Material Symbols Rounded", iconFontName: "arrow_back", width: 24, height: 24, fill: "#303133"})
titleText=I(header, {type: "text", content: "Create Product", fontSize: 18, fontWeight: "600", fill: "#303133"})
main=I(root, {type: "frame", layout: "vertical", width: "fill_container", height: "fit_content(800)", padding: 16, gap: 16, placeholder: true})
card1=I(main, {type: "frame", name: "Basic Info", layout: "vertical", width: "fill_container", padding: 16, gap: 16, fill: "#ffffff", cornerRadius: 12, stroke: {align: "inside", fill: "#e5e7eb", thickness: 1}})
card1Title=I(card1, {type: "text", content: "Basic Info", fontSize: 14, fontWeight: "600", fill: "#303133"})
```

**Style mapping used:**

- `bg-page` → root fill `#f5f6fa`
- `bg-white`, `border-b` → header fill `#ffffff`, stroke bottom 1px `#e5e7eb`
- `px-4` → header padding [0, 16]; `h-14` → height 56
- `text-lg font-semibold text-gray-900` → titleText fontSize 18, fontWeight 600, fill #303133
- `space-y-4` → main gap 16; `p-4` → main padding 16
- `rounded-xl p-4 shadow-soft bg-white` → card1 cornerRadius 12, padding 16, fill #ffffff, stroke 1px (shadow-soft approximated by stroke if effect not set)
- `text-sm font-bold text-gray-900 mb-4` → card1Title fontSize 14, fontWeight 600, fill #303133; mb-4 → card1 gap 16 (between title and future body)

Total: 8 operations. Next batch would add children under `card1` (e.g. form rows) or under `main` (more cards).
