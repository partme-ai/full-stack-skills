#!/usr/bin/env python3
"""
Build an Awesome Agent Skills markdown index from a skills root directory.

This script is stdlib-only and designed for agentic use (non-interactive).
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple


@dataclass
class Entry:
    path: str
    name: str
    description: str


def parse_args() -> argparse.Namespace:
    """Parse CLI args."""
    p = argparse.ArgumentParser(
        prog="build_awesome.py",
        description="Generate an AWESOME_AGENT_SKILLS.md index for a skills repository.",
    )
    p.add_argument("--skills-root", required=True, help="Path to the skills root (contains skill groups).")
    p.add_argument("--output", required=True, help="Output markdown file path.")
    p.add_argument("--max", type=int, default=5000, help="Max skills to include (safety).")
    return p.parse_args()


def read_text(path: Path) -> str:
    """Read UTF-8 text from file."""
    return path.read_text(encoding="utf-8")


def parse_frontmatter(skill_md: str) -> Dict[str, str]:
    """Parse minimal frontmatter (name/description/license) without YAML deps."""
    lines = skill_md.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fm: Dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm


def find_skill_dirs(skills_root: Path, limit: int) -> List[Path]:
    """Discover skill directories by locating SKILL.md under the skills root."""
    skill_dirs: List[Path] = []
    for p in skills_root.rglob("SKILL.md"):
        d = p.parent
        if d in skill_dirs:
            continue
        skill_dirs.append(d)
        if len(skill_dirs) >= limit:
            break
    return sorted(skill_dirs)


def load_entries(skills_root: Path, limit: int) -> List[Entry]:
    """Load skill entries from SKILL.md files."""
    entries: List[Entry] = []
    for d in find_skill_dirs(skills_root, limit):
        fm = parse_frontmatter(read_text(d / "SKILL.md"))
        name = fm.get("name", d.name)
        desc = fm.get("description", "")
        if desc.strip().upper().startswith("DEPRECATED"):
            continue
        rel = str(d.relative_to(skills_root.parent))
        entries.append(Entry(path=rel, name=name, description=desc))
    return entries


def group_key(entry: Entry) -> str:
    """Group key for awesome output."""
    p = Path(entry.path)
    parts = p.parts
    if len(parts) >= 2:
        return parts[-2]
    return "skills"


def render(entries: List[Entry]) -> str:
    """Render markdown content."""
    lines: List[str] = []
    lines.append("# Awesome Agent Skills")
    lines.append("")
    lines.append(f"_Generated at {datetime.now(timezone.utc).isoformat().replace('+00:00','Z')}_")
    lines.append("")

    groups: Dict[str, List[Entry]] = {}
    for e in entries:
        groups.setdefault(group_key(e), []).append(e)

    for g in sorted(groups.keys()):
        lines.append(f"## {g}")
        for e in sorted(groups[g], key=lambda x: x.name):
            one = e.description.strip().replace("\n", " ")
            if len(one) > 140:
                one = one[:137] + "..."
            lines.append(f"- [{e.name}]({e.path}) — {one}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    """CLI entrypoint."""
    args = parse_args()
    skills_root = Path(args.skills_root).expanduser().resolve()
    out_path = Path(args.output).expanduser().resolve()

    entries = load_entries(skills_root, args.max)
    content = render(entries)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
