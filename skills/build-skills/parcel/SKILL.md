---
name: parcel
description: "Provides comprehensive guidance for Parcel bundler including zero-configuration setup, asset handling, hot module replacement, code splitting, and production builds. Use when the user asks about Parcel, needs a zero-config build tool, or wants to bundle web applications quickly."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Set up a zero-configuration bundler for web applications
- Bundle JavaScript, CSS, HTML, images, and other assets automatically
- Use hot module replacement (HMR) for fast development
- Configure multi-entry builds, environment variables, and production output
- Migrate from or compare with Webpack/Vite

## How to use this skill

### Workflow

1. **Install** — add Parcel as a dev dependency
2. **Point to entry** — specify HTML or JS entry file
3. **Develop** — run `parcel` for dev server with HMR
4. **Build** — run `parcel build` for optimized production output
5. **Validate** — check output size and asset hashing

### Quick Start Example

```bash
# Install
npm install --save-dev parcel

# Development server with HMR
npx parcel src/index.html

# Production build
npx parcel build src/index.html --dist-dir dist
```

```json
// package.json
{
  "source": "src/index.html",
  "scripts": {
    "dev": "parcel",
    "build": "parcel build"
  }
}
```

```html
<!-- src/index.html — Parcel resolves dependencies automatically -->
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="./styles.css" />
</head>
<body>
  <div id="app"></div>
  <script type="module" src="./index.js"></script>
</body>
</html>
```

### Multi-Entry and Environment Variables

```bash
# Multiple entry points
npx parcel src/index.html src/admin.html

# Environment variables (available as process.env.API_URL)
API_URL=https://api.example.com npx parcel src/index.html
```

### Custom Configuration

```json
// .parcelrc — override default plugins when needed
{
  "extends": "@parcel/config-default",
  "transformers": {
    "*.svg": ["@parcel/transformer-svg-react"]
  }
}
```

## Best Practices

- Keep entry files and asset structure clear; Parcel auto-resolves dependencies
- Use `parcel build` with content hashing (default) for production caching
- Configure targets in `package.json` for library builds vs. app builds
- For large projects, evaluate performance against Vite or Webpack
- Use `.env` files for environment-specific configuration

## Reference

- Official documentation: https://parceljs.org/

## Keywords

parcel, bundler, zero-config, HMR, hot module replacement, code splitting, web bundling
