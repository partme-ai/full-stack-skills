#!/usr/bin/env python3
"""
Pencil Design System Skill Initializer - Creates a new pencil-ui-design-system-* skill from the Golden Template.

Usage:
    init_pencil_design_system_skill.py <name> --path <path>

Examples:
    init_pencil_design_system_skill.py layui --path skills/
    # Creates: skills/pencil-ui-design-system-layui

    init_pencil_design_system_skill.py uviewpro --path skills/
    # Creates: skills/pencil-ui-design-system-uviewpro
"""

import sys
import re
from pathlib import Path
import shutil

# Golden Template for SKILL.md (pencil-ui-design-system-*)
PENCIL_SKILL_TEMPLATE = """---
name: {skill_name}
description: Initialize {design_system_title}: design system components in Pencil (variables + component overview).
license: Complete terms in LICENSE.txt
---

# {design_system_title} Design System Initializer

**Constraint**: Only use this skill when the user explicitly mentions "Pencil" and "{design_system_title}" or when orchestrating a Pencil design system initialization task.

## When to use this skill

Use this skill when you need to initialize a new design system based on {design_system_title} specifications, specifically to set up the global color palette (and typography/radius) and create the initial component library frames in a .pen file.

## How to use this skill

This skill outputs a PENCIL_PLAN. The Agent then calls Pencil MCP tools in order: `open_document`, `set_variables`, `batch_design`, optionally `get_screenshot`.

### Step 1: Initialize Variables (set_variables)

Use `mcp__pencil__set_variables` to register the following {design_system_title} design tokens. Follow .pen file schema; variable names are arbitrary strings (no leading $ required).

| Variable | Value | Notes |
|----------|--------|--------|
| (Fill from official docs) | | Primary, error, warning, success, info, text, bg, border, font sizes, radius |

**Example (placeholder):**
- `primary`: `#1890ff`
- `primary-dark`: `#096dd9`
- `font-md`: `14px`
- `radius`: `4px`

### Step 2: Create Component Overview Structure (batch_design)

Use `mcp__pencil__batch_design` to create a "Components Overview" frame containing the following sections (Frames) based on {design_system_title} documentation:

1. **Basic Components**
   - (List component names from official docs)
2. **Form Components**
   - (List component names)
3. **Data / Feedback / Layout / Navigation / Other**
   - (List component names per category)

Organize component frames using Auto Layout for easy expansion. Keep each `batch_design` call to maximum 25 operations; split by logical sections if needed.

## Best Practices

- Always verify color and token values against the latest {design_system_title} documentation if unsure.
- Use `set_variables` with `replace: false` to merge into existing variables unless a full reset is requested.
- Organize component frames using Auto Layout for easy expansion.

## Keywords

pencil, {design_system_slug}, design system, init, variables, components

## References

- `references/contract.md` – Design tokens and component naming.
- `references/official.md` – Link to official documentation.
- `references/examples.md` – Example PENCIL_PLAN or usage.
"""

# Placeholder for references/contract.md
CONTRACT_PLACEHOLDER = """# Contract: {design_system_title} Design Tokens and Components

Fill from official documentation:

- Design tokens (colors, typography, radius)
- Component prefix / naming (e.g. up-, u-)
- Component list by category
"""

# Placeholder for references/official.md
OFFICIAL_PLACEHOLDER = """# Official Documentation

- Link to {design_system_title} official docs
- Design tokens / theme section
- Component list
"""

# Placeholder for references/examples.md
EXAMPLES_PLACEHOLDER = """# Examples

## PENCIL_PLAN example

Step 1: set_variables(variables: {{ ... }})
Step 2: batch_design(operations: "root=I(document, {{ type: 'frame', layout: 'vertical', name: 'Components Overview' }}) ...")
Step 3: get_screenshot(nodeId: <root-id>)
"""


