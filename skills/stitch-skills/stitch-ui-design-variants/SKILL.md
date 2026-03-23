---
name: stitch-ui-design-variants
description: Logic skill that generates prompts for alternative design variants e.g. A B testing options.
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
---


# Stitch Design Variants

This skill acts as a **Variant Generator**. It takes a base design and produces alternative prompts to explore different creative directions.

## Input
*   **Base Spec**: The original Design Spec or Prompt.
*   **Variant Type**:
    *   `LAYOUT`: Keep style, change structure.
    *   `STYLE`: Keep structure, change theme/colors.
    *   `CONTENT`: Keep design, change text/data.

## Output Format (List of Strings)
A list of 3 distinct prompts.

## Logic Rules

### 1. Layout Variants
*   *Variant A*: Standard layout.
*   *Variant B*: Split screen or asymmetrical layout.
*   *Variant C*: Minimalist/Hidden navigation layout.

### 2. Style Variants
*   *Variant A*: Original Theme.
*   *Variant B*: Inverted Theme (Light <-> Dark).
*   *Variant C*: High Contrast / Monochromatic.

## Usage Example
**User**: "Give me 3 style options for this dashboard."
**Output**:
1.  "Desktop Dashboard... **Dark Mode**... Blue accents..."
2.  "Desktop Dashboard... **Light Mode**... Clean white/grey..."
3.  "Desktop Dashboard... **High Contrast**... Black and White..."

## References

- [Examples](examples/usage.md)
