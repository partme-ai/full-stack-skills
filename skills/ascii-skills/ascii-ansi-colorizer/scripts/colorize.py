#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Options:
    """ANSI 上色参数。"""

    mode: str
    direction: str
    start: int
    end: int
    keep_spaces: bool


def parse_args(argv: Sequence[str] | None = None) -> Options:
    """解析命令行参数。"""

    p = argparse.ArgumentParser(description="ANSI colorize text (gradient/rainbow). Reads stdin, writes stdout.")
    p.add_argument("--mode", choices=["gradient", "rainbow"], default="gradient")
    p.add_argument("--direction", choices=["lr", "tb"], default="lr", help="lr=left->right, tb=top->bottom")
    p.add_argument("--start", type=int, default=33, help="ANSI 256 start color (0-255)")
    p.add_argument("--end", type=int, default=129, help="ANSI 256 end color (0-255)")
    p.add_argument("--keep-spaces", action="store_true", help="Colorize spaces too (not recommended)")
    ns = p.parse_args(argv)
    return Options(
        mode=ns.mode,
        direction=ns.direction,
        start=max(0, min(255, ns.start)),
        end=max(0, min(255, ns.end)),
        keep_spaces=bool(ns.keep_spaces),
    )


def _ansi_fg(code: int) -> str:
    """生成 ANSI 256 前景色控制序列。"""

    return f"\x1b[38;5;{code}m"


def _reset() -> str:
    """生成 ANSI 重置序列。"""

    return "\x1b[0m"


def _lerp(a: int, b: int, t: float) -> int:
    """线性插值计算 ANSI 颜色码。"""

    return int(round(a + (b - a) * t))


def colorize_lines(lines: Sequence[str], opt: Options) -> Iterable[str]:
    """对文本行应用 ANSI 上色。"""

    reset = _reset()
    if not lines:
        return []

    max_len = max(len(l.rstrip("\n")) for l in lines) or 1
    total_lines = len(lines)

    def pick_color(x: int, y: int) -> int:
        if opt.mode == "rainbow":
            # 使用 256 色中较饱和的一段
            base = [196, 202, 208, 214, 220, 46, 51, 39, 27, 93, 129]
            idx = (x if opt.direction == "lr" else y) % len(base)
            return base[idx]
        if opt.direction == "tb":
            t = 0.0 if total_lines <= 1 else y / (total_lines - 1)
        else:
            t = 0.0 if max_len <= 1 else x / (max_len - 1)
        return _lerp(opt.start, opt.end, t)

    for y, raw in enumerate(lines):
        line = raw.rstrip("\n")
        out = []
        for x, ch in enumerate(line):
            if ch == " " and not opt.keep_spaces:
                out.append(ch)
                continue
            code = pick_color(x, y)
            out.append(_ansi_fg(code) + ch + reset)
        yield "".join(out)


def main(argv: Sequence[str] | None = None) -> int:
    """程序入口：从 stdin 读取并上色输出。"""

    opt = parse_args(argv)
    data = sys.stdin.read().splitlines()
    for line in colorize_lines(data, opt):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
