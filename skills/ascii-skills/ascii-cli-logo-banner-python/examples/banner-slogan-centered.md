# ascii-cli-logo-banner-python: centered slogan + hint

## Run

```bash
python3 scripts/generate_banner.py \
  --brand "SPECIFY" \
  --width 80 \
  --glyph block \
  --slogan "GitHub Spec Kit - Spec-Driven Development Toolkit" \
  --hint "Run 'specify --help' for usage information" \
  --no-rule
```

## Notes
- `--glyph block` uses `█` for a solid logo look.
- `--no-rule` prints a “hero” style output (logo + centered lines), without the info block.
