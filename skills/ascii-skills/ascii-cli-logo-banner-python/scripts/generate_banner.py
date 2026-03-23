#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Dict, List, Sequence


@dataclass(frozen=True)
class BannerInput:
    brand: str
    version: str | None
    repo: str | None
    docs: str | None
    author: str | None
    width: int
    color: str
    slogan: str | None
    hint: str | None
    center: bool
    rule: bool
    glyph: str
    color_mode: str
    color_start: int
    color_end: int


_FONT_5X5: Dict[str, List[str]] = {
    "A": [
        " XXX ",
        "X   X",
        "XXXXX",
        "X   X",
        "X   X",
    ],
    "B": [
        "XXXX ",
        "X   X",
        "XXXX ",
        "X   X",
        "XXXX ",
    ],
    "C": [
        " XXX ",
        "X   X",
        "X    ",
        "X   X",
        " XXX ",
    ],
    "D": [
        "XXXX ",
        "X   X",
        "X   X",
        "X   X",
        "XXXX ",
    ],
    "E": [
        "XXXXX",
        "X    ",
        "XXXX ",
        "X    ",
        "XXXXX",
    ],
    "F": [
        "XXXXX",
        "X    ",
        "XXXX ",
        "X    ",
        "X    ",
    ],
    "G": [
        " XXX ",
        "X    ",
        "X XXX",
        "X   X",
        " XXXX",
    ],
    "H": [
        "X   X",
        "X   X",
        "XXXXX",
        "X   X",
        "X   X",
    ],
    "I": [
        "XXXXX",
        "  X  ",
        "  X  ",
        "  X  ",
        "XXXXX",
    ],
    "J": [
        "XXXXX",
        "   X ",
        "   X ",
        "X  X ",
        " XX  ",
    ],
    "K": [
        "X   X",
        "X  X ",
        "XXX  ",
        "X  X ",
        "X   X",
    ],
    "L": [
        "X    ",
        "X    ",
        "X    ",
        "X    ",
        "XXXXX",
    ],
    "M": [
        "X   X",
        "XX XX",
        "X X X",
        "X   X",
        "X   X",
    ],
    "N": [
        "X   X",
        "XX  X",
        "X X X",
        "X  XX",
        "X   X",
    ],
    "O": [
        " XXX ",
        "X   X",
        "X   X",
        "X   X",
        " XXX ",
    ],
    "P": [
        "XXXX ",
        "X   X",
        "XXXX ",
        "X    ",
        "X    ",
    ],
    "Q": [
        " XXX ",
        "X   X",
        "X   X",
        "X  XX",
        " XXXX",
    ],
    "R": [
        "XXXX ",
        "X   X",
        "XXXX ",
        "X  X ",
        "X   X",
    ],
    "S": [
        " XXXX",
        "X    ",
        " XXX ",
        "    X",
        "XXXX ",
    ],
    "T": [
        "XXXXX",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  ",
    ],
    "U": [
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        " XXX ",
    ],
    "V": [
        "X   X",
        "X   X",
        "X   X",
        " X X ",
        "  X  ",
    ],
    "W": [
        "X   X",
        "X   X",
        "X X X",
        "XX XX",
        "X   X",
    ],
    "X": [
        "X   X",
        " X X ",
        "  X  ",
        " X X ",
        "X   X",
    ],
    "Y": [
        "X   X",
        " X X ",
        "  X  ",
        "  X  ",
        "  X  ",
    ],
    "Z": [
        "XXXXX",
        "   X ",
        "  X  ",
        " X   ",
        "XXXXX",
    ],
    "0": [
        " XXX ",
        "X   X",
        "X   X",
        "X   X",
        " XXX ",
    ],
    "1": [
        "  X  ",
        " XX  ",
        "  X  ",
        "  X  ",
        " XXX ",
    ],
    "2": [
        " XXX ",
        "X   X",
        "   X ",
        "  X  ",
        "XXXXX",
    ],
    "3": [
        "XXXX ",
        "    X",
        " XXX ",
        "    X",
        "XXXX ",
    ],
    "4": [
        "X   X",
        "X   X",
        "XXXXX",
        "    X",
        "    X",
    ],
    "5": [
        "XXXXX",
        "X    ",
        "XXXX ",
        "    X",
        "XXXX ",
    ],
    "6": [
        " XXX ",
        "X    ",
        "XXXX ",
        "X   X",
        " XXX ",
    ],
    "7": [
        "XXXXX",
        "   X ",
        "  X  ",
        " X   ",
        "X    ",
    ],
    "8": [
        " XXX ",
        "X   X",
        " XXX ",
        "X   X",
        " XXX ",
    ],
    "9": [
        " XXX ",
        "X   X",
        " XXXX",
        "    X",
        " XXX ",
    ],
    " ": [
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
    ],
    "-": [
        "     ",
        "     ",
        "XXXXX",
        "     ",
        "     ",
    ],
    "_": [
        "     ",
        "     ",
        "     ",
        "     ",
        "XXXXX",
    ],
    ".": [
        "     ",
        "     ",
        "     ",
        "     ",
        "  X  ",
    ],
    "'": [
        "  X  ",
        "  X  ",
        "     ",
        "     ",
        "     ",
    ],
    "!": [
        "  X  ",
        "  X  ",
        "  X  ",
        "     ",
        "  X  ",
    ],
}


