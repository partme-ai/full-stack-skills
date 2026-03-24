---
name: ocrmypdf-optimize
description: OCRmyPDF optimization skill — compress PDFs, configure PDF/A output, JBIG2 encoding, and lossless optimization. Use when the user needs to reduce PDF file size, create archival PDF/A files, or optimize OCR output.
---

# OCRmyPDF — Optimization Guide

## Overview

[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) provides extensive optimization options to reduce file size, create PDF/A archival documents, and configure output quality.

For core OCR functionality, see the **ocrmypdf** skill. For image processing (deskew, rotate, clean), see **ocrmypdf-image**. For batch/Docker/scripting, see **ocrmypdf-batch**.

## Compression Levels

```bash
# Level 0 — no optimization (fastest)
ocrmypdf --optimize 0 input.pdf output.pdf

# Level 1 — lossless (default)
ocrmypdf --optimize 1 input.pdf output.pdf

# Level 2 — lossy (aggressive)
ocrmypdf --optimize 2 input.pdf output.pdf

# Level 3 — lossless, aggressive JPEG recompression
ocrmypdf --optimize 3 input.pdf output.pdf
```

## PDF/A Output

PDF/A is an archival format with embedded fonts and colorspaces:

```bash
# PDF/A-1b (basic, default)
ocrmypdf --output-type pdfa input.pdf output.pdf

# PDF/A-2b (includes transparency)
ocrmypdf --output-type pdfa2b input.pdf output.pdf

# PDF/A-2u (Unicode)
ocrmypdf --output-type pdfa2u input.pdf output.pdf

# Standard PDF (no archival)
ocrmypdf --output-type pdf input.pdf output.pdf
```

## JBIG2 Encoding

JBIG2 provides excellent compression for monochrome (1-bit) images:

```bash
# Enable JBIG2 (requires jbig2enc)
ocrmypdf --jbig2-lossy input.pdf output.pdf  # Lossy

ocrmypdf --jbib2-lossless input.pdf output.pdf  # Lossless (v17+)
```

**Requirements**:

```bash
# Debian/Ubuntu
apt install jbig2enc

# macOS
brew install jbig2enc
```

## PNG Optimization

Optimize embedded PNG images:

```bash
# Use pngquant for lossy compression
ocrmypdf --png-lossy input.pdf output.pdf

# Lossless PNG optimization
ocrmypdf --png-lossless input.pdf output.pdf
```

## Ghostscript Options

Fine-tune PDF processing with Ghostscript:

```bash
# Set PDF minor version
ocrmypdf --pdf-renderer hatch input.pdf output.pdf

# Use pdfimages for better image extraction
ocrmypdf --pdf-renderer img2pdf input.pdf output.pdf
```

## Sidecar Text

Generate text file alongside PDF without modifying PDF:

```bash
# Generate sidecar only
ocrmypdf --output-type none --sidecar text.txt input.pdf output.pdf

# Typical sidecar workflow
ocrmypdf --sidecar text.txt --force-ocr input.pdf output.pdf
```

## Combined Recipes

### Maximum compression

```bash
ocrmypdf --optimize 3 --jbig2-lossy --png-lossy input.pdf small.pdf
```

### Archival PDF/A with compression

```bash
ocrmypdf --output-type pdfa --optimize 2 input.pdf archival.pdf
```

### Lossless output

```bash
ocrmypdf --output-type pdf --optimize 1 --png-lossless input.pdf lossless.pdf
```

## Quick Reference

| Task | Command |
|------|---------|
| No optimization | `--optimize 0` |
| Lossless default | `--optimize 1` |
| Aggressive lossy | `--optimize 2` |
| Max quality | `--optimize 3` |
| PDF/A-1b (default) | `--output-type pdfa` |
| PDF/A-2b | `--output-type pdfa2b` |
| JBIG2 lossy | `--jbig2-lossy` |
| PNG lossy | `--png-lossy` |
| Sidecar text | `--sidecar text.txt` |

## Troubleshooting

- **Large file size**: Try `--optimize 2` or `--png-lossy`.
- **PDF/A validation fails**: Use `--output-type pdfa2b` for better compatibility.
- **Font issues**: PDF/A-2u ensures full Unicode support.