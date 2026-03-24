#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
# tui-skills 已迁移至 t2ui-skills 仓库；若工作区存在同级 t2ui-skills 则对其 skills 目录做检查
TUI_SKILLS_DIR = ROOT.parent / "t2ui-skills" / "skills"


def iter_target_files() -> list[Path]:
    targets: list[Path] = []
    if not TUI_SKILLS_DIR.exists():
        return targets
    for p in TUI_SKILLS_DIR.iterdir():
        if not p.is_dir():
            continue
        if p.name.startswith("tui-"):
            for f in p.rglob("*"):
                if f.is_file():
                    targets.append(f)
    return targets


def main() -> int:
    needle = "uviewpro"
    offenders: list[tuple[Path, int, str]] = []

    for f in iter_target_files():
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if needle not in text:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            if needle in line:
                offenders.append((f, i, line.strip()))

    if offenders:
        print(f"FAIL: found '{needle}' in {len(offenders)} location(s):")
        for f, i, line in offenders[:200]:
            print(f"- {f}:{i}: {line}")
        return 1

    print(f"OK: no '{needle}' found in TUI skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
