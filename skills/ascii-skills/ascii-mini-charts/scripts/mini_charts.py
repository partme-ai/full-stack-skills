#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from typing import List, Sequence


@dataclass(frozen=True)
class Options:
    """迷你图输出参数。"""

    chart_type: str
    width: int
    height: int
    normalize: str
    annotated: bool


def parse_args(argv: Sequence[str] | None = None) -> Options:
    """解析命令行参数。"""

    p = argparse.ArgumentParser(description="Generate ASCII mini charts from JSON on stdin.")
    p.add_argument("--type", choices=["sparkline", "bar"], default="sparkline")
    p.add_argument("--width", type=int, default=30)
    p.add_argument("--height", type=int, default=10)
    p.add_argument("--normalize", choices=["linear", "log"], default="linear")
    p.add_argument("--annotated", action="store_true", help="Append min/max/current labels")
    ns = p.parse_args(argv)
    return Options(
        chart_type=ns.type,
        width=max(5, ns.width),
        height=max(3, ns.height),
        normalize=ns.normalize,
        annotated=bool(ns.annotated),
    )


def _normalize(values: List[float], mode: str) -> List[float]:
    """归一化到 0..1。"""

    if not values:
        return []
    if mode == "log":
        safe = [math.log(v + 1.0) for v in values]
        mn, mx = min(safe), max(safe)
        if mx == mn:
            return [0.5] * len(values)
        return [(v - mn) / (mx - mn) for v in safe]
    mn, mx = min(values), max(values)
    if mx == mn:
        return [0.5] * len(values)
    return [(v - mn) / (mx - mn) for v in values]


def _sample(values: List[float], width: int) -> List[float]:
    """将序列压缩到指定宽度（均匀采样）。"""

    if len(values) <= width:
        return values
    out: List[float] = []
    for i in range(width):
        idx = int(i * (len(values) - 1) / (width - 1))
        out.append(values[idx])
    return out


def render_sparkline(values: List[float], width: int, normalize: str) -> str:
    """渲染 ASCII-only sparkline。"""

    charset = " .:-=+*#%@"
    sampled = _sample(values, width)
    norm = _normalize(sampled, normalize)
    chars = []
    for t in norm:
        idx = int(round(t * (len(charset) - 1)))
        chars.append(charset[idx])
    return "".join(chars).rstrip()


def render_bar(values: List[float], width: int, height: int, normalize: str) -> str:
    """渲染纵向柱状图（ASCII-only）。"""

    sampled = _sample(values, width)
    norm = _normalize(sampled, normalize)
    levels = [int(round(t * height)) for t in norm]
    lines: List[str] = []
    for row in range(height, 0, -1):
        line = []
        for lv in levels:
            line.append("#" if lv >= row else " ")
        lines.append("".join(line).rstrip())
    return "\n".join(lines).rstrip()


def main(argv: Sequence[str] | None = None) -> int:
    """程序入口。"""

    opt = parse_args(argv)
    raw = sys.stdin.read().strip()
    if not raw:
        print("Error: empty stdin. Provide JSON with series.", file=sys.stderr)
        return 1
    data = json.loads(raw)
    series = data.get("series", [])
    values = [float(x) for x in series]
    if not values:
        print("", end="")
        return 0

    if opt.chart_type == "bar":
        out = render_bar(values, opt.width, opt.height, opt.normalize)
    else:
        out = render_sparkline(values, opt.width, opt.normalize)

    if opt.annotated:
        mn, mx, cur = min(values), max(values), values[-1]
        if "\n" in out:
            out += f"\nmin={mn:g} max={mx:g} cur={cur:g}"
        else:
            out += f"  min={mn:g} max={mx:g} cur={cur:g}"
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
