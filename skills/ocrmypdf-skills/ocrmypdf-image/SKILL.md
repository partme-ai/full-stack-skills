---
name: ocrmypdf-image
description: OCRmyPDF image processing skill — deskew, rotate, clean, despeckle, remove border from scanned documents. Use when the user needs to improve scanned PDF quality, fix skewed pages, remove noise, or clean up scanned documents before OCR.
---

# OCRmyPDF — Image Processing Guide

## Overview

[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) includes powerful image processing capabilities to improve scan quality before OCR. These tools help fix skewed pages, remove noise, clean borders, and enhance readability.

For core OCR functionality, see the **ocrmypdf** skill. For optimization and PDF/A options, see **ocrmypdf-optimize**. For batch/Docker/scripting, see **ocrmypdf-batch**.

## Deskew

Deskew corrects pages that are slightly rotated (e.g., from feed scanner skew).

```bash
# Auto deskew (recommended)
ocrmypdf --deskew input.pdf output.pdf

# Force deskew even if rotation is minimal
ocrmypdf --deskew --force-ocr input.pdf output.pdf
```

## Rotation

Rotate pages to correct upside-down or sideways scans:

```bash
# Auto-rotate based on text orientation
ocrmypdf --rotate-pages input.pdf output.pdf

# Force rotate all pages
ocrmypdf --rotate-pages --force-ocr input.pdf output.pdf
```

## Remove Borders / Cleaning

Remove unwanted borders, artifacts, and noise from scanned pages:

```bash
# Remove borders (dots, solid borders)
ocrmypdf --remove-bordering input.pdf output.pdf

# Combine with cleanup
ocrmypdf --remove-bordering --clean input.pdf output.pdf
```

## Despeckle

Remove speckles and isolated noise pixels:

```bash
# Remove speckles
ocrmypdf --despeckle input.pdf output.pdf

# Aggressive despeckle for very noisy scans
ocrmypdf --despeckle --clean input.pdf output.pdf
```

## Unpaper

[unpaper](https://github.com/Flameeyes/unpaper) provides advanced post-processing:

```bash
# Apply unpaper with default settings
ocrmypdf --unpaper input.pdf output.pdf

# Custom unpaper board options
ocrmypdf --unpaper-args "--board A4" input.pdf output.pdf
```

## Oversampling

Increase image resolution before OCR for better accuracy:

```bash
# Oversample to 300 DPI before OCR
ocrmypdf --oversample 300 input.pdf output.pdf

# Common for low-resolution scans
ocrmypdf --oversample 400 input.pdf output.pdf
```

## Combined Recipes

### Fix a skewed scan

```bash
ocrmypdf --deskew --remove-bordering --despeckle scanned.pdf fixed.pdf
```

### Clean up a very noisy scan

```bash
ocrmypdf --deskew --rotate-pages --despeckle --clean --oversample 300 noisy.pdf clean.pdf
```

### Remove all artifacts

```bash
ocrmypdf --remove-bordering --unpaper --despeckle dirty.pdf clean.pdf
```

## Quick Reference

| Task | Command |
|------|---------|
| Auto deskew | `--deskew` |
| Auto rotate | `--rotate-pages` |
| Remove borders | `--remove-bordering` |
| Remove speckles | `--despeckle` |
| Unpaper | `--unpaper` |
| Oversample DPI | `--oversample N` |

## Troubleshooting

- **Poor OCR after cleaning**: Try `--oversample 300` to increase input quality.
- **Artifacts remain**: Use `--unpaper` for aggressive cleanup.
- **Over-cleaned image**: Reduce cleaning options for preserve original quality.