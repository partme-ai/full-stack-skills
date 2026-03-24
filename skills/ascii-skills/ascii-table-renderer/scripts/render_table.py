#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from typing import Any, List, Sequence


@dataclass(frozen=True)
class Options:
    """ASCII 表格渲染参数。"""

    fmt: str
    max_width: int
    max_col_width: int
    overflow: str
    border: str
    align: str


def parse_args(argv: Sequence[str] | None = None) -> Options:
    """解析命令行参数。"""

    p = argparse.ArgumentParser(description="Render ASCII table from JSON on stdin.")
    p.add_argument("--format", choices=["compact", "readable"], default="readable")
    p.add_argument("--max-width", type=int, default=80)
    p.add_argument("--max-col-width", type=int, default=20)
    p.add_argument("--overflow", choices=["ellipsis", "wrap"], default="ellipsis")
    p.add_argument("--border", choices=["light", "minimal"], default="light")
    p.add_argument("--align", choices=["left", "right", "center"], default="left")
    ns = p.parse_args(argv)
    return Options(
        fmt=ns.format,
        max_width=max(20, ns.max_width),
        max_col_width=max(4, ns.max_col_width),
        overflow=ns.overflow,
        border=ns.border,
        align=ns.align,
    )


def _stringify(value: Any) -> str:
    """把值转换为可显示字符串。"""

    if value is None:
        return "-"
    return str(value)


def _truncate(text: str, width: int) -> str:
    """按列宽截断文本。"""

    if width <= 0:
        return ""
    if len(text) <= width:
        return text
    if width <= 3:
        return text[:width]
    return text[: width - 3] + "..."


def _pad(text: str, width: int, align: str) -> str:
    """按对齐方式填充字符串到固定宽度。"""

    text = text[:width]
    if align == "right":
        return text.rjust(width)
    if align == "center":
        return text.center(width)
    return text.ljust(width)


def _compute_widths(headers: List[str], rows: List[List[str]], max_col_width: int) -> List[int]:
    """计算列宽（按最大内容宽度，受 max_col_width 限制）。"""

    widths = [min(max_col_width, max(1, len(h))) for h in headers]
    for r in rows:
        for i, cell in enumerate(r):
            widths[i] = min(max_col_width, max(widths[i], len(cell)))
    return widths


def render_table(headers: List[str], rows: List[List[str]], opt: Options) -> str:
    """渲染 ASCII 表格。"""

    if not headers:
        return ""
    normalized_rows = [[_stringify(c) for c in row] for row in rows]
    for r in normalized_rows:
        while len(r) < len(headers):
            r.append("-")
        if len(r) > len(headers):
            del r[len(headers) :]

    widths = _compute_widths(headers, normalized_rows, opt.max_col_width)

    def cell(text: str, w: int) -> str:
        if opt.overflow == "ellipsis":
            text = _truncate(text, w)
        else:
            text = text[:w]
        return _pad(text, w, opt.align)

    def sep(ch: str = "-") -> str:
        if opt.border == "minimal":
            return ""
        return "+" + "+".join((ch * (w + 2)) for w in widths) + "+"

    def row_line(vals: List[str]) -> str:
        if opt.border == "minimal":
            return "  ".join(cell(v, w) for v, w in zip(vals, widths))
        return "| " + " | ".join(cell(v, w) for v, w in zip(vals, widths)) + " |"

    lines: List[str] = []
    if opt.border != "minimal":
        lines.append(sep("-"))
    lines.append(row_line(headers))
    if opt.border == "minimal":
        lines.append("-" * min(opt.max_width, max(10, sum(widths) + (len(widths) - 1) * 2)))
    else:
        lines.append(sep("-"))
    for r in normalized_rows:
        lines.append(row_line(r))
    if opt.border != "minimal" and opt.fmt == "readable":
        lines.append(sep("-"))

    out = "\n".join(lines)
    # maxWidth 只做保底截断（避免极端输入刷屏）
    return "\n".join(line[: opt.max_width].rstrip() for line in out.splitlines()).rstrip()


def main(argv: Sequence[str] | None = None) -> int:
    """程序入口：从 stdin 读取 JSON 并输出表格。"""

    opt = parse_args(argv)
    raw = sys.stdin.read().strip()
    if not raw:
        print("Error: empty stdin. Provide JSON with headers and rows.", file=sys.stderr)
        return 1
    data = json.loads(raw)
    headers = [str(x) for x in data.get("headers", [])]
    rows = data.get("rows", [])
    if not isinstance(rows, list):
        print("Error: rows must be a list.", file=sys.stderr)
        return 1
    str_rows: List[List[str]] = [[_stringify(c) for c in (row if isinstance(row, list) else [row])] for row in rows]
    print(render_table(headers, str_rows, opt))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
