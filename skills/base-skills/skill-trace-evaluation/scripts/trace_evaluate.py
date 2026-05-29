#!/usr/bin/env python3
"""
Hybrid TRACE evaluator: static base score + evidence packet.

This script computes a deterministic base score for each TRACE sub-item from
measurable evidence fields. The AI (loaded with skill-trace-evaluation SKILL.md)
then applies a semantic adjustment (±0.3) based on reading the SKILL.md body.

Final score per sub-item = clamp(base + adjustment, 1.0, 5.0).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


FRONTMATTER_BOUNDARY = re.compile(r"^---\s*$")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SECRET_RE = re.compile(
    r"(AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{16,}|"
    r"(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]+['\"])",
    re.IGNORECASE,
)

SECURITY_DECLARATION_RE = re.compile(
    r'(?:does not (?:access|collect|upload|send|transmit|share|leak|store|log)'
    r'|no (?:sensitive|secret|credential|api.key|token|password)'
    r'|不(?:访问|收集|上传|发送|传输|共享|泄露|存储|记录)'
    r'|无(?:敏感|密钥|凭据|API|token|密码)'
    r'|最小权限|least.privilege'
    r'|安全|security.safe)',
    re.IGNORECASE,
)

CLI_SECTION_RE = re.compile(
    r'(?:^|\n)\s*(?:###?\s+)?(?:Prerequisites|Install(?:ation)?|Setup'
    r'|Configuration|Usage|Quick\s*Start|Getting\s*Started'
    r'|Environment\s*(?:Setup|Variables)|Authentication|Login'
    r'|基本用法|使用方式|安装|配置|环境|登录|前置条件)',
    re.IGNORECASE,
)

WORKFLOW_STEP_RE = re.compile(r'(?:^|\n)\s*(?:###?\s+)?Step\s+\d', re.MULTILINE)


@dataclass
class SubItemScore:
    base: float
    formula: str
    evidence: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DimScores:
    label: str
    sub_items: Dict[str, SubItemScore] = field(default_factory=dict)

    @property
    def avg(self) -> float:
        if not self.sub_items:
            return 0.0
        return round(sum(s.base for s in self.sub_items.values()) / len(self.sub_items), 1)


@dataclass
class EvidencePacket:
    skill_dir: str
    skill_name: str
    generated_at: str
    frontmatter: Dict[str, Any] = field(default_factory=dict)
    body: Dict[str, Any] = field(default_factory=dict)
    directory: Dict[str, Any] = field(default_factory=dict)
    safety: Dict[str, Any] = field(default_factory=dict)
    base_scores: Dict[str, Any] = field(default_factory=dict)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="trace_evaluate.py",
        description="Hybrid TRACE evaluator: static base score + evidence packet for AI adjustment.",
    )
    p.add_argument("--skill-dir", required=True, help="Path to the target skill directory.")
    p.add_argument("--format", choices=["json", "pretty"], default="json", help="Output format.")
    p.add_argument("--output", default="", help="Write output to a file instead of stdout.")
    return p.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has_chinese(text: str) -> bool:
    return bool(re.search(r'[\u4e00-\u9fff]', text))


def count_files(dir_path: Path) -> int:
    if not dir_path.exists():
        return 0
    return sum(1 for p in dir_path.rglob("*") if p.is_file())


def count_subdirs(dir_path: Path) -> int:
    if not dir_path.exists():
        return 0
    return sum(1 for p in dir_path.iterdir() if p.is_dir())


def list_ref_names(dir_path: Path) -> List[str]:
    if not dir_path.exists():
        return []
    return sorted([p.name for p in dir_path.rglob("*") if p.is_file()])


def parse_frontmatter(skill_md: str) -> Tuple[Dict[str, Any], str]:
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


def collect_facts(skill_dir: Path) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], str]:
    """Collect all raw facts from the skill directory."""
    skill_md_path = skill_dir / "SKILL.md"
    if not skill_md_path.exists():
        return {}, {}, {}, {}, ""

    raw = read_text(skill_md_path)
    fm, body = parse_frontmatter(raw)

    frontmatter = {
        "name": (fm.get("name") or "").strip(),
        "name_valid": bool(fm.get("name") and NAME_RE.match(fm["name"].strip())),
        "name_matches_dir": (fm.get("name") or "").strip() == skill_dir.name,
        "description": (fm.get("description") or "").strip()[:200],
        "description_length": len((fm.get("description") or "").strip()),
        "description_valid": 1 <= len((fm.get("description") or "").strip()) <= 1024,
        "license": (fm.get("license") or "").strip(),
    }

    body_lower = body.lower()
    body_facts = {
        "body_lines": len(body.splitlines()),
        "body_chars": len(body),
        "has_chinese": has_chinese(body),
        "has_workflow_steps": bool(WORKFLOW_STEP_RE.search(body)),
        "step_count": len(WORKFLOW_STEP_RE.findall(body)),
        "has_rules_section": bool(
            "## rules" in body_lower
            or "## writing rules" in body_lower
            or re.search(r'(?:^|\n)##\s+.*[Rr]ules', body) is not None
        ),
        "has_gotchas_section": "## gotchas" in body_lower,
        "has_validation": bool(
            re.search(r'(?:validation|校验|自检|checklist|verify|验证)', body_lower)
        ),
        "has_boundary": bool(
            "不该用" in body or "不适用" in body
            or "should not" in body.lower()
            or "not use" in body.lower()
            or "do not use" in body.lower()
        ),
        "has_when_to_use": bool("什么时候" in body or "When to" in body),
        "has_trigger_hints": bool(re.search(
            r'(?:加载|load|when to read|read.*if|打开.+文件|参考.*文件)', body_lower
        )),
        "has_security_declaration": bool(SECURITY_DECLARATION_RE.search(body)),
        "cli_sections_count": len(CLI_SECTION_RE.findall(body)),
        "bash_blocks_count": len(re.findall(r'```(?:bash|shell|sh|zsh)', body)),
        "tool_reference_count": len(re.findall(
            r'(?:dreamina|uvx|npx|pipx|bunx|deno\s+run|go\s+run|curl|wget)\b',
            body, re.IGNORECASE
        )),
        "prompt_keyword_count": len(re.findall(
            r'(?:提示词|prompt|word-library|vocabulary|场景|scenario|category|模板|template)',
            body, re.IGNORECASE
        )),
        "gotchas_count": len(re.findall(
            r'(?:^|\n)\d+\.\s+\*\*', body
        )) + len(re.findall(r'(?:^|\n)\d+\.\s', body)),
    }

    cli_score = body_facts["bash_blocks_count"] + body_facts["tool_reference_count"]
    if cli_score >= 3:
        body_facts["skill_type"] = "cli"
    elif body_facts["prompt_keyword_count"] >= 8:
        body_facts["skill_type"] = "prompt"
    else:
        body_facts["skill_type"] = "doc"

    directory = {
        "has_scripts": (skill_dir / "scripts").exists(),
        "scripts_files": count_files(skill_dir / "scripts"),
        "has_references": (skill_dir / "references").exists(),
        "references_files": count_files(skill_dir / "references"),
        "references_subdirs": count_subdirs(skill_dir / "references"),
        "has_examples": (skill_dir / "examples").exists(),
        "examples_files": count_files(skill_dir / "examples"),
        "has_license_file": (skill_dir / "LICENSE.txt").exists(),
        "ref_names": list_ref_names(skill_dir / "references"),
    }

    safety = {
        "secrets_detected": False,
        "secret_findings": [],
        "has_interactive_patterns": [],
    }
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
            safety["secrets_detected"] = True
            safety["secret_findings"].append(f"{p.relative_to(skill_dir)}: {m.group(0)[:60]}")
        if "input(" in text or "read -p" in text:
            safety["has_interactive_patterns"].append(
                f"{p.relative_to(skill_dir)}: may require interactive input"
            )

    return frontmatter, body_facts, directory, safety, body


# ══════════════════════════════════════════════════════════════════
#  Base score formulas — one function per sub-item.
#  Each returns a SubItemScore with base in [1.0, 5.0] and the
#  formula string explaining how the score was computed.
# ══════════════════════════════════════════════════════════════════


def _clamp(v: float) -> float:
    return round(max(1.0, min(5.0, v)), 1)


# ── T · Trust ──

def score_T1(fm, body, directory, safety) -> SubItemScore:
    s = safety["secrets_detected"]
    ss = safety.get("secret_findings", [])
    hs = directory["has_scripts"]
    sd = body["has_security_declaration"]
    base = 4.5
    if s:
        base = max(2.0, 3.5 - 0.5 * len(ss))
    else:
        base = 4.5
    if not hs:
        base += 0.3
    else:
        base -= 0.3
    if sd:
        base += 0.2
    return SubItemScore(
        base=_clamp(base),
        formula=f"4.5 + (no_scripts:{not hs} ? +0.3 : -0.3) + (secdecl:{sd} ? +0.2 : 0) - (secrets_detected:{s} ? -1.0 : 0)",
        evidence={"secrets_detected": s, "has_scripts": hs, "has_security_declaration": sd},
    )


def score_T2(fm, body, directory, safety) -> SubItemScore:
    hc = body["has_chinese"]
    bl = body["body_lines"]
    base = 5.0 if hc else 2.0
    return SubItemScore(
        base=_clamp(base),
        formula=f"has_chinese={hc} → {base}",
        evidence={"has_chinese": hc},
    )


def score_T3(fm, body, directory, safety) -> SubItemScore:
    hb = body["has_boundary"]
    hw = body["has_when_to_use"]
    base = 4.5 if hb else 3.0
    if hb and hw:
        base += 0.3
    return SubItemScore(
        base=_clamp(base),
        formula=f"boundary={hb}(+0.3) + when_to_use={hw}(+0.3) off 4.5 base → {base}",
        evidence={"has_boundary": hb, "has_when_to_use": hw},
    )


def score_T4(fm, body, directory, safety) -> SubItemScore:
    hs = directory["has_scripts"]
    sd = body["has_security_declaration"]
    base = 4.5
    if sd:
        base += 0.5
    if hs:
        base -= 0.2
    return SubItemScore(
        base=_clamp(base),
        formula=f"4.5 + (secdecl:{sd} ? +0.5 : 0) - (has_scripts:{hs} ? -0.2 : 0)",
        evidence={"has_security_declaration": sd, "has_scripts": hs},
    )


# ── R · Reliability ──

def score_R1(fm, body, directory, safety) -> SubItemScore:
    hg = body["has_gotchas_section"]
    hv = body["has_validation"]
    base = 4.0 if hg else 3.0
    if hg and hv:
        base += 0.5
    return SubItemScore(
        base=_clamp(base),
        formula=f"gotchas={hg}→4.0 + (validation:{hv} ? +0.5)",
        evidence={"has_gotchas_section": hg, "has_validation": hv},
    )


def score_R2(fm, body, directory, safety) -> SubItemScore:
    hw = body["has_workflow_steps"]
    sc = body["step_count"]
    cs = body["cli_sections_count"]
    ex = directory["examples_files"]
    st = body["skill_type"]
    base = 4.5 if hw else (4.0 if cs >= 3 else 3.5)
    if sc >= 5 or ex >= 10:
        base += 0.3
    return SubItemScore(
        base=_clamp(base),
        formula=f"WF={hw}({sc}steps) CLI={cs} exs={ex} type={st} → {base}",
        evidence={"has_workflow_steps": hw, "step_count": sc, "cli_sections_count": cs, "examples_files": ex},
    )


def score_R3(fm, body, directory, safety) -> SubItemScore:
    hg = body["has_gotchas_section"]
    hr = body["has_rules_section"]
    hv = body["has_validation"]
    base = 4.0
    if hg or hr:
        base += 0.3
    if hv:
        base += 0.2
    return SubItemScore(
        base=_clamp(base),
        formula=f"gotchas={hg} rules={hr} validation={hv} → {base}",
        evidence={"has_gotchas_section": hg, "has_rules_section": hr, "has_validation": hv},
    )


def score_R4(fm, body, directory, safety) -> SubItemScore:
    hb = body["has_boundary"]
    base = 4.5 if hb else 3.5
    return SubItemScore(
        base=_clamp(base),
        formula=f"boundary={hb} → {base}",
        evidence={"has_boundary": hb},
    )


# ── A · Adaptability ──

def score_A1(fm, body, directory, safety) -> SubItemScore:
    hb = body["has_boundary"]
    hw = body["has_when_to_use"]
    base = 4.5 if (hb and hw) else 4.0
    return SubItemScore(
        base=_clamp(base),
        formula=f"boundary={hb} + when_to_use={hw} → {base}",
        evidence={"has_boundary": hb, "has_when_to_use": hw},
    )


def score_A2(fm, body, directory, safety) -> SubItemScore:
    dl = fm["description_length"]
    dv = fm["description_valid"]
    base = 5.0 if dl >= 100 else (4.5 if dl >= 50 else 3.5)
    if not dv:
        base = min(base, 3.0)
    return SubItemScore(
        base=_clamp(base),
        formula=f"description_length={dl} valid={dv} → {base}",
        evidence={"description_length": dl, "description_valid": dv},
    )


def score_A3(fm, body, directory, safety) -> SubItemScore:
    hc = body["has_chinese"]
    bl = body["body_lines"]
    base = 4.0
    if hc:
        base += 0.3
    return SubItemScore(
        base=_clamp(base),
        formula=f"chinese={hc} → {base}",
        evidence={"has_chinese": hc},
    )


def score_A4(fm, body, directory, safety) -> SubItemScore:
    ex = directory["examples_files"]
    rf = directory["references_files"]
    st = body["skill_type"]
    base = 4.5 if (ex >= 10 or st == "cli") else 4.0
    return SubItemScore(
        base=_clamp(base),
        formula=f"type={st} exs={ex} refs={rf} → {base}",
        evidence={"skill_type": st, "examples_files": ex, "references_files": rf},
    )


# ── C · Convention ──

def score_C1(fm, body, directory, safety) -> SubItemScore:
    ex = directory["examples_files"]
    st = body["skill_type"]
    threshold = 4 if st == "cli" else 10
    base = 5.0 if ex >= threshold else (4.5 if ex >= 3 else 3.5)
    return SubItemScore(
        base=_clamp(base),
        formula=f"type={st} exs={ex}>={threshold} → {base}",
        evidence={"skill_type": st, "examples_files": ex},
    )


def score_C2(fm, body, directory, safety) -> SubItemScore:
    rf = directory["references_files"]
    bl = body["body_lines"]
    th = body["has_trigger_hints"]
    st = body["skill_type"]
    base = 4.0
    body_threshold = 150 if st == "cli" else 200
    if rf >= 8 and bl < body_threshold:
        base = 5.0
    elif rf >= 3 and bl < 350:
        base = 4.5
    elif rf > 0:
        base = 4.0
    else:
        base = 3.0
    if th and rf > 0:
        base += 0.2
    return SubItemScore(
        base=_clamp(base),
        formula=f"type={st} refs={rf} body={bl} trigger_hints={th} → {base}",
        evidence={"references_files": rf, "body_lines": bl, "has_trigger_hints": th},
    )


def score_C3(fm, body, directory, safety) -> SubItemScore:
    nv = fm["name_valid"]
    nm = fm["name_matches_dir"]
    rs = directory["references_subdirs"]
    base = 4.5
    if nv and nm:
        base += 0.2
    if rs >= 2:
        base += 0.3
    return SubItemScore(
        base=_clamp(base),
        formula=f"name_valid={nv} name_matches={nm} ref_subdirs={rs} → {base}",
        evidence={"name_valid": nv, "name_matches_dir": nm, "references_subdirs": rs},
    )


def score_C4(fm, body, directory, safety) -> SubItemScore:
    hg = body["has_gotchas_section"]
    gc = body.get("gotchas_count", 0)
    base = 4.5 if hg else 3.5
    if gc >= 5:
        base += 0.3
    return SubItemScore(
        base=_clamp(base),
        formula=f"gotchas_section={hg} gotchas_count≈{gc} → {base}",
        evidence={"has_gotchas_section": hg, "gotchas_count_approx": gc},
    )


# ── E · Effectiveness ──

def score_E1(fm, body, directory, safety) -> SubItemScore:
    hw = body["has_workflow_steps"]
    hv = body["has_validation"]
    st = body["skill_type"]
    base = 4.5 if hw else 4.0
    if hv:
        base += 0.3
    return SubItemScore(
        base=_clamp(base),
        formula=f"type={st} WF={hw} validation={hv} → {base}",
        evidence={"skill_type": st, "has_workflow_steps": hw, "has_validation": hv},
    )


def score_E2(fm, body, directory, safety) -> SubItemScore:
    ex = directory["examples_files"]
    st = body["skill_type"]
    thresholds = {"prompt": 25, "cli": 4, "doc": 5}
    t = thresholds.get(st, 5)
    base = 5.0 if ex >= t else (4.5 if ex >= 10 else (4.0 if ex >= 3 else 3.0))
    return SubItemScore(
        base=_clamp(base),
        formula=f"type={st} exs={ex}>={t} → {base}",
        evidence={"skill_type": st, "examples_files": ex},
    )


def score_E3(fm, body, directory, safety) -> SubItemScore:
    rs = directory["references_subdirs"]
    rf = directory["references_files"]
    base = 4.5 if rs >= 2 else 4.0
    if rf >= 10:
        base += 0.2
    return SubItemScore(
        base=_clamp(base),
        formula=f"ref_subdirs={rs} refs={rf} → {base}",
        evidence={"references_subdirs": rs, "references_files": rf},
    )


def score_E4(fm, body, directory, safety) -> SubItemScore:
    hw = body["has_workflow_steps"]
    hv = body["has_validation"]
    hg = body["has_gotchas_section"]
    cs = body["cli_sections_count"]
    base = 4.0
    if hw:
        base += 0.3
    if hv:
        base += 0.3
    if hg:
        base += 0.2
    if cs >= 3:
        base += 0.2
    return SubItemScore(
        base=_clamp(base),
        formula=f"WF={hw} val={hv} gotchas={hg} cli_secs={cs} → {base}",
        evidence={"has_workflow_steps": hw, "has_validation": hv, "has_gotchas_section": hg, "cli_sections_count": cs},
    )


# ── Master table ──

SCORE_FUNCTIONS: Dict[str, callable] = {
    "T1": score_T1, "T2": score_T2, "T3": score_T3, "T4": score_T4,
    "R1": score_R1, "R2": score_R2, "R3": score_R3, "R4": score_R4,
    "A1": score_A1, "A2": score_A2, "A3": score_A3, "A4": score_A4,
    "C1": score_C1, "C2": score_C2, "C3": score_C3, "C4": score_C4,
    "E1": score_E1, "E2": score_E2, "E3": score_E3, "E4": score_E4,
}


def compute_base_scores(fm, body, directory, safety) -> Dict[str, Any]:
    dims = {"T": [], "R": [], "A": [], "C": [], "E": []}
    for key, fn in SCORE_FUNCTIONS.items():
        dim = key[0]
        sub = fn(fm, body, directory, safety)
        dims[dim].append(sub)

    result = {}
    for dim, subs in dims.items():
        avg = round(sum(s.base for s in subs) / len(subs), 2) if subs else 0.0
        result[dim] = {
            "avg": avg,
            "sub_items": {f"{dim}{i+1}": {"base": subs[i].base, "formula": subs[i].formula, "evidence": subs[i].evidence} for i in range(len(subs))},
        }
    result["overall"] = round(
        sum(result[d]["avg"] for d in ["T", "R", "A", "C", "E"]) / 5.0, 2
    )
    return result


def main() -> int:
    args = parse_args()
    skill_dir = Path(args.skill_dir).expanduser().resolve()

    fm, body, directory, safety, _ = collect_facts(skill_dir)
    if not fm:
        return 1

    base_scores = compute_base_scores(fm, body, directory, safety)

    packet = {
        "skill_dir": str(skill_dir),
        "skill_name": (fm.get("name") or skill_dir.name).strip(),
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "frontmatter": fm,
        "body": body,
        "directory": directory,
        "safety": safety,
        "base_scores": base_scores,
    }

    if args.format == "pretty":
        out = json.dumps(packet, ensure_ascii=False, indent=2, default=str)
    else:
        out = json.dumps(packet, ensure_ascii=False, indent=2, default=str)

    if args.output:
        out_path = Path(args.output).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out, encoding="utf-8")
        return 0

    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
