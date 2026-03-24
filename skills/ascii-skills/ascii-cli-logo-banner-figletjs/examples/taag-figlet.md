# ascii-cli-logo-banner-figletjs: FIGlet/TAAG-style output (via figlet.js options)

This example shows how to reproduce TAAG-like text output by using the `figlet` npm package (powered by `figlet.js`).

## Install dependency

```bash
npm install figlet
```

## Run

```bash
node scripts/figlet_banner.mjs \
  --brand "PartmeAI" \
  --version "1.2.3" \
  --repo "https://github.com/partme-ai/partme-cli" \
  --width 80 \
  --font "Ghost" \
  --slogan "GitHub Spec Kit - Spec-Driven Development Toolkit" \
  --hint "Run 'specify --help' for usage information" \
  --no-rule \
  --horizontalLayout "default" \
  --verticalLayout "default" \
  --whitespaceBreak true
```

## Notes
- `horizontalLayout` and `verticalLayout` match the common FIGlet layout options (default/full/fitted/controlled smushing/universal smushing).
- For narrow terminals (`width < 60`), the script prints a compact fallback banner (no big-letter logo).
