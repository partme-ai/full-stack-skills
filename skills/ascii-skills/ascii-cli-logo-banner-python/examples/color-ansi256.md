# ascii-cli-logo-banner-python: ANSI color (ansi256)

This example colorizes the logo using ANSI 256 colors while keeping spacing alignment safe (spaces are not colorized).

## Run

```bash
python3 scripts/generate_banner.py \
  --brand "SPECIFY" \
  --width 80 \
  --glyph ascii \
  --slogan "GitHub Spec Kit - Spec-Driven Development Toolkit" \
  --hint "Run 'specify --help' for usage information" \
  --no-rule \
  --colorMode ansi256 \
  --colorStart 46 \
  --colorEnd 196
```


## Notes
- If output is redirected to a file, consider disabling color (`--colorMode none`) to keep raw text clean.
