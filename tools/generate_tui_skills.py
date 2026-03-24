#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
# tui-skills 已迁移至 t2ui-skills 仓库；生成目标为同级 t2ui-skills/skills
TUI_SKILLS_DIR = ROOT.parent / "t2ui-skills" / "skills"
SOURCES_INDEX = ROOT / "tui-sources" / "components.json"

DO_NOT_OVERWRITE = {
    "tui-button",
    "tui-input",
    "tui-form",
    "tui-modal",
    "tui-table",
    "tui-tabs",
    "tui-navbar",
    "tui-select",
    "tui-cell",
    "tui-rate",
}


def title_from_slug(slug: str) -> str:
    return " ".join(p.capitalize() for p in slug.split("-") if p).strip() or slug


def classify(slug: str) -> str:
    s = slug.lower()
    if any(k in s for k in ["button", "fab"]):
        return "action"
    if any(k in s for k in ["input", "textarea", "field", "keyboard", "message-input", "verification-code"]):
        return "text-input"
    if "checkbox" in s:
        return "checkbox"
    if "radio" in s:
        return "radio"
    if "switch" in s:
        return "switch"
    if any(k in s for k in ["select", "picker", "dropdown"]):
        return "select"
    if "rate" in s:
        return "rating"
    if any(k in s for k in ["table", "grid"]):
        return "data-table"
    if any(k in s for k in ["tabs", "tabbar", "subsection", "swiper"]):
        return "tabs"
    if any(k in s for k in ["navbar", "top-tips", "notice-bar"]):
        return "top-bar"
    if any(k in s for k in ["modal", "popup", "mask", "action-sheet"]):
        return "overlay"
    if any(k in s for k in ["toast", "alert", "empty", "no-network", "loading"]):
        return "feedback"
    if any(k in s for k in ["progress", "count-down", "count-to"]):
        return "progress"
    if any(k in s for k in ["calendar", "time-line", "steps"]):
        return "timeline"
    if any(k in s for k in ["image", "avatar", "upload"]):
        return "media"
    if any(k in s for k in ["card", "cell", "section", "divider", "line"]):
        return "container"
    return "generic"