def _fill_char(glyph: str) -> str:
    if glyph == "block":
        return "█"
    return "#"


def render_block_text(text: str, glyph: str) -> List[str]:
    fill = _fill_char(glyph)
    rows = [""] * 5
    for ch in text.upper():
        g = _FONT_5X5.get(ch, _FONT_5X5[" "])
        for i in range(5):
            painted = "".join(fill if c != " " else " " for c in g[i])
            rows[i] += painted + " "
    return [r.rstrip() for r in rows]


def truncate_line(line: str, width: int) -> str:
    """截断行内容，确保不超过指定列宽。"""

    if width <= 0:
        return ""
    return line[:width]


def center_line(line: str, width: int) -> str:
    if width <= 0:
        return ""
    s = line.rstrip("\n")
    if len(s) >= width:
        return s[:width].rstrip()
    pad_left = (width - len(s)) // 2
    return (" " * pad_left) + s


def _ansi_fg_256(code: int) -> str:
    return f"\x1b[38;5;{code}m"


def _ansi_reset() -> str:
    return "\x1b[0m"


def _lerp(a: int, b: int, t: float) -> int:
    return int(round(a + (b - a) * t))


def colorize_ansi256(lines: List[str], start: int, end: int) -> List[str]:
    reset = _ansi_reset()
    if not lines:
        return []
    max_len = max(len(l) for l in lines) or 1
    out_lines: List[str] = []
    for line in lines:
        out = []
        for x, ch in enumerate(line):
            if ch == " ":
                out.append(ch)
                continue
            t = 0.0 if max_len <= 1 else x / (max_len - 1)
            code = _lerp(start, end, t)
            out.append(_ansi_fg_256(code) + ch + reset)
        out_lines.append("".join(out))
    return out_lines


def hr(width: int, ch: str = "-") -> str:
    """生成水平分隔线。"""

    width = max(0, width)
    ch = (ch or "-")[0]
    return ch * width


def render_compact(b: BannerInput) -> str:
    """渲染窄屏降级 banner。"""

    title = b.brand
    if b.version:
        title += f" (v{b.version})"
    lines: List[str] = [truncate_line(title, b.width)]
    if b.slogan:
        lines.append(center_line(b.slogan, b.width))
    if b.hint:
        lines.append(center_line(b.hint, b.width))
    lines.append(hr(b.width, "-"))
    if b.repo:
        lines.append(truncate_line(f"Repo: {b.repo}", b.width))
    if b.docs:
        lines.append(truncate_line(f"Docs: {b.docs}", b.width))
    return "\n".join(lines).rstrip()


