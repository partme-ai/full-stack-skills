---
name: nextjs
description: Guidance for Next.js using the official docs at nextjs.org/docs. Use when the user needs Next.js concepts, configuration, routing, data fetching, or API reference details.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Follow Next.js documentation topics (App Router, Pages Router, architecture, community)
- Implement Next.js routing, data fetching, caching, or deployment
- Use official APIs and configuration options from the docs

## How to use this skill

1. **Identify the topic** from the user request.
2. **Open the matching example file** in `examples/`.
3. **Follow the official Next.js docs** linked in the file.

## Mapping Rules (one-to-one with https://nextjs.org/docs)

The `examples/` directory mirrors the official docs structure:

- `examples/index.md` → https://nextjs.org/docs
- `examples/app/...` → https://nextjs.org/docs/app/...
- `examples/pages/...` → https://nextjs.org/docs/pages/...
- `examples/architecture/...` → https://nextjs.org/docs/architecture/...
- `examples/community/...` → https://nextjs.org/docs/community/...

**Path rule:**
- Remove numeric prefixes from doc folders and filenames (e.g., `01-app` → `app`).
- `index.mdx` pages map to `index.md` inside the corresponding directory.

## Resources
- Docs: https://nextjs.org/docs

## Keywords
Next.js, App Router, Pages Router, routing, data fetching, caching, server components, client components, middleware, deployment, configuration
