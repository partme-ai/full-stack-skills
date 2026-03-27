---
name: full-stack-doc
description: >
  Scaffolds, validates, and maintains PartMe/Octo-style product documentation
  trees — 11 root-level docs, 7 per-version docs, and optional per-module
  triplets (PRD / Stitch / UI). Provides ready-to-copy Markdown templates with
  {Name} and {V} placeholders. Use when creating new product doc repositories,
  organizing partme-docs or Octo* projects, auditing repo doc structures, or
  generating documentation scaffolding — even if the user just says "set up docs",
  "create doc structure", "初始化文档", or "产品文档".
metadata:
  author: partme
  version: "2.0"
compatibility: Requires filesystem access for scaffolding and template copying.
---

# Product Documentation Standard

Enforces a fixed directory-and-naming convention for product documentation, aligned with the PartMe / Octo series. Ready-to-copy Markdown templates live under [`templates/`](templates/).

## When to use

- Creating or initializing a product documentation repository
- Scaffolding doc trees for Octo* or PartMe projects
- Auditing or aligning existing repos against the PartMe doc standard
- Generating / renaming docs to match the naming convention
- Aligning `partme-docs/` content with the template structure

## Placeholders

| Placeholder | Meaning | Example |
|-------------|---------|---------|
| `{Name}` | Product / brand name | `OctoPanel` |
| `{V}` | Version directory name | `V1`, `V2` |
| `{模块简称}` | Module short name | `登录页`, `设备中心` |

Replace placeholders in **both filenames and content**. Root allows two files sharing sequence `6、` — this is intentional.

## Structure at a glance

| Scope | Count | Templates | Naming pattern |
|-------|-------|-----------|----------------|
| Root | 11 (two share `6、`) | [`templates/root/`](templates/root/) | `{序号}、{Name}-{文档名}.md` |
| Version (`{V}/`) | 7 | [`templates/version/`](templates/version/) | `{序号}、{Name}-{文档名}-{V}.md` |
| Module (optional) | 3 per module | [`templates/module/`](templates/module/) | `{Name}-{模块简称}-{类型}-{V}.md` |
| Delivery (optional) | 5 | [`templates/delivery/`](templates/delivery/) | Context-dependent |

Special directories: `技术调研/` for tech research, `其他/` for non-standard docs. Directories like `demo/`, `assets/`, `.stitch/` stay untouched.

For complete file listings and naming rules, see [`references/structure.md`](references/structure.md).

## Scaffolding workflow

Copy this checklist and track progress:

```
Doc Scaffolding:
- [ ] Step 1: Root — copy templates/root/ → project root, rename with {Name}
- [ ] Step 2: Version — copy templates/version/ → {V}/, rename with {Name} and {V}
- [ ] Step 3: Modules — copy templates/module/ per module folder (if applicable)
- [ ] Step 4: Special dirs — create 技术调研/ and 其他/ as needed
- [ ] Step 5: Validate — run the checklist below
```

**Step 1 — Root docs**: Copy all 11 files from `templates/root/` into the project root. Rename each replacing `{Name}` with the actual product name: e.g., `1、命名与品牌说明.md` → `1、OctoPanel-命名与品牌说明.md`.

**Step 2 — Version docs**: Create `{V}/` (e.g., `V1/`). Copy 7 files from `templates/version/`. Replace both `{Name}` and `{V}` in filenames and content.

**Step 3 — Module docs** (optional): For each functional module, create `{V}/{序号}、{模块名}/`. Copy 3 files from `templates/module/`. Replace `{Name}`, `{模块简称}`, and `{V}`.

Example (OctoPanel V1 login):
- `OctoPanel-登录页-PRD-V1.md`
- `OctoPanel-登录页-Stitch设计提示词.md`
- `OctoPanel-登录页-UI设计说明-V1.md`

**Step 4 — Special dirs**: Create `技术调研/` for tech research and `其他/` for non-standard docs. Delivery templates (`templates/delivery/`) go into `其他/` or a dedicated delivery folder.

**Step 5 — Validate**: Run the validation checklist below.

## Gotchas

- Sequence numbers `1–7` in version folders are **reserved** for the 7 standard docs. Non-standard docs must use `8+` or go into `其他/`.
- Root has **two** files numbered `6、` (产品与版本规划 and 详细功能清单) — this is by design.
- Don't reorganize special directories (`demo/`, `assets/`, `.stitch/`, `stitch_*`, `实施指南/`) unless the user explicitly requests it.
- Delivery templates are optional and do **not** occupy root-level standard sequence numbers.

## Validation checklist

1. Root contains 11 standard files (including two `6、`s) ending with `10、功能菜单与版本规划`
2. Each active version folder contains exactly 7 standard files with correct `{V}` suffix
3. `技术调研/` and `其他/` do not contain root-level standard docs
4. Module folders have PRD / Stitch / UI triplet (if project uses module-level docs)
5. No sequence numbers 1–7 used for non-standard docs in version folders

## Related skills

- [`documentation-builder`](../dev-utils-skills/documentation-builder): General doc writing and formatting conventions
- [`api-doc-generator`](api-doc-generator): OpenAPI and API documentation generation
