---
name: stitch-ui-design-variants
description: "Generate alternative Stitch design variant prompts for A/B testing and creative exploration. Use when the user wants multiple style, layout, or content options for a Stitch screen. Takes a base Design Spec or prompt and produces 3 distinct variants (layout, style, or content variations)."
allowed-tools: "stitch*:*, Read, Write"
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

## Validation

Ensure each variant is **sufficiently distinct**: different layout structure (for LAYOUT), different color palette (for STYLE), or different content/copy (for CONTENT). If two variants look too similar, regenerate the weaker one.

## Example: Style Variants for a Dashboard

**Input**: "Desktop SaaS dashboard. Dark mode. Blue primary (#2563EB). Sidebar nav."

**Output**:

1. "Desktop SaaS dashboard. Dark mode with deep navy background (#0f172a). Primary blue (#2563EB) for CTAs. Sidebar navigation. Cards with subtle border glow. High-contrast text (#f8fafc)."
2. "Desktop SaaS dashboard. Light mode with clean white background (#ffffff). Primary blue (#2563EB) for CTAs. Sidebar navigation. Cards with soft gray (#f1f5f9) backgrounds and subtle shadows."
3. "Desktop SaaS dashboard. High-contrast monochrome with pure black background (#000000). Accent electric blue (#3b82f6) for active states only. Sidebar navigation. Minimal chrome, maximum data density."

## References

- [Examples](examples/usage.md)
