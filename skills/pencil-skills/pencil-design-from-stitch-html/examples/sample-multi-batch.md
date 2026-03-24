# Sample: Multi-Batch (Header + One Card + Two Form Rows)

This example shows how a small page is split into **multiple** `batch_design` calls so that each batch stays under 25 operations and parents are created before their children. Parent bindings from one batch are used as the parent argument in the next.

## Input (simplified HTML)

```html
<body class="min-h-screen bg-page">
  <header class="sticky top-0 bg-white border-b px-4 h-14 flex items-center">
    <span class="icon">back</span>
    <h1 class="text-lg font-semibold text-gray-900">Create Product</h1>
  </header>
  <main class="px-4 py-4 space-y-4">
    <section class="rounded-xl p-4 bg-white">
      <h2 class="text-sm font-bold text-gray-900">Basic Info</h2>
      <div class="space-y-3">
        <label class="block text-sm text-gray-600">Product name</label>
        <input type="text" placeholder="Enter name" class="rounded border px-3 py-2 w-full" />
        <label class="block text-sm text-gray-600">Price (optional)</label>
        <input type="text" placeholder="0.00" class="rounded border px-3 py-2 w-full" />
      </div>
    </section>
  </main>
</body>
```

## Batch 1 — Root and main structure (parent: document)

Creates `root`, `header`, `main`. Binding names used in later batches: `root`, `header`, `main`.

```javascript
root=I(document, {type: "frame", name: "Screen", layout: "vertical", width: 390, height: 844, fill: "#f5f6fa", placeholder: true})
header=I(root, {type: "frame", layout: "horizontal", width: "fill_container", height: 56, padding: [0, 16], alignItems: "center", gap: 12, fill: "#ffffff", stroke: {align: "inside", fill: "#e5e7eb", thickness: {bottom: 1}}})
main=I(root, {type: "frame", layout: "vertical", width: "fill_container", height: "fit_content(800)", padding: 16, gap: 16, placeholder: true})
```

Ops: 3. Parent for next batch: `header`, `main`.

---

## Batch 2 — Header content (parent: header)

Fills the header. Parent `header` was created in Batch 1.

```javascript
backIcon=I(header, {type: "icon_font", iconFontFamily: "Material Symbols Rounded", iconFontName: "arrow_back", width: 24, height: 24, fill: "#303133"})
titleText=I(header, {type: "text", content: "Create Product", fontSize: 18, fontWeight: "600", fill: "#303133"})
```

Ops: 2.

---

## Batch 3 — First section container (parent: main)

Creates card1, card1Header, card1Title, card1Body. Binding `card1Body` is the parent for form rows in Batch 4.

```javascript
card1=I(main, {type: "frame", name: "Basic Info", layout: "vertical", width: "fill_container", padding: 16, gap: 16, fill: "#ffffff", cornerRadius: 12, stroke: {align: "inside", fill: "#e5e7eb", thickness: 1}})
card1Header=I(card1, {type: "frame", layout: "horizontal", width: "fill_container", justifyContent: "space_between", alignItems: "center"})
card1Title=I(card1Header, {type: "text", content: "Basic Info", fontSize: 14, fontWeight: "600", fill: "#303133"})
card1Body=I(card1, {type: "frame", layout: "vertical", width: "fill_container", gap: 12, placeholder: true})
```

Ops: 4. Parent for next batch: `card1Body`.

---

## Batch 4 — Section body (form rows) (parent: card1Body)

Adds two label + input rows under `card1Body`. Parent `card1Body` was created in Batch 3.

```javascript
row1=I(card1Body, {type: "frame", layout: "vertical", width: "fill_container", gap: 4})
label1=I(row1, {type: "text", content: "Product name", fontSize: 14, fill: "#606266"})
input1=I(row1, {type: "frame", layout: "vertical", width: "fill_container", height: 40, padding: [8, 12], stroke: {align: "inside", fill: "#e5e7eb", thickness: 1}, cornerRadius: 4, fill: "#ffffff"})
row2=I(card1Body, {type: "frame", layout: "vertical", width: "fill_container", gap: 4})
label2=I(row2, {type: "text", content: "Price (optional)", fontSize: 14, fill: "#606266"})
input2=I(row2, {type: "frame", layout: "vertical", width: "fill_container", height: 40, padding: [8, 12], stroke: {align: "inside", fill: "#e5e7eb", thickness: 1}, cornerRadius: 4, fill: "#ffffff"})
```

Ops: 6.

---

## Summary

| Batch | Parent(s) from previous batch | Ops | Content |
|-------|-------------------------------|-----|---------|
| 1 | document | 3 | root, header, main |
| 2 | header | 2 | backIcon, titleText |
| 3 | main | 4 | card1, card1Header, card1Title, card1Body |
| 4 | card1Body | 6 | row1, label1, input1; row2, label2, input2 |

Total: 4 batches, 15 operations. Order must be 1 → 2 → 3 → 4. See [SKILL.md](../SKILL.md) **Execution order and batch split** for the full phase table.
