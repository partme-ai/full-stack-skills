---
name: ocrmypdf
description: OCRmyPDF core skill — add searchable OCR text layer to scanned PDFs, convert images to searchable PDFs, support 100+ languages via Tesseract. Use when the user needs to OCR a PDF, make a scanned PDF searchable, or extract text from scanned documents.
---

# OCRmyPDF — Core OCR Guide

## Overview

[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) adds an OCR text layer to scanned PDF files, allowing them to be searched or copy-pasted. It uses Tesseract OCR, supports 100+ languages, produces PDF/A by default, and distributes work across all CPU cores.

For image processing (deskew, rotate, clean), see the **ocrmypdf-image** skill. For optimization and PDF/A options, see **ocrmypdf-optimize**. For batch/Docker/scripting, see **ocrmypdf-batch**. For Python API and plugins, see **ocrmypdf-api**.

## Installation

### One-liner installs (recommended)

| OS | Command |
|----|---------|
| **Debian / Ubuntu** | `apt install ocrmypdf` |
| **Fedora** | `dnf install ocrmypdf tesseract-osd` |
| **macOS (Homebrew)** | `brew install ocrmypdf` |
| **macOS (MacPorts)** | `port install ocrmypdf` |
| **FreeBSD** | `pkg install py-ocrmypdf` |
| **Snap** | `snap install ocrmypdf` |

### pip install (latest version)

```bash
# After installing system dependencies (Tesseract, Ghostscript)
pip install ocrmypdf
```

### Verify

```bash
ocrmypdf --version
ocrmypdf --help
```

### Requirements

- **Python 3.11+**
- **Tesseract 4.1.1+** (OCR engine)
- **Ghostscript 9.54+** or **pypdfium2** (PDF rasterization)
- Optional: jbig2enc (compression), pngquant (image optimization), unpaper (cleaning)

## Quick Start

```bash
# Basic OCR — input scanned PDF, output searchable PDF/A
ocrmypdf input.pdf output.pdf

# OCR an image file directly
ocrmypdf --image-dpi 300 scan.png output.pdf

# OCR in place (only overwrites on success)
ocrmypdf myfile.pdf myfile.pdf
```

## Language Support

OCRmyPDF uses Tesseract language packs. Install them for your OS:

```bash
# Debian / Ubuntu
apt-cache search tesseract-ocr          # List all language packs
apt install tesseract-ocr-chi-sim       # Chinese Simplified
apt install tesseract-ocr-fra           # French

# macOS (Homebrew)
brew install tesseract-lang             # All languages

# Fedora
dnf search tesseract-langpack
dnf install tesseract-langpack-ita      # Italian
```

### Using languages

```bash
# Single language
ocrmypdf -l fra document.pdf output.pdf

# Multiple languages
ocrmypdf -l eng+fra bilingual.pdf output.pdf

# Chinese Simplified + English
ocrmypdf -l chi_sim+eng chinese-doc.pdf output.pdf
```

**Note**: Use [ISO 639-3 codes](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html) for language identifiers.

## OCR Modes

### Default mode (skip existing text)

```bash
# Skip pages that already have text — only OCR pages without text
ocrmypdf input.pdf output.pdf
```

### Force OCR (`--force-ocr` or `-m force`)

```bash
# Rasterize and OCR all pages, even those with existing text
ocrmypdf --force-ocr input.pdf output.pdf
# v17+ short form:
ocrmypdf -m force input.pdf output.pdf
```

### Redo OCR (`--redo-ocr` or `-m redo`)

```bash
# Replace existing OCR without rasterizing (preserves quality)
ocrmypdf --redo-ocr input.pdf output.pdf
# v17+ short form:
ocrmypdf -m redo input.pdf output.pdf
```

### Skip text (`--skip-text` or `-m skip`)

```bash
# Skip pages with any text, only OCR blank/image pages
ocrmypdf --skip-text input.pdf output.pdf
# v17+ short form:
ocrmypdf -m skip input.pdf output.pdf
```

### No OCR (image processing only)

```bash
# Apply image processing / PDF/A conversion without OCR
ocrmypdf --ocr-engine none input.pdf output.pdf
```