def normalize_skill_name(input_name: str) -> str:
    """Ensures the skill name is pencil-ui-design-system-<name> (kebab-case)."""
    name = input_name.lower().strip()
    # Remove prefix if user passed full name
    if name.startswith("pencil-ui-design-system-"):
        name = name.replace("pencil-ui-design-system-", "", 1)
    # Kebab-case: replace spaces/underscores with hyphens
    name = re.sub(r"[\\s_]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return "pencil-ui-design-system-" + name if name else "pencil-ui-design-system-unknown"


def extract_design_system_title(skill_name: str) -> str:
    """Extracts display title from skill name, e.g. 'uview-pro' -> 'uView Pro'."""
    core = skill_name.replace("pencil-ui-design-system-", "")
    return " ".join(word.capitalize() for word in core.split("-"))


def init_skill(input_name: str, path: str):
    skill_name = normalize_skill_name(input_name)
    design_system_title = extract_design_system_title(skill_name)
    design_system_slug = skill_name.replace("pencil-ui-design-system-", "")

    skill_dir = Path(path).resolve() / skill_name

    if skill_dir.exists():
        print(f"Error: Skill directory already exists: {skill_dir}")
        return None

    if not re.fullmatch(r"pencil-ui-design-system-[a-z0-9]+(?:-[a-z0-9]+)*", skill_name):
        print("Error: Invalid skill name. Expected: pencil-ui-design-system-<name> (kebab-case).")
        print(f"   Got: {skill_name}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"Error creating directory: {e}")
        return None

    # Copy LICENSE from an existing skill in the same repo
    script_dir = Path(__file__).resolve().parent
    skills_parent = script_dir.parents[1]
    license_src = skills_parent / "pencil-ui-design-system-uviewpro" / "LICENSE.txt"
    if not license_src.exists():
        license_src = skills_parent / "pencil-mcp-batch-design" / "LICENSE.txt"
    if license_src.exists():
        try:
            shutil.copyfile(license_src, skill_dir / "LICENSE.txt")
            print("Added LICENSE.txt")
        except Exception as e:
            print(f"Error copying LICENSE.txt: {e}")
    else:
        (skill_dir / "LICENSE.txt").write_text("Apache License 2.0 (See root LICENSE)\n")
        print("Added LICENSE.txt (placeholder)")

    # Create SKILL.md
    skill_content = PENCIL_SKILL_TEMPLATE.format(
        skill_name=skill_name,
        design_system_title=design_system_title,
        design_system_slug=design_system_slug,
    )
    try:
        (skill_dir / "SKILL.md").write_text(skill_content)
        print("Created SKILL.md with Golden Template")
    except Exception as e:
        print(f"Error creating SKILL.md: {e}")
        return None

    # Create references/
    ref_dir = skill_dir / "references"
    ref_dir.mkdir(exist_ok=True)
    for filename, content_tpl in [
        ("contract.md", CONTRACT_PLACEHOLDER),
        ("official.md", OFFICIAL_PLACEHOLDER),
        ("examples.md", EXAMPLES_PLACEHOLDER),
    ]:
        content = content_tpl.format(design_system_title=design_system_title)
        (ref_dir / filename).write_text(content)
    print("Created references/contract.md, official.md, examples.md")

    print(f"\nPencil Design System Skill '{skill_name}' initialized successfully!")
    print(f"   Design system: {design_system_title}")
    print("\nNext steps:")
    print(f"1. Open {skill_dir}/SKILL.md and fill Step 1 Variables and Step 2 Component overview from official docs.")
    print(f"2. Update {skill_dir}/references/contract.md, official.md, examples.md.")

    return skill_dir


def main():
    if len(sys.argv) < 3:
        print("Usage: init_pencil_design_system_skill.py <name> --path <path>")
        sys.exit(1)

    input_name = sys.argv[1]
    path = "."
    if len(sys.argv) >= 4 and sys.argv[2] == "--path":
        path = sys.argv[3]

    init_skill(input_name, path)


if __name__ == "__main__":
    main()
