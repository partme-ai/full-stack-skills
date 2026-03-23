---
name: ocrmypdf-api
description: OCRmyPDF Python API and plugin skill — use OCRmyPDF programmatically from Python, integrate with applications, and extend with plugins (EasyOCR, PaddleOCR, AppleOCR). Use when the user needs to call OCRmyPDF from Python code, build OCR pipelines, or use alternative OCR engines.
---

# OCRmyPDF — Python API & Plugins Guide

## Overview

OCRmyPDF provides a Python API for programmatic use and a plugin interface for extending or replacing OCR engines. This skill covers the Python API, integration patterns, and the plugin ecosystem.

For CLI usage, see the **ocrmypdf** skill. For batch scripting, see **ocrmypdf-batch**.

## Python API

### Basic usage

```python
import ocrmypdf

# Basic OCR
exit_code = ocrmypdf.ocr('input.pdf', 'output.pdf')

# With options
exit_code = ocrmypdf.ocr(
    'input.pdf',
    'output.pdf',
    language='eng+fra',
    deskew=True,
    rotate_pages=True,
    skip_text=True,
    optimize=2,
    jobs=4,
)
```

### Return codes

```python
import ocrmypdf

result = ocrmypdf.ocr('input.pdf', 'output.pdf')

if result == ocrmypdf.ExitCode.ok:
    print("OCR completed successfully")
elif result == ocrmypdf.ExitCode.already_done_ocr:
    print("PDF already has OCR text")
elif result == ocrmypdf.ExitCode.input_file:
    print("Input file issue")
else:
    print(f"Error: {result}")
```

### Common API parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `language` | str | Tesseract language(s), e.g. `'eng+fra'` |
| `deskew` | bool | Straighten crooked pages |
| `rotate_pages` | bool | Auto-rotate pages |
| `skip_text` | bool | Skip pages that already have text |
| `force_ocr` | bool | Force OCR on all pages |
| `redo_ocr` | bool | Replace existing OCR |
| `optimize` | int | Optimization level (0-3) |
| `output_type` | str | `'pdfa'`, `'pdf'`, `'auto'`, `'none'` |
| `jobs` | int | Number of parallel workers |
| `sidecar` | str | Path for sidecar text file |
| `image_dpi` | int | DPI for image inputs |
| `clean` | bool | Clean pages with unpaper (OCR only) |
| `clean_final` | bool | Clean pages and use in output |
| `remove_background` | bool | Remove noisy backgrounds |
| `oversample` | int | Oversample DPI for low-res images |
| `pages` | str | Page range, e.g. `'1,3,5-10'` |
| `title` | str | Output PDF title |
| `author` | str | Output PDF author |

### Integration example: Flask web service

```python
from flask import Flask, request, send_file
import ocrmypdf
import tempfile
import os

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr_endpoint():
    """OCR a PDF via HTTP POST."""
    if 'file' not in request.files:
        return {'error': 'No file uploaded'}, 400

    uploaded = request.files['file']
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as inp:
        uploaded.save(inp.name)
        out_path = inp.name.replace('.pdf', '_ocr.pdf')

    try:
        result = ocrmypdf.ocr(
            inp.name, out_path,
            language='eng',
            skip_text=True,
            optimize=2,
        )
        if result == ocrmypdf.ExitCode.ok:
            return send_file(out_path, as_attachment=True,
                             download_name='ocr_output.pdf')
        return {'error': f'OCR failed: {result}'}, 500
    finally:
        os.unlink(inp.name)
        if os.path.exists(out_path):
            os.unlink(out_path)

if __name__ == '__main__':
    app.run(port=5000)
```

### Streamlit web UI

OCRmyPDF provides an optional Streamlit-based web UI:

```bash
pip install ocrmypdf[webservice]
# See OCRmyPDF docs for launching the web service
```

## Plugin Ecosystem

OCRmyPDF's plugin interface allows replacing the OCR engine. Available plugins:

### OCRmyPDF-EasyOCR

Replaces Tesseract with [EasyOCR](https://github.com/JaidedAI/EasyOCR) (PyTorch-based). GPU strongly recommended.

```bash
pip install ocrmypdf-easyocr

# Usage
ocrmypdf --plugin ocrmypdf_easyocr -l en input.pdf output.pdf
```

### OCRmyPDF-PaddleOCR

Replaces Tesseract with [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR). Powerful GPU-accelerated engine.

```bash
pip install ocrmypdf-paddleocr

# Usage
ocrmypdf --plugin ocrmypdf_paddleocr input.pdf output.pdf
```

### OCRmyPDF-AppleOCR

Replaces Tesseract with Apple Vision Framework. macOS only.

```bash
pip install ocrmypdf-appleocr

# Usage
ocrmypdf --plugin ocrmypdf_appleocr input.pdf output.pdf
```

### paperless-ngx Integration

[paperless-ngx](https://docs.paperless-ngx.com/) uses OCRmyPDF internally for searchable document management. See paperless-ngx docs for configuration.

## Custom Plugins

Create a custom OCR plugin by implementing the OCRmyPDF plugin interface:

```python
# my_ocr_plugin.py
from ocrmypdf import OcrEngine, hookimpl

class MyOcrEngine(OcrEngine):
    """Custom OCR engine implementation."""

    @staticmethod
    def version():
        return "1.0.0"

    @staticmethod
    def creator_tag(options):
        return "MyOCR"

    def recognize(self, input_file, output_file, output_text, options):
        # Implement OCR logic here
        pass

@hookimpl
def get_ocr_engine():
    return MyOcrEngine()
```

```bash
# Use custom plugin
ocrmypdf --plugin my_ocr_plugin input.pdf output.pdf
```

## Quick Reference

| Task | Code / Command |
|------|----------------|
| Python API basic | `ocrmypdf.ocr('in.pdf', 'out.pdf')` |
| With options | `ocrmypdf.ocr('in.pdf', 'out.pdf', language='eng', deskew=True)` |
| Check result | `if result == ocrmypdf.ExitCode.ok: ...` |
| EasyOCR plugin | `ocrmypdf --plugin ocrmypdf_easyocr in.pdf out.pdf` |
| PaddleOCR plugin | `ocrmypdf --plugin ocrmypdf_paddleocr in.pdf out.pdf` |
| AppleOCR plugin | `ocrmypdf --plugin ocrmypdf_appleocr in.pdf out.pdf` |

## Troubleshooting

- **Import error**: Ensure `pip install ocrmypdf` in your Python environment.
- **Plugin not found**: Check plugin is installed (`pip install ocrmypdf-easyocr`).
- **GPU not used (EasyOCR/PaddleOCR)**: Ensure CUDA/GPU drivers are installed.
- **Memory issues**: Use `jobs=1` for large files; process in batches.

## References

- [OCRmyPDF API Reference](https://ocrmypdf.readthedocs.io/en/latest/api.html)
- [OCRmyPDF Plugin Interface](https://ocrmypdf.readthedocs.io/en/latest/plugins.html)
- [OCRmyPDF-EasyOCR](https://github.com/ocrmypdf/OCRmyPDF-EasyOCR)
- [OCRmyPDF-PaddleOCR](https://github.com/clefru/ocrmypdf-paddleocr)
- [OCRmyPDF-AppleOCR](https://github.com/mkyt/ocrmypdf-AppleOCR)
- [paperless-ngx](https://docs.paperless-ngx.com/)
