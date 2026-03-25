Hey 👋 @partme-ai

I ran your skills through `tessl skill review` at work and found some targeted improvements across all 421 skills. Here's the full before/after:

![Score Card](score_card.png)

**Overall: 53% → 86% average (+32 percentage points) across 421 skills — 345 improved, 74 unchanged, 2 minor regressions.**

| Skill Group | Skills | Before | After | Change |
|-------------|--------|--------|-------|--------|
| stitch-skills | 28 | 4% | 88% | +83% |
| tauri-skills | 52 | 32% | 89% | +57% |
| nvm-skills | 15 | 45% | 95% | +49% |
| social-skills | 2 | 40% | 84% | +43% |
| t2ui-skills | 97 | 46% | 87% | +41% |
| document-skills | 5 | 42% | 79% | +37% |
| vscode-skills | 4 | 58% | 91% | +34% |
| teaching-skills | 3 | 54% | 87% | +32% |
| avue-skills | 3 | 62% | 94% | +31% |
| electron-skills | 3 | 47% | 78% | +31% |
| svelte-skills | 1 | 64% | 94% | +30% |
| uview-skills | 2 | 66% | 94% | +28% |
| mobile-native-skills | 2 | 60% | 86% | +26% |
| drawio-skills | 2 | 66% | 92% | +26% |
| database-skills | 5 | 64% | 89% | +25% |
| speckit-skills | 13 | 61% | 85% | +24% |
| pencil-skills | 28 | 60% | 83% | +22% |
| antd-skills | 4 | 66% | 88% | +22% |
| chart-skills | 2 | 64% | 86% | +22% |
| devops-skills | 6 | 68% | 88% | +20% |
| python-skills | 3 | 68% | 87% | +19% |
| go-skills | 2 | 66% | 84% | +19% |
| nodejs-skills | 4 | 68% | 86% | +18% |
| utility-skills | 3 | 64% | 81% | +18% |
| ascii-skills | 13 | 70% | 86% | +16% |
| build-skills | 6 | 69% | 85% | +16% |
| dev-utils-skills | 13 | 63% | 78% | +15% |
| angular-skills | 1 | 70% | 85% | +15% |
| design-skills | 4 | 59% | 73% | +14% |
| react-skills | 6 | 75% | 88% | +14% |
| threejs-skills | 18 | 84% | 95% | +11% |
| ddd-skills | 6 | 71% | 82% | +11% |
| flutter-skills | 2 | 72% | 83% | +10% |
| testing-skills | 9 | 73% | 83% | +9% |
| uniapp-skills | 13 | 58% | 67% | +9% |
| spring-skills | 7 | 75% | 81% | +5% |
| docker-skills | 2 | 84% | 88% | +4% |
| vue-skills | 7 | 72% | 74% | +2% |
| vue-ui-skills | 4 | 70% | 70% | 0% |
| openspec-skills | 15 | 88% | 88% | 0% |
| ocrmypdf-skills | 5 | 93% | 93% | 0% |
| cocos-skills | 1 | 71% | 71% | 0% |

<details>
<summary>Changes made</summary>

### Validation fixes (biggest impact on 0% skills)
- **Fixed `allowed-tools` format** in 26 stitch-skills: converted YAML arrays to comma-separated quoted strings (the spec requires a string, not an array)
- **Fixed descriptions exceeding 1024 chars** in mermaid, plantuml, and several others — trimmed while preserving key trigger terms
- **Fixed YAML parse errors** in plantuml frontmatter
- **Fixed `name` field** in internal-comms and uniapp-mini to match kebab-case requirements

### Description improvements (all 421 skills)
- Converted `>-` chevron descriptions to quoted strings for consistent formatting
- Added explicit "Use when..." trigger clauses where missing
- Made descriptions more specific and action-oriented (e.g., "Provides comprehensive guidance" → "Creates, debugs, and configures...")
- Ensured all descriptions include concrete trigger terms users would naturally say

### Content improvements (345 skills)
- Added executable code examples (real, runnable snippets — not pseudocode) to skills that only had bullet points or topic outlines
- Added numbered workflow steps with validation checkpoints
- Expanded thin Chinese-only content with English equivalents while preserving all existing domain-specific content
- Added concrete CLI commands with actual arguments (e.g., `ng generate component user-profile --standalone`)
- Added troubleshooting sections for common error scenarios in framework skills

### Skills left unchanged (76)
- High-scoring skills (90%+) like openspec, ocrmypdf, and well-structured vue/spring/threejs skills were not modified beyond formatting
- Skills with deep, well-structured domain content that would not benefit from changes

### Minor regressions (2)
- `java-code-comments` (74% → 68%) and `mybatis-plus-generator` (77% → 74%): description improved to 100%, but the existing verbose body content (450+ lines of domain-specific Chinese content) was scored more harshly. The body was preserved as-is to maintain domain expertise.

</details>

Honest disclosure — I work at @tesslio where we build tooling around skills like these. Not a pitch - just saw room for improvement and wanted to contribute.

Want to self-improve your skills? Just point your agent (Claude Code, Codex, etc.) at [this Tessl guide](https://docs.tessl.io/evaluate/optimize-a-skill-using-best-practices) and ask it to optimize your skill. Ping me - [@rohan-tessl](https://github.com/rohan-tessl) - if you hit any snags.

Thanks in advance 🙏
