---
name: brand-guidelines
description: "Applies Anthropic brand colors (dark #141413, orange #d97757, blue #6a9bcc, green #788c5d), Poppins headings, and Lora body text to artifacts such as presentations, documents, or visuals. Use when the user needs Anthropic brand styling, brand color application, corporate typography, or visual formatting following Anthropic design standards."
license: Complete terms in LICENSE.txt
---

# Anthropic Brand Styling

## When to use this skill

Use this skill when:
- The user needs to apply Anthropic brand colors and typography to any artifact
- The user asks about Anthropic's official color palette, fonts, or visual identity
- An artifact (presentation, document, visual) needs Anthropic's look-and-feel
- The user mentions brand guidelines, corporate styling, or Anthropic visual standards

## Brand Guidelines

### Colors

**Main Colors:**

- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**

- Orange: `#d97757` - Primary accent
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography

- **Headings**: Poppins (with Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- **Note**: Fonts should be pre-installed in your environment for best results

## Features

### Smart Font Application

- Applies Poppins font to headings (24pt and larger)
- Applies Lora font to body text
- Automatically falls back to Arial/Georgia if custom fonts unavailable
- Preserves readability across all systems

### Text Styling

- Headings (24pt+): Poppins font
- Body text: Lora font
- Smart color selection based on background
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use accent colors
- Cycles through orange, blue, and green accents
- Maintains visual interest while staying on-brand

## Technical Details

### Font Management

- Uses system-installed Poppins and Lora fonts when available
- Provides automatic fallback to Arial (headings) and Georgia (body)
- No font installation required - works with existing system fonts
- For best results, pre-install Poppins and Lora fonts in your environment

### Color Application

- Uses RGB color values for precise brand matching
- Applied via python-pptx's RGBColor class
- Maintains color fidelity across different systems

## Workflow

1. **Identify the artifact** to style (presentation, document, HTML, image).
2. **Apply colors**: Use main colors for backgrounds and text; accent colors for highlights and shapes.
3. **Apply typography**: Poppins for headings (24pt+), Lora for body text.
4. **Verify contrast**: Ensure dark text on light backgrounds and light text on dark backgrounds.

```python
# Example: Apply brand colors to a PowerPoint slide
from pptx.util import Pt
from pptx.dml.color import RGBColor

# Anthropic brand colors
DARK = RGBColor(0x14, 0x14, 0x13)
LIGHT = RGBColor(0xFA, 0xF9, 0xF5)
ORANGE = RGBColor(0xD9, 0x77, 0x57)
```

## Keywords

branding, corporate identity, visual identity, brand colors, typography, Anthropic brand, Poppins, Lora