def example_tui(title: str, kind: str, variant: str) -> str:
    if kind == "action":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ [✓] Save changes                                             │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Keys: <enter> click  <esc> back                               │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ [ Save changes ]                                             │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ [ Continue ]                                                 │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "text-input":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Email                                                        │\n"
                "│ [ ada@example.com|___________________________ ]   [x]         │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Keys: <tab> next  <enter> commit  <esc> back                  │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Password                                                     │\n"
                "│ [ ••••••••••_______________________________ ]                │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ Search                                                       │\n"
            "│ [ type here...______________________________ ]               │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "checkbox":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ [x] Email alerts                                             │\n"
                "│ [ ] SMS alerts                                               │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ [x] Accept terms                                             │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ [ ] Remember me                                              │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "radio":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ ( ) Daily summary   (*) Weekly summary                        │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ (*) Weekly summary                                           │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ (*) Option A   ( ) Option B                                  │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "switch":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Enable feature:  [ ON ]                                      │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Enable feature:  [ ON ]                                      │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ Enable feature:  [ OFF ]                                     │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "select":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Plan: [ Pro ]                                                │\n"
                "│                                                            │\n"
                "│ > Pro                                                       │\n"
                "│   Team (disabled)                                            │\n"
                "│   Enterprise                                                 │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Plan: [ Pro ]                                                │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ Country: [ Select... ]                                       │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "rating":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ * * * * .  (4/5)                                             │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Keys: <left>/<right> adjust  <enter> confirm  <esc> back      │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ * * * + .  (3.5/5)                                           │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ * * . . .  (2/5)                                             │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "data-table":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Name ↑               | Role        | Last login              │\n"
                "│ Ada Lovelace         | Engineer    | 2026-01-30 12:43         │\n"
                "│ Grace Hopper         | Admiral     | 2026-01-29 09:10         │\n"
                "│ A very very long na… | Analyst     | 2026-01-28 20:01         │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ (table is read-only)                                         │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ Name                 | Status                                │\n"
            "│ Ada Lovelace         | Active                                │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "tabs":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ [Profile]  Settings  Security  Notific…  (Billing)           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Keys: <left>/<right> switch  <enter> activate  <esc> back     │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ [Profile]  (Settings)                                        │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ [Home]  Search  Settings                                     │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "top-bar":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ < Back              Settings                      Edit >     │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ (navigation disabled)                                        │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ Title                                                        │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "overlay":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ ┌──────────────────────────────────────────────────────────┐ │\n"
                "│ │ Confirm action?                                          │ │\n"
                "│ │ [Cancel]                              [Confirm]          │ │\n"
                "│ └──────────────────────────────────────────────────────────┘ │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ (overlay hidden)                                             │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ (overlay)                                                    │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "feedback":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Success: Saved                                               │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ (no messages)                                                │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ Loading...                                                   │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "progress":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ [██████████░░░░░░░░░░░░░░░]  42%                             │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ [████████████████████████]  100%                             │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ [██░░░░░░░░░░░░░░░░░░░░░░]  10%                              │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "timeline":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ 1) Draft   →  2) Review  →  3) Done                          │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ (timeline is read-only)                                      │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ • 09:00  Check-in                                            │\n"
            "│ • 12:00  Lunch                                               │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "media":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ [Image: 320x180]                                             │\n"
                "│ ██████████████████████████████████████████████████████       │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ (media unavailable)                                          │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ [Avatar]  (A)                                                │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if kind == "container":
        if variant == "styled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}]                                                    │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ Title: Account Overview                                      │\n"
                "│ Balance: $2,340.18                                           │\n"
                "│ Status: Active                                               │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        if variant == "disabled":
            return (
                "┌──────────────────────────────────────────────────────────────┐\n"
                f"│ [{title}] Disabled                                           │\n"
                "├──────────────────────────────────────────────────────────────┤\n"
                "│ (content hidden)                                             │\n"
                "└──────────────────────────────────────────────────────────────┘"
            )
        return (
            "┌──────────────────────────────────────────────────────────────┐\n"
            f"│ [{title}]                                                    │\n"
            "├──────────────────────────────────────────────────────────────┤\n"
            "│ Item A                                   >                   │\n"
            "│ Item B                                   >                   │\n"
            "└──────────────────────────────────────────────────────────────┘"
        )

    if variant == "disabled":
        body = "Error: Something went wrong…"
        status = "Disabled"
    elif variant == "styled":
        body = "(custom style example)"
        status = ""
    else:
        body = "(default state)"
        status = ""

    status_suffix = f" {status}" if status else ""
    return (
        "┌──────────────────────────────────────────────────────────────┐\n"
        f"│ [{title}]{status_suffix:<52}│\n"
        "├──────────────────────────────────────────────────────────────┤\n"
        f"│ {body:<60}│\n"
        "└──────────────────────────────────────────────────────────────┘"
    )


