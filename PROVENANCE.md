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
| **Packages** | `github.com/full-stack-skills/<package>` | 47 independently versioned skill packages, each its own Git repo |
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

> **Important:** a package-level Apache-2.0 declaration covers the package's own
> content. Individual skills that derive from third-party projects retain their
> original license — see §3. Downstream redistributors should preserve the
> per-skill `LICENSE.txt` files intact.

---

## 3. Skill-level license exceptions

Most of the 671 skills in the collection are Apache-2.0. The following skills carry
a **different** license and must be treated accordingly.

### 3.1 Third-party MIT skills (retain original copyright)

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

### 3.2 First-party MIT skills (PartMe.AI authored)

These skills are authored by PartMe.AI but carry an MIT (rather than Apache-2.0)
skill-level license. This is an internal inconsistency, not a third-party claim.

| Package | Skills |
|---|---|
| `uniapp-skills` | `uniapp-ad`, `uniapp-cloud`, `uniapp-mini`, `uniapp-native-app`, `uniapp-native-plugin`, `uniapp-plugin`, `uniapp-project`, `uniappx-project` (8 skills, © 2024 partme-ai, MIT) |

### 3.3 Pointer-style declarations

12 skills carry a short pointer rather than the full license text. They are
Apache-2.0 by intent; the pointer refers to the package-level `LICENSE`:

- `pencil-skills/skills/pencil-design-from-stitch-html` — `Apache-2.0. See repository LICENSE.`
- `stitch-skills/skills/stitch-*` — 10 skills, same wording
- `agent-skills/skills/skill-trace-evaluation`, `skill-official-evaluation` — `Apache-2.0`

### 3.4 Skills whose content documents third-party tools

Many skills (e.g. `speckit-skills/*`, `openspec-skills/*`, `nvm-skills/*`,
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

---

## 4. Package inventory

47 packages, 671 skills. Each is an independent repository under the
`full-stack-skills` GitHub organization.

| Package | Skills | License | Repo |
|---|---:|---|---|
| `agent-skills` | 15 | Apache-2.0 (5 MIT skills, §3.1/§3.3) | [↗](https://github.com/full-stack-skills/agent-skills) |
| `angular-skills` | 1 | Apache-2.0 | [↗](https://github.com/full-stack-skills/angular-skills) |
| `antd-skills` | 4 | Apache-2.0 | [↗](https://github.com/full-stack-skills/antd-skills) |
| `ascii-skills` | 13 | Apache-2.0 | [↗](https://github.com/full-stack-skills/ascii-skills) |
| `avue-skills` | 3 | Apache-2.0 | [↗](https://github.com/full-stack-skills/avue-skills) |
| `build-skills` | 7 | Apache-2.0 (1 MIT skill, §3.1) | [↗](https://github.com/full-stack-skills/build-skills) |
| `chart-skills` | 2 | Apache-2.0 | [↗](https://github.com/full-stack-skills/chart-skills) |
| `cocos-skills` | 1 | Apache-2.0 (1 MIT skill, §3.1) | [↗](https://github.com/full-stack-skills/cocos-skills) |
| `database-skills` | 5 | Apache-2.0 | [↗](https://github.com/full-stack-skills/database-skills) |
| `ddd-skills` | 16 | Apache-2.0 | [↗](https://github.com/full-stack-skills/ddd-skills) |
| `ddd4j-skills` | 62 | Apache-2.0 | [↗](https://github.com/full-stack-skills/ddd4j-skills) |
| `design-skills` | 9 | Apache-2.0 | [↗](https://github.com/full-stack-skills/design-skills) |
| `devops-skills` | 10 | Apache-2.0 | [↗](https://github.com/full-stack-skills/devops-skills) |
| `docker-skills` | 16 | Apache-2.0 | [↗](https://github.com/full-stack-skills/docker-skills) |
| `document-skills` | 11 | Apache-2.0 (3 MIT skills, §3.4) | [↗](https://github.com/full-stack-skills/document-skills) |
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
| `pencil-skills` | 28 | Apache-2.0 (§3.3 pointer) | [↗](https://github.com/full-stack-skills/pencil-skills) |
| `python-skills` | 19 | Apache-2.0 | [↗](https://github.com/full-stack-skills/python-skills) |
| `react-skills` | 7 | Apache-2.0 | [↗](https://github.com/full-stack-skills/react-skills) |
| `rust-skills` | 29 | Apache-2.0 | [↗](https://github.com/full-stack-skills/rust-skills) |
| `social-skills` | 2 | Apache-2.0 | [↗](https://github.com/full-stack-skills/social-skills) |
| `speckit-skills` | 13 | Apache-2.0 (§3.4 tool) | [↗](https://github.com/full-stack-skills/speckit-skills) |
| `spring-skills` | 7 | Apache-2.0 | [↗](https://github.com/full-stack-skills/spring-skills) |
| `stitch-skills` | 29 | Apache-2.0 (§3.3 pointer) | [↗](https://github.com/full-stack-skills/stitch-skills) |
| `svelte-skills` | 16 | Apache-2.0 | [↗](https://github.com/full-stack-skills/svelte-skills) |
| `swift-skills` | 7 | Apache-2.0 | [↗](https://github.com/full-stack-skills/swift-skills) |
| `t2ui-skills` | 97 | Apache-2.0 | [↗](https://github.com/full-stack-skills/t2ui-skills) |
| `tauri-skills` | 52 | Apache-2.0 | [↗](https://github.com/full-stack-skills/tauri-skills) |
| `teaching-skills` | 3 | Apache-2.0 | [↗](https://github.com/full-stack-skills/teaching-skills) |
| `testing-skills` | 10 | Apache-2.0 | [↗](https://github.com/full-stack-skills/testing-skills) |
| `threejs-skills` | 18 | Apache-2.0 | [↗](https://github.com/full-stack-skills/threejs-skills) |
| `uniapp-skills` | 13 | Apache-2.0 (8 MIT skills, §3.2) | [↗](https://github.com/full-stack-skills/uniapp-skills) |
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
grep -r '^license:' <package>/skills/*/SKILL.md | grep -v 'Apache' | grep -v 'LICENSE.txt'

# Inspect a specific skill's license text
cat <package>/skills/<skill>/LICENSE.txt
```

Skill frontmatter declares the license with a `license:` field; when it reads
`Complete terms in LICENSE.txt`, the authoritative text is the `LICENSE.txt` file
in the same skill directory.

---

## 7. Known gaps

Tracked openly so reviewers do not have to discover them independently:

| Item | Status |
|---|---|
| `vue-skills/skills/pinia/LICENSE.txt` previously contained a `404: Not Found` fetch artifact | **Fixed 2026-09-11** — replaced with Apache-2.0 text |
| Package-level `LICENSE` files across 41 packages previously contained third-party notices rather than an Apache-2.0 grant | **Fixed 2026-09-11** — split into `LICENSE` (Apache-2.0) + `THIRD-PARTY-NOTICES.md` |
| `firmware-skills`, `zig-skills` had no `LICENSE` file | **Fixed 2026-09-11** — Apache-2.0 added |
| 8 first-party skills carry MIT instead of Apache-2.0 (§3.2) | Open — internal inconsistency; both are permissive |
| 12 skills use pointer-style license declarations (§3.3) | Open — intentional brevity; points to package `LICENSE` |

---

## 8. Contact

Provenance questions, corrections, or additional audit requests:
open an issue at [`partme-ai/full-stack-skills/issues`](https://github.com/partme-ai/full-stack-skills/issues).
