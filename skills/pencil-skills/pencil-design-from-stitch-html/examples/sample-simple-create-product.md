# Sample: Simplified Create Product (quick validation)

Minimal **Create Product** page for testing the pipeline: header + **one** card (one segment control + one input) + submit button. Fits in **1–2 batches** (≤25 ops each) so you can verify Stitch → Pencil flow without a full form.

Use this when:
- Validating that root height is fixed (no blank canvas).
- Checking that batch_design and get_screenshot work end-to-end.
- Iterating on mapping/tokens before adding more sections.

---

## Target structure

- **Root**: 390×**844** (fixed height), layout vertical, fill #F5F6FA.
- **Header**: back icon + title "创建商品".
- **Main**: one card "Basic Info" with (1) label "履约方式" + segment [到店 | 上门 | 快递], (2) label "商品名称" + one input row.
- **Submit**: full-width primary button "提交审核".

---

## Batch 1 (root + header + main + card + one block + submit)

All in one batch so bindings (header, main, card1, etc.) are in the same call. Total 18 ops.

**Root:** fixed height 844 to avoid blank canvas (see [html-to-pencil-mapping §2](../references/html-to-pencil-mapping.md#2-document-and-root)).

```javascript
root=I(document, {type: "frame", name: "Create Product", layout: "vertical", width: 390, height: 844, fill: "#F5F6FA", placeholder: true})
header=I(root, {type: "frame", layout: "horizontal", width: "fill_container", height: 56, padding: [0, 16], alignItems: "center", justifyContent: "space_between", fill: "#FFFFFF", stroke: {align: "inside", fill: "#E5E7EB", thickness: {bottom: 1}}})
backIcon=I(header, {type: "icon_font", iconFontFamily: "Material Symbols Rounded", iconFontName: "chevron_left", width: 24, height: 24, fill: "#1f2937"})
titleText=I(header, {type: "text", content: "创建商品", fontSize: 18, fontWeight: "700", fill: "#111827"})
main=I(root, {type: "frame", layout: "vertical", width: "fill_container", height: "fit_content(800)", padding: 16, gap: 16, placeholder: true})
card1=I(main, {type: "frame", layout: "vertical", width: "fill_container", padding: 16, gap: 16, fill: "#FFFFFF", cornerRadius: 12, stroke: {align: "inside", fill: "#E5E7EB", thickness: 1}})
segRow=I(card1, {type: "frame", layout: "vertical", width: "fill_container", gap: 8})
segLabel=I(segRow, {type: "text", content: "* 履约方式", fontSize: 14, fontWeight: "700", fill: "#111827"})
segWrap=I(segRow, {type: "frame", layout: "horizontal", width: "fill_container", gap: 4, fill: "#f3f4f6", padding: 4, cornerRadius: 8})
seg1=I(segWrap, {type: "frame", layout: "vertical", width: "fill_container", padding: [6, 0], fill: "#FFFFFF", cornerRadius: 6, justifyContent: "center", alignItems: "center"})
seg1T=I(seg1, {type: "text", content: "到店", fontSize: 14, fontWeight: "500", fill: "#1677FF"})
seg2=I(segWrap, {type: "frame", layout: "vertical", width: "fill_container", padding: [6, 0], justifyContent: "center", alignItems: "center"})
seg2T=I(seg2, {type: "text", content: "上门", fontSize: 14, fill: "#6b7280"})
seg3=I(segWrap, {type: "frame", layout: "vertical", width: "fill_container", padding: [6, 0], justifyContent: "center", alignItems: "center"})
seg3T=I(seg3, {type: "text", content: "快递", fontSize: 14, fill: "#6b7280"})
nameRow=I(card1, {type: "frame", layout: "vertical", width: "fill_container", gap: 8})
nameLabel=I(nameRow, {type: "text", content: "* 商品名称", fontSize: 14, fontWeight: "700", fill: "#111827"})
nameInput=I(nameRow, {type: "frame", layout: "vertical", width: "fill_container", height: 44, padding: [12, 0], stroke: {align: "inside", fill: "#E5E7EB", thickness: {bottom: 1}}, fill: "transparent"})
submitBtn=I(main, {type: "frame", layout: "vertical", width: "fill_container", height: 52, fill: "#1677FF", cornerRadius: 12, justifyContent: "center", alignItems: "center"})
submitText=I(submitBtn, {type: "text", content: "提交审核", fontSize: 16, fontWeight: "700", fill: "#FFFFFF"})
```

---

## After running

1. Call `get_screenshot(filePath, rootNodeId)` and confirm the screen is not blank (root has fixed height 844).
2. If you have a Stitch screenshot, compare visually and note any gaps.
3. To extend: add a second batch with more form rows under `card1` using the returned node ID for `card1` (e.g. `I("card1Id", { ... })`).

See [usage.md](usage.md) for the two entry points (Stitch URL vs pasted HTML) and verification step.
