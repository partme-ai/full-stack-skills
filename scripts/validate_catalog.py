#!/usr/bin/env python3
"""Validate README package inventory and headline counts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REPOSITORY_RE = re.compile(
    r"^\| \[([^]]+)\]\(https://github\.com/full-stack-skills/([^)]+)\) \| ([0-9]+) \|",
    re.MULTILINE,
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def read_inventory() -> list[str]:
    return [
        line.strip()
        for line in (ROOT / "scripts/repositories.txt").read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def validate_readme(path: Path, expected: set[str]) -> int:
    text = path.read_text(encoding="utf-8")
    rows = REPOSITORY_RE.findall(text)
    repositories = [repository for label, repository, _ in rows if label == repository]
    counts = [int(count) for label, repository, count in rows if label == repository]
    errors = 0

    duplicates = sorted({name for name in repositories if repositories.count(name) > 1})
    missing = sorted(expected - set(repositories))
    unexpected = sorted(set(repositories) - expected)
    for label, values in (("duplicate", duplicates), ("missing", missing), ("unexpected", unexpected)):
        if values:
            fail(f"{path.name}: {label} repositories: {', '.join(values)}")
            errors += 1

    headline = re.search(
        r"\*\*([0-9]+)(?: 个)? Agent Skills[。.]\s*([0-9]+)(?: 个技能包| Skill Packages)",
        text,
    )
    if not headline:
        fail(f"{path.name}: headline counts not found")
        return errors + 1
    declared_skills, declared_packages = map(int, headline.groups())
    if declared_packages != len(expected):
        fail(f"{path.name}: declares {declared_packages} packages, expected {len(expected)}")
        errors += 1
    if declared_skills != sum(counts):
        fail(f"{path.name}: declares {declared_skills} skills, table sums to {sum(counts)}")
        errors += 1

    print(f"{path.name}: {len(repositories)} packages, {sum(counts)} skills")
    return errors


def main() -> int:
    inventory = read_inventory()
    if inventory != sorted(set(inventory)):
        fail("scripts/repositories.txt must be sorted and unique")
        return 1
    expected = set(inventory)
    errors = sum(validate_readme(ROOT / name, expected) for name in ("README.md", "README.en.md"))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
