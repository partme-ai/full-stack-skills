#!/usr/bin/env python3
"""
Evaluate an Agent Skill against “official” Agent Skills conventions and output a report.

This script is intentionally dependency-free (stdlib only) to keep it portable.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


FRONTMATTER_BOUNDARY = re.compile(r"^---\s*$")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SECRET_RE = re.compile(
    r"(AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{16,}|(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]+['\"])",
    re.IGNORECASE,
)


@dataclass
class CheckResult:
    item: str
    result: str
    evidence: str
    suggestion: str


def parse_args() -> argparse.Namespace:
    """Parse CLI args."""
    p = argparse.ArgumentParser(
        prog="official_evaluate.py",
        description="Evaluate a skill directory and output an official-style report.",
    )
    p.add_argument("--skill-dir", required=True, help="Path to the target skill directory.")
    p.add_argument("--format", choices=["md", "json"], default="md", help="Output format.")
    p.add_argument("--output", default="", help="Write output to a file instead of stdout.")
    return p.parse_args()


def read_text(path: Path) -> str:
    """Read UTF-8 text from file."""
    return path.read_text(encoding="utf-8")


def parse_frontmatter(skill_md: str) -> Tuple[Dict[str, Any], str]:
    """Parse YAML-like frontmatter from SKILL.md without external YAML deps."""
    lines = skill_md.splitlines()
    if not lines or not FRONTMATTER_BOUNDARY.match(lines[0]):
        return {}, skill_md

    i = 1
    fm_lines: List[str] = []
    while i < len(lines) and not FRONTMATTER_BOUNDARY.match(lines[i]):
        fm_lines.append(lines[i])
        i += 1

    if i >= len(lines):
        return {}, skill_md

    body = "\n".join(lines[i + 1 :]).lstrip("\n")
    fm: Dict[str, Any] = {}
    for raw in fm_lines:
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        if ":" not in raw:
            continue
        k, v = raw.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm, body


def short(s: str, limit: int = 120) -> str:
    """Shorten long strings for evidence rendering."""
    s = " ".join(s.split())
    if len(s) <= limit:
        return s
    return s[: limit - 3] + "..."


def check_name(dir_name: str, fm: Dict[str, Any]) -> CheckResult:
    """Check name format and directory match."""
    name = (fm.get("name") or "").strip()
    if not name:
        return CheckResult("Frontmatter name present", "Fail", "Missing frontmatter name", "Add name and match directory name")
    if name != dir_name:
        return CheckResult("Name matches directory", "Fail", f"name={name}, dir={dir_name}", "Make name match directory name")
    if not NAME_RE.match(name) or len(name) > 64:
        return CheckResult("Name format valid", "Fail", f"name={name}", "Use lowercase letters/numbers/hyphens; length 1-64")
    if "--" in name or name.startswith("-") or name.endswith("-"):
        return CheckResult("Hyphen rules", "Fail", f"name={name}", "Avoid consecutive hyphens; do not start/end with hyphen")
    return CheckResult("Name matches directory", "Pass", f"name={name}", "-")


def check_description(fm: Dict[str, Any]) -> CheckResult:
    """Check description presence and basic quality."""
    desc = (fm.get("description") or "").strip()
    if not desc:
        return CheckResult("Frontmatter description present", "Fail", "Missing frontmatter description", "Add description (what + when)")
    if len(desc) > 1024:
        return CheckResult("Description length", "Fail", f"len={len(desc)}", "Reduce to 1-1024 characters")
    if len(desc) < 20:
        return CheckResult("Description informativeness", "Needs improvement", short(desc), "Add triggers and user-intent phrasing")
    return CheckResult("Description valid", "Pass", short(desc), "-")


def check_license(skill_dir: Path, fm: Dict[str, Any]) -> CheckResult:
    """Check license field and file existence when referenced."""
    lic = (fm.get("license") or "").strip()
    if not lic:
        return CheckResult("License field", "Needs improvement", "No frontmatter license", "Add license field or reference LICENSE.txt")
    if "LICENSE" in lic and not (skill_dir / "LICENSE.txt").exists():
        return CheckResult("LICENSE.txt present", "Fail", f"license={lic}", "Add LICENSE.txt or fix the license reference")
    return CheckResult("License basic check", "Pass", short(lic), "-")


def scan_for_secrets(skill_dir: Path) -> List[str]:
    """Scan common text files for likely secrets."""
    findings: List[str] = []
    for p in skill_dir.rglob("*"):
        if p.is_dir():
            continue
        if p.suffix.lower() not in {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".sh"}:
            continue
        try:
            text = read_text(p)
        except Exception:
            continue
        m = SECRET_RE.search(text)
        if m:
            findings.append(f"{p.relative_to(skill_dir)}: {short(m.group(0), 80)}")
    return findings


def detect_noninteractive_issues(skill_dir: Path) -> List[str]:
    """Heuristically detect interactive patterns in scripts."""
    issues: List[str] = []
    scripts_dir = skill_dir / "scripts"
    if not scripts_dir.exists():
        return issues
    for p in scripts_dir.rglob("*"):
        if p.is_dir():
            continue
        if p.suffix.lower() not in {".py", ".sh"}:
            continue
        try:
            text = read_text(p)
        except Exception:
            continue
        if "input(" in text or "read -p" in text or "select " in text:
            issues.append(f"{p.relative_to(skill_dir)}: may require interactive input")
    return issues


def evaluate(skill_dir: Path) -> Dict[str, Any]:
    """Run checks and return a structured report object."""
    skill_md_path = skill_dir / "SKILL.md"
    if not skill_md_path.exists():
        return {
            "error": "SKILL.md not found",
            "skill_dir": str(skill_dir),
        }

    raw = read_text(skill_md_path)
    fm, _body = parse_frontmatter(raw)
    dir_name = skill_dir.name

    checks: List[CheckResult] = []
    checks.append(CheckResult("SKILL.md present", "Pass", "SKILL.md", "-"))
    checks.append(check_name(dir_name, fm))
    checks.append(check_description(fm))
    checks.append(check_license(skill_dir, fm))

    refs = (skill_dir / "references").exists()
    scripts = (skill_dir / "scripts").exists()
    assets = (skill_dir / "assets").exists()
    checks.append(
        CheckResult(
            "Optional directories",
            "Pass",
            f"references={refs}, scripts={scripts}, assets={assets}",
            "-",
        )
    )

    secret_findings = scan_for_secrets(skill_dir)
    if secret_findings:
        checks.append(
            CheckResult(
                "Secrets scan",
                "Fail",
                "; ".join(secret_findings[:3]) + (" ..." if len(secret_findings) > 3 else ""),
                "Remove secrets; use environment variables or secure storage",
            )
        )
    else:
        checks.append(CheckResult("Secrets scan", "Pass", "No high-confidence secret patterns detected", "-"))

    interactive_issues = detect_noninteractive_issues(skill_dir)
    if interactive_issues:
        checks.append(
            CheckResult(
                "Non-interactive scripts",
                "Needs improvement",
                "; ".join(interactive_issues[:3]) + (" ..." if len(interactive_issues) > 3 else ""),
                "Avoid interactive input; use CLI flags instead of stdin/TTY prompts",
            )
        )
    else:
        checks.append(CheckResult("Non-interactive scripts", "Pass", "No obvious interactive patterns detected", "-"))

    overall = "通过"
    top: List[str] = []
    for c in checks:
        if c.result == "Fail":
            overall = "需改进"
            top.append(c.item)
        elif c.result == "Needs improvement" and overall != "需改进":
            overall = "通过（有改进空间）"
            top.append(c.item)

    return {
        "skill_dir": str(skill_dir),
        "skill_name": fm.get("name", ""),
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "overall": overall,
        "top_issues": top[:3],
        "checks": [c.__dict__ for c in checks],
    }


def to_markdown(report: Dict[str, Any]) -> str:
    """Render report as Markdown."""
    if "error" in report:
        return (
            "# Official Skill Evaluation Report\n\n"
            f"- Error: {report['error']}\n"
            f"- Path: {report.get('skill_dir','')}\n"
        )

    lines: List[str] = []
    lines.append("# Official Skill Evaluation Report")
    lines.append("")
    lines.append(f"Target: `{report.get('skill_dir','')}`")
    lines.append("")
    lines.append("## Conclusion")
    lines.append(f"- Overall: {report.get('overall','')}")
    top = report.get("top_issues") or []
    if top:
        lines.append("- Top issues:")
        for i, t in enumerate(top, 1):
            lines.append(f"  {i}. {t}")
    else:
        lines.append("- Top issues: none")
    lines.append("")
    lines.append("## Checklist")
    lines.append("| Item | Result | Evidence | Suggestion |")
    lines.append("| --- | --- | --- | --- |")
    for c in report.get("checks", []):
        lines.append(f"| {c['item']} | {c['result']} | {c['evidence']} | {c['suggestion']} |")
    lines.append("")
    lines.append("## Risks & Limits")
    lines.append("- Static evaluation only. It does not validate runtime behavior (e.g., network calls, sandbox behavior).")
    lines.append("- For stronger trust conclusions, provide third-party scan reports or runtime logs.")
    lines.append("")
    lines.append("## Recommendations")
    recs: List[str] = []
    for c in report.get("checks", []):
        if c["result"] in {"Fail", "Needs improvement"} and c["suggestion"] != "-":
            recs.append(f"- {c['item']}: {c['suggestion']}")
    if not recs:
        lines.append("- None")
    else:
        lines.extend(recs[:10])
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    """CLI entrypoint."""
    args = parse_args()
    skill_dir = Path(args.skill_dir).expanduser().resolve()
    report = evaluate(skill_dir)

    if args.format == "json":
        out = json.dumps(report, ensure_ascii=False, indent=2)
    else:
        out = to_markdown(report)

    if args.output:
        out_path = Path(args.output).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out, encoding="utf-8")
        return 0

    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