def render_skill_md(skill_name: str, slug: str, tag: str) -> str:
    title = title_from_slug(slug)
    kind = classify(slug)
    ex1_tui = example_tui(title, kind, "default")
    ex2_tui = example_tui(title, kind, "styled")
    ex3_tui = example_tui(title, kind, "disabled")
    summary_row = (
        f'| {skill_name} | {title} | 0 | 0 | 0 | 0 | 0 | keyProps=... | state=... | hotkeys=... |'
    )

    return f"""---
name: {skill_name}
description: Generate pixel-precise ASCII TUI for {title} ({tag}) with strict output blocks (TUI_RENDER, COMPONENT_SPEC, PENCIL_SPEC, PENCIL_BATCH_DESIGN) suitable for Pencil MCP drawing workflows.
---

## Purpose

- Produce an ASCII Text UI (TUI) representation of **{title}**.
- Always output layout attributes (top/left/width/height, spacing, colors, typography, zIndex).
- Always output Pencil MCP–ready specs and a `batch_design` plan (≤25 operations per call).

## Source Documentation

This skill intentionally does not embed external doc URLs. Use the repository index:

- `full-stack-skills/tui-sources/components.json` (lookup by `skill={skill_name}` or `slug={slug}`)

## Input Model (Recommended)

```json
{{
  "widthCols": 70,
  "grid": {{ "cellWidthPx": 8, "cellHeightPx": 16 }},
  "props": {{}},
  "modelValue": null,
  "state": {{ "focused": false, "disabled": false, "loading": false, "error": null }},
  "style": {{
    "fillColor": "#ffffff",
    "textColor": "#111111",
    "strokeColor": "#e5e7eb",
    "strokeThickness": 1,
    "cornerRadius": 12
  }},
  "typography": {{ "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 }},
  "layout": {{ "paddingPx": 16, "gapPx": 8 }},
  "hotkeys": []
}}
```

## Output Contract (Mandatory)

### OUTPUT: TUI_RENDER

```text
...monospace-only text...
```

### OUTPUT: COMPONENT_SPEC

```json
{{
  "id": "{skill_name}_1",
  "name": "{title}",
  "type": "{skill_name}",
  "bbox": {{ "topPx": 0, "leftPx": 0, "widthPx": 0, "heightPx": 0 }},
  "zIndex": 1,
  "layout": {{ "paddingPx": 16, "gapPx": 8, "align": "left", "valign": "top" }},
  "style": {{
    "fillColor": "#ffffff",
    "textColor": "#111111",
    "strokeColor": "#e5e7eb",
    "strokeThickness": 1,
    "cornerRadius": 12,
    "opacity": 1
  }},
  "typography": {{ "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 }},
  "overflow": {{ "mode": "truncate", "ellipsis": "…", "maxLines": 1 }},
  "state": {{ "focused": false, "disabled": false, "loading": false, "error": null }},
  "hotkeys": []
}}
```

### OUTPUT: PENCIL_SPEC

```json
{{
  "canvas": {{ "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" }},
  "grid": {{ "cellWidthPx": 8, "cellHeightPx": 16 }},
  "nodes": [],
  "components": []
}}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{{type:"frame",name:"Screen"}})
U(screen,{{width:390,height:844,x:0,y:0}})

CALL 2:
cmpBg=I(screen,{{type:"rect",name:"{title}/Background"}})
U(cmpBg,{{x:24,y:24,width:342,height:96,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12}})
cmpText=I(screen,{{type:"text",name:"{title}/Text",content:"{title}"}})
U(cmpText,{{x:40,y:56,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600}})
```

## Rendering Rules (Component-Level)

Follow the shared rules from `tui-front-ui`:
- No TAB characters.
- Do not exceed `widthCols`.
- Provide a header row, body area, and minimal hotkeys if interactive.
- `disabled=true` must suppress interaction hints.
- `loading=true` must show a stable placeholder.
- `error!=null` must be printed in a single line footer (truncated to width).

## Examples (Must include all output blocks)

### Example 1 — Minimal / default

### OUTPUT: TUI_RENDER

```text
{ex1_tui}
```

### OUTPUT: COMPONENT_SPEC

```json
{{
  "id": "{skill_name}_ex1",
  "name": "{title}",
  "type": "{skill_name}",
  "bbox": {{ "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 96 }},
  "zIndex": 1,
  "layout": {{ "paddingPx": 16, "gapPx": 8, "align": "left", "valign": "top" }},
  "style": {{ "fillColor": "#ffffff", "textColor": "#111111", "strokeColor": "#e5e7eb", "strokeThickness": 1, "cornerRadius": 12, "opacity": 1 }},
  "typography": {{ "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 }},
  "overflow": {{ "mode": "truncate", "ellipsis": "…", "maxLines": 1 }},
  "state": {{ "focused": false, "disabled": false, "loading": false, "error": null }},
  "hotkeys": []
}}
```

### OUTPUT: PENCIL_SPEC

```json
{{
  "canvas": {{ "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" }},
  "grid": {{ "cellWidthPx": 8, "cellHeightPx": 16 }},
  "nodes": [],
  "components": [
    {{ "id": "{skill_name}_ex1", "name": "{title}", "bbox": {{ "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 96 }}, "zIndex": 1 }}
  ]
}}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{{type:"frame",name:"Screen"}})
U(screen,{{width:390,height:844,x:0,y:0}})

CALL 2:
cmpBg=I(screen,{{type:"rect",name:"{title}/Background"}})
U(cmpBg,{{x:24,y:24,width:342,height:96,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12}})
cmpText=I(screen,{{type:"text",name:"{title}/Text",content:"{title}"}})
U(cmpText,{{x:40,y:56,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600}})
```

### Example 2 — Styled / customized

### OUTPUT: TUI_RENDER

```text
{ex2_tui}
```

### OUTPUT: COMPONENT_SPEC

```json
{{
  "id": "{skill_name}_ex2",
  "name": "{title}",
  "type": "{skill_name}",
  "bbox": {{ "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 104 }},
  "zIndex": 1,
  "layout": {{ "paddingPx": 20, "gapPx": 10, "align": "left", "valign": "top" }},
  "style": {{ "fillColor": "#ffffff", "textColor": "#111111", "strokeColor": "#111111", "strokeThickness": 2, "cornerRadius": 12, "opacity": 1 }},
  "typography": {{ "fontFamily": "Inter", "fontSize": 14, "fontWeight": 600, "lineHeight": 20 }},
  "overflow": {{ "mode": "truncate", "ellipsis": "…", "maxLines": 1 }},
  "state": {{ "focused": false, "disabled": false, "loading": false, "error": null }},
  "hotkeys": []
}}
```

### OUTPUT: PENCIL_SPEC

```json
{{
  "canvas": {{ "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" }},
  "grid": {{ "cellWidthPx": 8, "cellHeightPx": 16 }},
  "nodes": [],
  "components": [
    {{ "id": "{skill_name}_ex2", "name": "{title}", "bbox": {{ "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 104 }}, "zIndex": 1 }}
  ]
}}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{{type:"frame",name:"Screen"}})
U(screen,{{width:390,height:844,x:0,y:0}})

CALL 2:
cmpBg=I(screen,{{type:"rect",name:"{title}/Background"}})
U(cmpBg,{{x:24,y:24,width:342,height:104,fillColor:"#ffffff",strokeColor:"#111111",strokeThickness:2,cornerRadius:12}})
cmpText=I(screen,{{type:"text",name:"{title}/Text",content:"{title}"}})
U(cmpText,{{x:40,y:60,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600}})
```

### Example 3 — Disabled / error / edge-case

### OUTPUT: TUI_RENDER

```text
{ex3_tui}
```

### OUTPUT: COMPONENT_SPEC

```json
{{
  "id": "{skill_name}_ex3",
  "name": "{title}",
  "type": "{skill_name}",
  "bbox": {{ "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 112 }},
  "zIndex": 1,
  "layout": {{ "paddingPx": 16, "gapPx": 8, "align": "left", "valign": "top" }},
  "style": {{ "fillColor": "#ffffff", "textColor": "#6b7280", "strokeColor": "#e5e7eb", "strokeThickness": 1, "cornerRadius": 12, "opacity": 1 }},
  "typography": {{ "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 }},
  "overflow": {{ "mode": "truncate", "ellipsis": "…", "maxLines": 1 }},
  "state": {{ "focused": false, "disabled": true, "loading": false, "error": "Something went wrong" }},
  "hotkeys": []
}}
```

### OUTPUT: PENCIL_SPEC

```json
{{
  "canvas": {{ "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" }},
  "grid": {{ "cellWidthPx": 8, "cellHeightPx": 16 }},
  "nodes": [],
  "components": [
    {{ "id": "{skill_name}_ex3", "name": "{title}", "bbox": {{ "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 112 }}, "zIndex": 1 }}
  ]
}}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{{type:"frame",name:"Screen"}})
U(screen,{{width:390,height:844,x:0,y:0}})

CALL 2:
cmpBg=I(screen,{{type:"rect",name:"{title}/Background"}})
U(cmpBg,{{x:24,y:24,width:342,height:112,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12,opacity:1}})
cmpText=I(screen,{{type:"text",name:"{title}/Error",content:"Error: Something went wrong…"}})
U(cmpText,{{x:40,y:60,width:310,height:20,textColor:"#6b7280",fontFamily:"Inter",fontSize:14,fontWeight:400}})
```

## Component Summary Row (for page aggregation)

```text
| id | name | top | left | width | height | z | keyProps | state | hotkeys |
{summary_row}
```
"""


def main() -> int:
    data = json.loads(SOURCES_INDEX.read_text(encoding="utf-8"))
    components: List[Dict[str, Any]] = data["components"]

    for c in components:
        skill = c["skill"]
        slug = c["slug"]
        tag = c["tag"]

        if skill in DO_NOT_OVERWRITE:
            continue

        skill_dir = TUI_SKILLS_DIR / skill
        skill_dir.mkdir(parents=True, exist_ok=True)
        skill_md = skill_dir / "SKILL.md"
        skill_md.write_text(render_skill_md(skill, slug, tag), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
