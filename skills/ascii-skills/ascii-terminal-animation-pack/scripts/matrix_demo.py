#!/usr/bin/env python3
from __future__ import annotations

import argparse
import random
import sys
import time
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class Options:
    """矩阵雨演示参数（短时运行）。"""

    width: int
    height: int
    fps: int
    seconds: float
    ansi256: bool


def parse_args(argv: Sequence[str] | None = None) -> Options:
    """解析命令行参数。"""

    p = argparse.ArgumentParser(description="Matrix rain demo (short-run).")
    p.add_argument("--width", type=int, default=80)
    p.add_argument("--height", type=int, default=24)
    p.add_argument("--fps", type=int, default=10)
    p.add_argument("--seconds", type=float, default=3.0)
    p.add_argument("--ansi256", action="store_true", help="Enable ANSI 256 green (best-effort)")
    ns = p.parse_args(argv)
    return Options(
        width=max(20, ns.width),
        height=max(10, ns.height),
        fps=max(1, min(30, ns.fps)),
        seconds=max(0.5, ns.seconds),
        ansi256=bool(ns.ansi256),
    )


def _is_tty() -> bool:
    """判断 stdout 是否为交互终端。"""

    return sys.stdout.isatty()


def _ansi(code: int) -> str:
    """ANSI 256 前景色。"""

    return f"\x1b[38;5;{code}m"


def _reset() -> str:
    """ANSI reset。"""

    return "\x1b[0m"


def main(argv: Sequence[str] | None = None) -> int:
    """程序入口：仅在 TTY 中运行，避免刷屏日志。"""

    opt = parse_args(argv)
    if not _is_tty():
        print("Non-interactive output detected. Skip animation.", file=sys.stderr)
        return 0

    charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    drops = [random.randint(0, opt.height - 1) for _ in range(opt.width)]
    start = time.time()
    frame_delay = 1.0 / opt.fps
    reset = _reset()
    green = _ansi(46)  # bright green

    # 清屏 + 隐藏光标
    sys.stdout.write("\x1b[2J\x1b[?25l")
    sys.stdout.flush()
    try:
        while time.time() - start < opt.seconds:
            # 光标回到左上角
            sys.stdout.write("\x1b[H")
            lines = []
            for y in range(opt.height):
                row = []
                for x in range(opt.width):
                    if drops[x] == y:
                        ch = random.choice(charset)
                        if opt.ansi256:
                            row.append(green + ch + reset)
                        else:
                            row.append(ch)
                    else:
                        row.append(" ")
                lines.append("".join(row))
            sys.stdout.write("\n".join(lines))
            sys.stdout.flush()

            # 更新 drop
            for x in range(opt.width):
                if random.random() < 0.2:
                    drops[x] = (drops[x] + 1) % opt.height
            time.sleep(frame_delay)
        return 0
    finally:
        # 显示光标 + reset
        sys.stdout.write("\x1b[?25h" + reset + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    raise SystemExit(main())