## Page Selection

```bash
# OCR only specific pages
ocrmypdf --pages 1,3,5-10 input.pdf output.pdf

# OCR only the first page, minimal changes elsewhere
ocrmypdf --pages 1 --output-type pdf --optimize 0 input.pdf output.pdf
```

## Output Types

```bash
# PDF/A (default) — for archival
ocrmypdf --output-type pdfa input.pdf output.pdf

# Standard PDF
ocrmypdf --output-type pdf input.pdf output.pdf

# Auto (v17+) — speculative PDF/A, falls back to standard PDF
ocrmypdf --output-type auto input.pdf output.pdf

# No output PDF — only produce sidecar text
ocrmypdf --output-type none --sidecar text.txt input.pdf -
```

## Sidecar Text File

```bash
# Produce a companion text file with OCR text
ocrmypdf --sidecar output.txt input.pdf output.pdf
```

## Metadata

```bash
# Set output PDF metadata
ocrmypdf --title "My Document" --author "Author Name" --subject "Subject" input.pdf output.pdf
```

## Parallel Processing

```bash
# Use 4 CPU cores (default: all available)
ocrmypdf --jobs 4 input.pdf output.pdf

# Single-threaded
ocrmypdf --jobs 1 input.pdf output.pdf
```

## Common Recipes

### Make a scanned PDF searchable

```bash
ocrmypdf scanned.pdf searchable.pdf
```

### Convert image to searchable PDF

```bash
ocrmypdf --image-dpi 300 scan.jpg output.pdf
```

### OCR a multilingual document

```bash
ocrmypdf -l eng+deu+fra multilingual.pdf output.pdf
```

### Re-OCR with newer Tesseract

```bash
ocrmypdf --redo-ocr old-ocr.pdf updated.pdf
```

### Strip all text/OCR from a PDF

```bash
ocrmypdf --ocr-engine none --force-ocr input.pdf stripped.pdf
```

## Quick Reference

| Task | Command |
|------|---------|
| Basic OCR | `ocrmypdf input.pdf output.pdf` |
| Specify language | `ocrmypdf -l fra input.pdf output.pdf` |
| Multiple languages | `ocrmypdf -l eng+fra input.pdf output.pdf` |
| Force re-OCR all pages | `ocrmypdf --force-ocr input.pdf output.pdf` |
| Replace existing OCR | `ocrmypdf --redo-ocr input.pdf output.pdf` |
| Skip pages with text | `ocrmypdf --skip-text input.pdf output.pdf` |
| Specific pages only | `ocrmypdf --pages 1,3,5-10 input.pdf output.pdf` |
| Output standard PDF | `ocrmypdf --output-type pdf input.pdf output.pdf` |
| Extract text sidecar | `ocrmypdf --sidecar text.txt input.pdf output.pdf` |
| Image to PDF | `ocrmypdf --image-dpi 300 image.png output.pdf` |
| In-place OCR | `ocrmypdf myfile.pdf myfile.pdf` |
| Set metadata | `ocrmypdf --title "Title" input.pdf output.pdf` |
| Parallel jobs | `ocrmypdf --jobs 4 input.pdf output.pdf` |

## Troubleshooting

- **"Tesseract not found"**: Install Tesseract and ensure it's on PATH.
- **Poor OCR quality**: Check language packs (`-l`), try `--deskew` (see ocrmypdf-image), or `--oversample 300`.
- **"Input file has text"**: Use `--force-ocr`, `--redo-ocr`, or `--skip-text` as appropriate.
- **Large output files**: See ocrmypdf-optimize for `--optimize` levels and JBIG2.
- **Signed PDFs**: Use `--invalidate-digital-signatures` to override (signatures will be invalidated).

## References

- [OCRmyPDF Documentation](https://ocrmypdf.readthedocs.io/en/latest/)
- [OCRmyPDF GitHub](https://github.com/ocrmypdf/OCRmyPDF)
- [Tesseract Language Packs](https://github.com/tesseract-ocr/tessdata)
- [OCRmyPDF Cookbook](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html)