def render_plain(b: BannerInput) -> str:
    """渲染标准 ASCII-only banner。"""

    logo_lines = render_block_text(b.brand, b.glyph)
    if b.color_mode == "ansi256":
        logo_lines = colorize_ansi256(logo_lines, b.color_start, b.color_end)
    if b.center:
        lines: List[str] = [center_line(truncate_line(l, b.width), b.width) for l in logo_lines]
    else:
        lines = [truncate_line(l, b.width) for l in logo_lines]

    if b.slogan or b.hint:
        lines.append("")
    if b.slogan:
        lines.append(center_line(b.slogan, b.width))
    if b.hint:
        lines.append("")
        lines.append(center_line(b.hint, b.width))

    if b.rule:
        lines.append("")
        lines.append(hr(b.width, "-"))
        lines.append(truncate_line(f"Name: {b.brand}", b.width))
        if b.version:
            lines.append(truncate_line(f"Version: {b.version}", b.width))
        if b.author:
            lines.append(truncate_line(f"Author: {b.author}", b.width))
        if b.repo:
            lines.append(truncate_line(f"Repo: {b.repo}", b.width))
        if b.docs:
            lines.append(truncate_line(f"Docs: {b.docs}", b.width))
    return "\n".join(lines).rstrip()


def parse_args(argv: Sequence[str] | None = None) -> BannerInput:
    """解析命令行参数并构造 BannerInput。"""

    p = argparse.ArgumentParser(description="Generate ASCII-only CLI banner (with compact fallback).")
    p.add_argument("--brand", required=True, help="Brand name, e.g. PartmeAI")
    p.add_argument("--version", default=None, help="Version, e.g. 1.2.3")
    p.add_argument("--repo", default=None, help="Repository URL")
    p.add_argument("--docs", default=None, help="Docs URL")
    p.add_argument("--author", default=None, help="Author or team")
    p.add_argument("--width", type=int, default=80, help="Banner width, default 80")
    p.add_argument("--slogan", default=None, help="Centered slogan line under the logo")
    p.add_argument("--hint", default=None, help="Centered hint line under the slogan")
    p.add_argument("--glyph", default="ascii", choices=["ascii", "block"], help="Logo glyph style: ascii (#) or block (█)")
    p.add_argument("--center", dest="center", action="store_true", default=True, help="Center the logo within the width")
    p.add_argument("--no-center", dest="center", action="store_false", help="Do not center the logo")
    p.add_argument("--rule", dest="rule", action="store_true", default=True, help="Include horizontal rule + info block")
    p.add_argument("--no-rule", dest="rule", action="store_false", help="Only output logo + slogan/hint (no info block)")
    p.add_argument("--colorMode", default="none", choices=["none", "ansi256"], help="Color mode: none|ansi256 (logo only)")
    p.add_argument("--colorStart", type=int, default=33, help="ANSI 256 start color (0-255)")
    p.add_argument("--colorEnd", type=int, default=129, help="ANSI 256 end color (0-255)")
    ns = p.parse_args(argv)
    return BannerInput(
        brand=ns.brand,
        version=ns.version,
        repo=ns.repo,
        docs=ns.docs,
        author=ns.author,
        width=max(10, int(ns.width)),
        color="none",
        slogan=ns.slogan,
        hint=ns.hint,
        center=bool(ns.center),
        rule=bool(ns.rule),
        glyph=ns.glyph,
        color_mode=str(ns.colorMode),
        color_start=max(0, min(255, int(ns.colorStart))),
        color_end=max(0, min(255, int(ns.colorEnd))),
    )


def main(argv: Sequence[str] | None = None) -> int:
    """程序入口：根据 width 选择标准或 compact 输出。"""

    b = parse_args(argv)
    if b.width < 60:
        print(render_compact(b))
        return 0
    print(render_plain(b))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
