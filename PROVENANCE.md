# Package Provenance & Redistribution Terms

This document records the provenance, licensing, and redistribution terms for the
`full-stack-skills` collection, so downstream consumers and directory reviewers can
audit it without guesswork.

_Last updated: 2026-09-11_

---

## 1. Collection structure

The collection is **not a single monolithic repository**. It is composed of:

| Layer | Location | Contents |
|---|---|---|
| **Hub** | `github.com/partme-ai/full-stack-skills` | Catalog, docs, platform guide. **No skill code.** |
| **Packages** | `github.com/full-stack-skills/<package>` | 49 independently versioned skill packages (each its own Git repo); `boss-skills` exists in the worktree but is excluded — see §4 |
| **Skills** | `<package>/skills/<skill-name>/` | One directory per skill, containing `SKILL.md` + optional `references/`, `examples/`, `scripts/`, `assets/` |

Skills are installed individually via the standard Agent Skills mechanism:

```bash
npx skills add full-stack-skills/<package>                  # whole package
npx skills add full-stack-skills/<package> --skill <name>   # single skill
```

Because installs are granular, a skill must not rely on sibling skills being present.

---

## 2. Licensing layers

Licensing is **three-tiered**. The applicable license for a given skill is the most
specific one that applies:

| Tier | Scope | License |
|---|---|---|
| Hub | `partme-ai/full-stack-skills` | Apache-2.0 (see [`LICENSE`](LICENSE)) |
| Package | Each `full-stack-skills/<package>` repo | Apache-2.0 (each repo's `LICENSE`) |
| Skill | `<package>/skills/<skill>/LICENSE.txt` | Apache-2.0 **or an exception listed in §3** |

Third-party components embedded in this collection (fonts, libraries, bundled media)
are attributed in [`THIRD-PARTY-NOTICES.md`](THIRD-PARTY-NOTICES.md).

> **Skill-level license scheme (unified 2026-09-11).** Every skill declares its
> license in the `SKILL.md` frontmatter `license:` field, with exactly two values:
>
> | Value | Applies to | Count |
> |---|---|---:|
> | `Apache-2.0` | First-party skills authored by PartMe.AI | 636 |
> | `MIT` | Skills whose content derives from, or is authored by, a third party | 35 |
>
> The MIT set is itemized in §3.1 and §3.2 below. Skills must not be relicensed to
> Apache-2.0 if their content originated elsewhere — that is the whole point of the
> exception list.

> **Important:** a package-level Apache-2.0 declaration covers the package's own
> content. Individual skills that derive from third-party projects retain their
> original license — see §3. Downstream redistributors should preserve the
> per-skill `LICENSE.txt` files intact.

---

## 3. Skill-level license exceptions

Most of the 671 skills in the collection are Apache-2.0. The following skills carry
a **different** license and must be treated accordingly.

### 3.1 Upstream-derived skills (content copied or adapted from other projects)

A subset of skills reproduce, or are closely adapted from, skills published by other
projects. Each such skill carries a **`LICENSE.txt`** in its own directory and a
**来源声明 / source note** at the top of its `SKILL.md`. The applicable licence is
the upstream one — not the package's Apache-2.0.

| Package | Skills | Upstream source | Upstream license | Copyright |
|---|---:|---|---|---|
| `speckit-skills` | 9 skills (`analyze`, `checklist`, `clarify`, `constitution`, `implement`, `plan`, `specify`, `tasks`, `taskstoissues`) | [`github/spec-kit`](https://github.com/github/spec-kit) | **MIT** | Copyright GitHub, Inc. |
| `python-skills` | 16 skills (`python-type-safety`, `python-testing-patterns`, `architecture-patterns`, `python-observability`, `python-code-style`, `python-anti-patterns`, `python-error-handling`, `python-background-jobs`, `python-resource-management`, `python-project-structure`, `python-configuration`, `python-resilience`, `python-performance-optimization`, `python-packaging`, `fastapi-templates`, `python-design-patterns`) | [`wshobson/agents`](https://github.com/wshobson/agents) | **MIT** | Copyright (c) 2024 Seth Hobson |
| `devops-skills` | `spark-optimization` | [`wshobson/agents`](https://github.com/wshobson/agents) | **MIT** | Copyright (c) 2024 Seth Hobson |
| `stitch-skills` | `stitch-design-md`, `stitch-ui-prompt-architect` | [`google-labs-code/stitch-skills`](https://github.com/google-labs-code/stitch-skills) | **Apache-2.0** | Google LLC and contributors |
| `agent-skills` | `browser-trace` | [`browserbase/skills`](https://github.com/browserbase/skills) | **MIT** | Copyright (c) 2026 Browserbase, Inc. |

**Note on `speckit-skills` (2026-09-11):** an earlier revision of the 10
`speckit-*` skills was found to be near-verbatim identical to a third-party packaging
of the same prompts that is published under AGPL-3.0. Because the *content* originates
with `github/spec-kit` (MIT), those skills were **regenerated directly from the MIT
upstream** rather than from the AGPL-3.0 packaging. The current text matches the MIT
source at 0.96–0.99 similarity and carries the MIT notice. `speckit-baseline` has no
official Spec Kit counterpart, so its analysis workflow was rewritten as first-party
content that reuses only the (MIT) spec-structure conventions.

**Redistribution:** for these skills, preserve the `LICENSE.txt` and the source note
in any copy or substantial portion. Where the upstream license is MIT, that means
carrying the copyright notice and permission text. Where it is Apache-2.0, that means
carrying the license text and stating any modifications (this project adapts and
integrates the upstream content).

### 3.2 Third-party MIT skills (retain original copyright)

These skills were authored by or derived from third-party projects and are
distributed under their original MIT license. **Their copyright notices must be
preserved.**

| Package | Skill | Copyright holder | License |
|---|---|---|---|
| `agent-skills` | `browser-trace` | Browserbase, Inc. | MIT |
| `agent-skills` | `codebase-design` | Matt Pocock | MIT |
| `agent-skills` | `caveman` | Julius Brussee | MIT |
| `build-skills` | `rspack` | Bytedance Inc and its affiliates | MIT |
| `cocos-skills` | `cocos2d-x` | (see skill `LICENSE.txt`) | MIT |

All five carry a per-skill `LICENSE.txt` with the original copyright notice. On
2026-09-11 their frontmatter `license:` fields were set to `MIT`; `caveman` and
`codebase-design` had been missing the field entirely, and `rspack` / `cocos2d-x`
had been pointing at `LICENSE.txt` in a way that obscured the MIT grant.

### 3.3 First-party MIT skills — resolved 2026-09-11

**No skills remain in this category.** Eight `uniapp-skills` skills were previously
authored by PartMe.AI under MIT (`Copyright (c) 2024 partme-ai`) while the package
README and badge declared Apache-2.0. To remove the inconsistency, the frontmatter
`license:` field and the per-skill `LICENSE.txt` were converted to Apache-2.0 on
2026-09-11, matching the package declaration.

| Package | Skills | Was | Now |
|---|---|---|---|
| `uniapp-skills` | `uniapp-ad`, `uniapp-cloud`, `uniapp-mini`, `uniapp-native-app`, `uniapp-native-plugin`, `uniapp-plugin`, `uniapp-project`, `uniappx-project` | MIT (© partme-ai) | Apache-2.0 |

### 3.4 Pointer-style license text

A small number of skills ship a short pointer in their `LICENSE.txt` rather than the
full license text. They are Apache-2.0 by intent; the pointer refers to the
package-level `LICENSE`:

- `pencil-skills/skills/pencil-design-from-stitch-html` — `Apache-2.0. See repository LICENSE.`
- `stitch-skills/skills/stitch-*` — 10 skills, same wording
- `agent-skills/skills/skill-trace-evaluation`, `skill-official-evaluation` — `Apache-2.0`

Their frontmatter `license:` field reads `Apache-2.0`.

### 3.5 Skills whose content documents third-party tools

Many skills (e.g. `openspec-skills/*`, `nvm-skills/*`,
`document-skills/markitdown-*`) document **how to use** third-party tools and
services. The skill text is first-party; the referenced tools belong to their
respective owners:

| Skill group | Third-party tool referenced | Tool's license |
|---|---|---|
| `speckit-skills` | [GitHub spec-kit](https://github.com/github/spec-kit) | MIT |
| `openspec-skills` | OpenSpec | see upstream project |
| `nvm-skills` | [nvm](https://github.com/nvm-sh/nvm) (`based on the official README`) | MIT |
| `document-skills/markitdown-*` | [Microsoft MarkItDown](https://github.com/microsoft/markitdown) | MIT |
| `firmware-skills` | OpenWrt / [ophub](https://github.com/ophub) Amlogic builds, ESP-IDF | see upstream projects |

These skills do not copy upstream source code; they provide original guidance and
link to the upstream documentation as the source of truth.

Three of them — `document-skills/markitdown-awesome`, `markitdown-cli`,
`markitdown-ocr` — are written directly against Microsoft MarkItDown's CLI source
(`packages/markitdown/src/markitdown/__main__.py`). They therefore declare
`license: MIT` and credit the upstream project, rather than being relicensed to
Apache-2.0. No upstream source code is copied.

---

## 4. Package inventory

49 packages, 693 skills (counted by `find <pkg>/skills -maxdepth 1 -mindepth 1 -type d` on 2026-09-16). The `boss-skills` directory is excluded because it is an old mixed-in personal scratch dir with no `skills/` subfolder. Each is an independent repository under the `full-stack-skills` GitHub organization.

| Package | Skills | License | Repo |
|---|---:|---|---|
| `agent-skills` | 15 | Apache-2.0 (1 MIT-derived §3.1; 3 MIT §3.2; 2 pointer §3.4) | [↗](https://github.com/full-stack-skills/agent-skills) |
| `angular-skills` | 1 | Apache-2.0 | [↗](https://github.com/full-stack-skills/angular-skills) |
| `antd-skills` | 4 | Apache-2.0 | [↗](https://github.com/full-stack-skills/antd-skills) |
| `ascii-skills` | 13 | Apache-2.0 | [↗](https://github.com/full-stack-skills/ascii-skills) |
| `avue-skills` | 3 | Apache-2.0 | [↗](https://github.com/full-stack-skills/avue-skills) |
| `build-skills` | 7 | Apache-2.0 (1 MIT skill, §3.2) | [↗](https://github.com/full-stack-skills/build-skills) |
| `chart-skills` | 2 | Apache-2.0 | [↗](https://github.com/full-stack-skills/chart-skills) |
| `cocos-skills` | 1 | Apache-2.0 (1 MIT skill, §3.2) | [↗](https://github.com/full-stack-skills/cocos-skills) |
| `database-skills` | 5 | Apache-2.0 | [↗](https://github.com/full-stack-skills/database-skills) |
| `ddd-skills` | 16 | Apache-2.0 | [↗](https://github.com/full-stack-skills/ddd-skills) |
| `ddd4j-skills` | 62 | Apache-2.0 | [↗](https://github.com/full-stack-skills/ddd4j-skills) |
| `design-skills` | 9 | Apache-2.0 | [↗](https://github.com/full-stack-skills/design-skills) |
| `devops-skills` | 10 | Apache-2.0 (1 MIT-derived skill, §3.1) | [↗](https://github.com/full-stack-skills/devops-skills) |
| `docker-skills` | 16 | Apache-2.0 | [↗](https://github.com/full-stack-skills/docker-skills) |
| `document-skills` | 11 | Apache-2.0 (3 MIT skills, §3.5) | [↗](https://github.com/full-stack-skills/document-skills) |
| `drawio-skills` | 2 | Apache-2.0 | [↗](https://github.com/full-stack-skills/drawio-skills) |
| `electron-skills` | 3 | Apache-2.0 | [↗](https://github.com/full-stack-skills/electron-skills) |
| `firmware-skills` | 20 | Apache-2.0 | [↗](https://github.com/full-stack-skills/firmware-skills) |
| `flutter-skills` | 2 | Apache-2.0 | [↗](https://github.com/full-stack-skills/flutter-skills) |
| `go-skills` | 2 | Apache-2.0 | [↗](https://github.com/full-stack-skills/go-skills) |
| `java-skills` | 39 | Apache-2.0 | [↗](https://github.com/full-stack-skills/java-skills) |
| `kotlin-skills` | 7 | Apache-2.0 | [↗](https://github.com/full-stack-skills/kotlin-skills) |
| `nodejs-skills` | 4 | Apache-2.0 | [↗](https://github.com/full-stack-skills/nodejs-skills) |
| `nvm-skills` | 15 | Apache-2.0 | [↗](https://github.com/full-stack-skills/nvm-skills) |
| `ocrmypdf-skills` | 5 | Apache-2.0 | [↗](https://github.com/full-stack-skills/ocrmypdf-skills) |
| `openspec-skills` | 15 | Apache-2.0 | [↗](https://github.com/full-stack-skills/openspec-skills) |
| `pencil-skills` | 28 | Apache-2.0 (§3.4 pointer) | [↗](https://github.com/full-stack-skills/pencil-skills) |
| `python-skills` | 19 | Apache-2.0 (16 MIT-derived skills, §3.1) | [↗](https://github.com/full-stack-skills/python-skills) |
| `react-skills` | 7 | Apache-2.0 | [↗](https://github.com/full-stack-skills/react-skills) |
| `rust-skills` | 29 | Apache-2.0 | [↗](https://github.com/full-stack-skills/rust-skills) |
| `social-skills` | 2 | Apache-2.0 | [↗](https://github.com/full-stack-skills/social-skills) |
| `speckit-skills` | 13 | Apache-2.0 (10 MIT-derived skills, §3.1) | [↗](https://github.com/full-stack-skills/speckit-skills) |
| `spring-skills` | 7 | Apache-2.0 | [↗](https://github.com/full-stack-skills/spring-skills) |
| `stitch-skills` | 29 | Apache-2.0 (2 Apache-2.0-derived §3.1; 10 pointer §3.4) | [↗](https://github.com/full-stack-skills/stitch-skills) |
| `svelte-skills` | 16 | Apache-2.0 | [↗](https://github.com/full-stack-skills/svelte-skills) |
| `swift-skills` | 7 | Apache-2.0 | [↗](https://github.com/full-stack-skills/swift-skills) |
| `t2ui-skills` | 97 | Apache-2.0 | [↗](https://github.com/full-stack-skills/t2ui-skills) |
| `tauri-skills` | 52 | Apache-2.0 | [↗](https://github.com/full-stack-skills/tauri-skills) |
| `teaching-skills` | 3 | Apache-2.0 | [↗](https://github.com/full-stack-skills/teaching-skills) |
| `testing-skills` | 10 | Apache-2.0 | [↗](https://github.com/full-stack-skills/testing-skills) |
| `threejs-skills` | 18 | Apache-2.0 | [↗](https://github.com/full-stack-skills/threejs-skills) |
| `uniapp-skills` | 13 | Apache-2.0 (§3.3 resolved 2026-09-11) | [↗](https://github.com/full-stack-skills/uniapp-skills) |
| `uview-skills` | 2 | Apache-2.0 | [↗](https://github.com/full-stack-skills/uview-skills) |
| `vscode-skills` | 4 | Apache-2.0 | [↗](https://github.com/full-stack-skills/vscode-skills) |
| `vue-skills` | 7 | Apache-2.0 | [↗](https://github.com/full-stack-skills/vue-skills) |
| `vue-ui-skills` | 4 | Apache-2.0 | [↗](https://github.com/full-stack-skills/vue-ui-skills) |
| `zig-skills` | 15 | Apache-2.0 | [↗](https://github.com/full-stack-skills/zig-skills) |

---

## 5. Redistribution

- **Apache-2.0 content** may be redistributed under Apache-2.0 terms. Preserve
  `LICENSE` and `NOTICE`-style attributions.
- **MIT content (§3.1, §3.2)** may be redistributed under MIT terms. The copyright
  notice and permission notice must be included in all copies or substantial
  portions.
- **Bundled third-party material** is attributed in
  [`THIRD-PARTY-NOTICES.md`](THIRD-PARTY-NOTICES.md). Redistributors should carry
  that file forward.
- **No warranty**: skills are provided "AS IS", without warranty of any kind, as
  set out in the applicable license.

---

## 6. How to audit this yourself

```bash
# Clone a package and inspect its license
git clone https://github.com/full-stack-skills/<package>.git
cat <package>/LICENSE                      # package-level license

# Find skills with a non-default license
grep -r '^license:' <package>/skills/*/SKILL.md | grep -v 'Apache-2.0'

# Inspect a specific skill's license text
cat <package>/skills/<skill>/LICENSE.txt
```

Skill frontmatter declares the license with a `license:` field, which is either
`Apache-2.0` (first-party) or `MIT` (third-party or upstream-derived, §3.1–§3.2).
For MIT skills the authoritative copyright text is the `LICENSE.txt` file in the
same skill directory.

---

## 7. Known gaps

Tracked openly so reviewers do not have to discover them independently:

| Item | Status |
|---|---|
| Package-level `LICENSE` files across 41 packages contained third-party notices rather than an Apache-2.0 grant | **Fixed 2026-09-11** — split into `LICENSE` (Apache-2.0) + `THIRD-PARTY-NOTICES.md` |
| `firmware-skills`, `zig-skills` had no `LICENSE` file | **Fixed 2026-09-11** — Apache-2.0 added |
| `vue-skills/skills/pinia/LICENSE.txt` contained a `404: Not Found` fetch artifact | **Fixed 2026-09-11** — replaced with Apache-2.0 text |
| 17 upstream-derived skills (`python-skills` ×16, `devops-skills` ×1) carried no upstream attribution, violating the MIT notice requirement | **Fixed 2026-09-11** — per-skill `LICENSE.txt` + source note added (§3.1) |
| 2 `stitch-skills` skills reproduced Apache-2.0 upstream text without attribution | **Fixed 2026-09-11** — per-skill `LICENSE.txt` + source note added (§3.1) |
| 10 `speckit-skills` skills were near-verbatim from an AGPL-3.0 third-party packaging | **Fixed 2026-09-11** — regenerated from the MIT upstream `github/spec-kit` (§3.1) |
| READMEs stated "460+ skills / 42 packages" | **Fixed 2026-09-11** — corrected to 671 skills / 47 packages |
| READMEs / `Package inventory` still stated "47 packages / 671 skills" while the upstream worktrees already had **8 unlisted packages** (`agent-skills`, `boss-skills` [excluded as scratch], `ddd4j-skills`, `firmware-skills`, `kotlin-skills`, `processon-skills`, `skills-toolchain`, `swift-skills`) and **3 phantom rows** (`dev-utils-skills`, `mobile-native-skills`, `utility-skills`) | **Fixed 2026-09-16** — `zh`/`en` README + `PROVENANCE §4` corrected to 49 packages / 693 skills; `boss-skills` explicitly excluded with rationale; all 16 category sub-tables now match upstream `main` HEAD counts |
| 8 first-party skills carry MIT instead of Apache-2.0 (§3.3) | **Fixed 2026-09-11** — converted to Apache-2.0 (frontmatter + `LICENSE.txt`) |
| 12 skills use pointer-style license declarations (§3.4) | **Fixed 2026-09-11** — frontmatter normalized to `Apache-2.0`; pointer text remains only in `LICENSE.txt` |
| 296 skills carried no `license:` frontmatter field at all | **Fixed 2026-09-11** — 294 set to `Apache-2.0`; 2 third-party set to `MIT` |
| 4 different license value spellings (`Complete terms in LICENSE.txt` ×214, `Apache-2.0` ×127, `MIT` ×31, `Apache 2.0` ×1) | **Fixed 2026-09-11** — unified: `Apache-2.0` (636) / `MIT` (35) |
| `build-skills/rspack` and `cocos-skills/cocos2d-x` pointed at `LICENSE.txt` while their actual license is third-party MIT | **Fixed 2026-09-11** — frontmatter corrected to `MIT` |
| 5 skills had unparseable YAML frontmatter (unquoted colon inside `description:`) | **Fixed 2026-09-11** — description values quoted |

## 8. Contact

Provenance questions, corrections, or additional audit requests:
open an issue at [`partme-ai/full-stack-skills/issues`](https://github.com/partme-ai/full-stack-skills/issues).
