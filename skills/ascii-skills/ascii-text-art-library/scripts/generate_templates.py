#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class Options:
    """模板生成参数。"""

    width: int
    title: str


def parse_args(argv: Sequence[str] | None = None) -> Options:
    """解析命令行参数。"""

    p = argparse.ArgumentParser(description="Generate ASCII-only text templates.")
    p.add_argument("--width", type=int, default=80)
    p.add_argument("--title", default="PartmeAI")
    ns = p.parse_args(argv)
    return Options(width=max(40, ns.width), title=str(ns.title))


def hr(width: int, ch: str) -> str:
    """生成水平分隔线。"""

    return (ch or "-")[0] * max(0, width)


def title_line(title: str, width: int, ch: str) -> str:
    """生成标题行（居中）。"""

    title = f" {title.strip()} "
    if len(title) >= width:
        return title[:width]
    left = (width - len(title)) // 2
    right = width - len(title) - left
    return (ch * left) + title + (ch * right)


def box(title: str, bullets: list[str], width: int) -> str:
    """生成提示框。"""

    inner = max(10, width - 4)
    top = "+" + "-" * (width - 2) + "+"
    lines = [top]
    header = (title + ":").ljust(inner)[:inner]
    lines.append("| " + header + " |")
    for b in bullets:
        msg = ("- " + b).ljust(inner)[:inner]
        lines.append("| " + msg + " |")
    lines.append(top)
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    """程序入口：输出一套基础模板。"""

    opt = parse_args(argv)
    print(title_line(opt.title, opt.width, "="))
    print(title_line(opt.title, opt.width, "-"))
    print(hr(opt.width, "-"))
    print(hr(opt.width, "="))
    print()
    print(box("INFO", ["This is an informational message.", "Keep it short and actionable."], opt.width))
    print()
    print(box("WARN", ["Do NOT paste tokens here."], opt.width))
    print()
    print(box("ERROR", ["Operation failed. Check logs and retry."], opt.width))
    print()
    print(box("SUCCESS", ["Completed successfully."], opt.width))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
