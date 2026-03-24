# pencil-design-from-stitch-html Usage

## When to use

- User has a **Stitch screen** and wants a **Pencil .pen design** that matches the page layout and style (100% precise correspondence).
- You need HTML (from Stitch or pasted), then parse DOM and Tailwind, then output sequential Pencil `batch_design` operations.

## Two entry points

| Entry | Input | What to do |
|-------|--------|------------|
| **A. Stitch URL or project/screen IDs** | User gives Stitch URL or projectId + screenId | Call Stitch MCP `get_screen(projectId, screenId)` to get `htmlCode.downloadUrl`, `screenshot.downloadUrl`, width, height, title. Try to **fetch HTML** from `htmlCode.downloadUrl` (e.g. `web_fetch`). If fetch fails (auth/network), **ask the user to paste the HTML** so mapping can proceed. Use width/height for root frame (e.g. 390×844). |
| **B. User provides HTML** | User pastes or supplies the page HTML | Skip Stitch fetch. Parse the HTML directly; use [html-to-pencil-mapping.md](../references/html-to-pencil-mapping.md) and [tailwind-to-pencil-styles.md](../references/tailwind-to-pencil-styles.md) to build node tree and styles. Root dimensions: use 390 width and **fixed height 844 or 884** (see [Root frame convention](../references/html-to-pencil-mapping.md#2-document-and-root)). |

## Example MCP flow (end-to-end)

1. **Stitch** (if entry A): `list_projects` (optional) → `list_screens(projectId)` → choose screen → `get_screen(projectId, screenId)` → get `htmlCode.downloadUrl`, `screenshot.downloadUrl`, width, height, title.
2. **Get HTML**: From `htmlCode.downloadUrl` (fetch) or **user-pasted HTML** (entry B). If fetch fails, prompt: “Please paste the screen HTML so I can generate the Pencil design.”
3. **Parse**: Extract DOM and Tailwind classes per node; identify header, main, sections, forms.
4. **Map + style**: Apply [html-to-pencil-mapping.md](../references/html-to-pencil-mapping.md) (use **fixed root height** 844/884); [tailwind-to-pencil-styles.md](../references/tailwind-to-pencil-styles.md) (and target framework *-to-pencil-styles.md if set) for fill, padding, fontSize.
5. **Plan batches**: Split ops ≤25 per batch per [SKILL.md](../SKILL.md) **Execution order and batch split**.
6. **Pencil**: `open_document('new')` or path → optionally `find_empty_space_on_canvas` → `batch_design` Batch 1 → Batch 2 → … → `get_screenshot(rootNodeId)` to verify.
7. **Verify** (recommended): If you have Stitch `screenshot.downloadUrl`, download that image and compare visually with Pencil `get_screenshot(root)` to note layout/style gaps for a follow-up pass.

## Steps (summary)

1. **Resolve screen**: From Stitch design URL parse projectId and screenId, or use list_projects → list_screens to pick a screen.
2. **get_screen**: Call Stitch MCP get_screen; obtain htmlCode.downloadUrl, screenshot.downloadUrl, width, height, title.
3. **Download HTML**: Fetch HTML from htmlCode.downloadUrl (Bash script or web_fetch); save to e.g. temp/source.html.
4. **Parse HTML**: Build DOM tree and per-node Tailwind class list; identify semantic regions (header, main, sections, forms).
5. **Apply mapping**: Use [references/html-to-pencil-mapping.md](../references/html-to-pencil-mapping.md) to map each element to Pencil node type and default layout/size.
6. **Apply styles**: Use [references/tailwind-to-pencil-styles.md](../references/tailwind-to-pencil-styles.md) to resolve background, color, size, margin, padding, shadow, border-radius for each node.
7. **Build batches**: Use the pencil-design-from-stitch-html [SKILL.md](../SKILL.md) section **Execution order and batch split** to split operations into ordered batches (≤25 ops per batch_design).
8. **Run Pencil**: open_document('new' or path) → optionally find_empty_space_on_canvas → batch_design(Batch 1) → batch_design(Batch 2) → … → get_screenshot(root) to verify.

## Example user prompt

> "Convert this Stitch screen into a Pencil design that looks exactly the same: https://stitch.withgoogle.com/projects/123/screen/456"

Or:

> "Use pencil-design-from-stitch-html to draw the Create Product page from Stitch in Pencil."

## Output

- A .pen file (new or at given path) with a root frame and children matching the page structure.
- **Verification**: Compare Pencil `get_screenshot(root)` with Stitch screenshot (from `screenshot.downloadUrl` if entry A) to catch missing blocks or style drift.

## Example docs in this folder

| Doc | Purpose |
|-----|---------|
| [usage.md](usage.md) | When to use, steps, example prompts, MCP flow (this file). |
| [sample-batch-ops.md](sample-batch-ops.md) | Minimal page → **single** batch_design (≤25 ops). |
| [sample-multi-batch.md](sample-multi-batch.md) | Header + one card + two form rows → **four** batches; shows parent bindings across batches. |
| [sample-with-framework-refs.md](sample-with-framework-refs.md) | Same minimal page with **target framework** (uView Pro): refs and tokens instead of primitives. |
| [sample-simple-create-product.md](sample-simple-create-product.md) | **Simplified** Create Product: header + one card (one segment + one input) + submit; 1–2 batches for quick validation. |

## References

- [HTML → Pencil mapping](../references/html-to-pencil-mapping.md)
- [SKILL.md](../SKILL.md) (includes Execution order and batch split)
- [Tailwind → Pencil styles](../references/tailwind-to-pencil-styles.md)
- [Sample batch ops](sample-batch-ops.md) · [Multi-batch](sample-multi-batch.md) · [With framework refs](sample-with-framework-refs.md) · [Simplified Create Product](sample-simple-create-product.md)
