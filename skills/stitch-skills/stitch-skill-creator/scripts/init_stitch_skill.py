#!/usr/bin/env python3
"""
Stitch Skill Initializer - Creates a new Stitch UI Scenario Skill from the Golden Template.

Usage:
    init_stitch_skill.py <scenario-name> --path <path>

Examples:
    init_stitch_skill.py music-designer --path skills/
    # Creates: skills/stitch-ui-music-designer

    init_stitch_skill.py stitch-ui-blog-designer --path skills/
    # Creates: skills/stitch-ui-blog-designer
"""

import sys
import re
from pathlib import Path
import shutil

# The Golden Template for SKILL.md
STITCH_SKILL_TEMPLATE = """---
name: {skill_name}
description: Specialized prompt architect for {scenario_title} screens.
license: Complete terms in LICENSE.txt
---

# {scenario_title} Screen Designer

**Constraint**: Only use this skill when the user explicitly mentions "Stitch" or when orchestrating a Stitch design task.

This skill helps you construct high-quality prompts for {scenario_title} flows to be used by the Stitch Orchestrator.

## Functionality
It encapsulates best practices for {scenario_title} UI design and translates user intent into a structured Stitch prompt.

## Integration with Stitch Designer SOP
This skill is part of the **Stitch UI Orchestration** flow.
1.  **Orchestrator**: `stitch-ui-designer` calls this skill when a scenario-specific prompt is needed.
2.  **Guidelines**: You MUST apply principles from `stitch-ued-guide` (e.g., visual vocabulary, device constraints).
3.  **Output**: You do NOT execute. You return a prompt only.

## Prompt Template

When the user asks for a {scenario_title} screen, use this template to construct a prompt:

```text
[Context]
[Device] {scenario_title} screen for [App Name]. [Style] aesthetic.

[Layout]
Header: [...]
Body: [...]
Footer: [...]

[Components]
- [...]
- [...]
```

## Output Format (STRICT)

Return exactly one code block and no extra prose:

```text
[Context]
...

[Layout]
...

[Components]
...
```

## Usage in Orchestrator
This skill is designed to be called by `stitch-ui-designer`. It does NOT execute; it returns a prompt only.
"""

# Template for examples/usage.md
USAGE_TEMPLATE = """# Usage Example

## 1. Basic {scenario_title} Screen
**User**: "Design a simple {scenario_lower} page."
**Output**:
```text
[Context]
Mobile {scenario_lower} screen. Clean layout. High-fidelity.

[Layout]
Header: title + back.
Body: main blocks for this scenario.
Footer: primary action.

[Components]
- Primary CTA
- Core widgets for this scenario
```

## 2. Advanced {scenario_title} Flow
**User**: "I need a complex {scenario_lower} interface with [Feature]."
**Output**:
```text
[Context]
Desktop {scenario_lower} interface with [Feature]. High information density.

[Layout]
Left: navigation.
Main: primary content area.
Right/Bottom: secondary panels if needed.

[Components]
- Search/filter
- Data list/grid
- Primary action area
```
"""

def normalize_skill_name(input_name):
    """
    Ensures the skill name starts with 'stitch-ui-' and ends with '-designer' if implied.
    Actually, per SOP, we want 'stitch-ui-<scenario>-designer'.
    Let's be smart but strict.
    """
    name = input_name.lower()
    
    # If user provides "music", make it "stitch-ui-music-designer"
    # If user provides "stitch-ui-music-designer", keep it.
    
    if not name.startswith("stitch-ui-"):
        name = "stitch-ui-" + name
    
    if not name.endswith("-designer"):
        name = name + "-designer"
        
    return name

def extract_scenario_title(skill_name):
    """
    Extracts 'Music' from 'stitch-ui-music-designer'.
    """
    # Remove prefix and suffix
    core = skill_name.replace("stitch-ui-", "").replace("-designer", "")
    # Title case (e.g., "music-player" -> "Music Player")
    return " ".join(word.capitalize() for word in core.split("-"))

def init_skill(input_name, path):
    skill_name = normalize_skill_name(input_name)
    scenario_title = extract_scenario_title(skill_name)
    scenario_lower = scenario_title.lower()
    
    skill_dir = Path(path).resolve() / skill_name

    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return None

    if not re.fullmatch(r"stitch-ui-[a-z0-9]+(?:-[a-z0-9]+)*-designer", skill_name):
        print("❌ Error: Invalid skill name. Expected: stitch-ui-<scenario>-designer (kebab-case).")
        print(f"   Got: {skill_name}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    license_src = Path(__file__).resolve().parents[2] / "stitch-ui-designer" / "LICENSE.txt"
    if license_src.exists():
        try:
            shutil.copyfile(license_src, skill_dir / "LICENSE.txt")
            print("✅ Added LICENSE.txt")
        except Exception as e:
            print(f"❌ Error copying LICENSE.txt: {e}")
            return None

    # Create SKILL.md
    skill_content = STITCH_SKILL_TEMPLATE.format(
        skill_name=skill_name,
        scenario_title=scenario_title
    )
    
    try:
        (skill_dir / 'SKILL.md').write_text(skill_content)
        print("✅ Created SKILL.md with Golden Template")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    # Create examples/usage.md
    try:
        examples_dir = skill_dir / 'examples'
        examples_dir.mkdir(exist_ok=True)
        (examples_dir / 'usage.md').write_text(USAGE_TEMPLATE.format(
            scenario_title=scenario_title,
            scenario_lower=scenario_lower
        ))
        print("✅ Created examples/usage.md")
    except Exception as e:
        print(f"❌ Error creating examples: {e}")
        return None

    print(f"\n✅ Stitch Skill '{skill_name}' initialized successfully!")
    print(f"   Scenario: {scenario_title}")
    print("\nNext steps:")
    print(f"1. Open {skill_dir}/SKILL.md and refine the Prompt Template.")
    print(f"2. Update {skill_dir}/examples/usage.md with real-world examples.")
    
    return skill_dir

def main():
    if len(sys.argv) < 3:
        print("Usage: init_stitch_skill.py <scenario-name> --path <path>")
        sys.exit(1)
        
    # Simple arg parsing
    input_name = sys.argv[1]
    path = "."
    if len(sys.argv) >= 4 and sys.argv[2] == "--path":
        path = sys.argv[3]
        
    init_skill(input_name, path)

if __name__ == "__main__":
    main()
