#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import time
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class Options:
    """进度条/Spinner 演示参数。"""

    mode: str
    width: int
    seconds: float
    log: bool


def parse_args(argv: Sequence[str] | None = None) -> Options:
    """解析命令行参数。"""

    p = argparse.ArgumentParser(description="ASCII progress/spinner demo.")
    p.add_argument("--mode", choices=["bar", "spinner"], default="bar")
    p.add_argument("--width", type=int, default=40)
    p.add_argument("--seconds", type=float, default=3.0)
    p.add_argument("--log", action="store_true", help="Log mode (no carriage return)")
    ns = p.parse_args(argv)
    return Options(mode=ns.mode, width=max(10, ns.width), seconds=max(0.5, ns.seconds), log=bool(ns.log))


def render_bar(progress: float, width: int) -> str:
    """渲染 ASCII 进度条。"""

    progress = max(0.0, min(1.0, progress))
    filled = int(round(progress * width))
    bar = "#" * filled + "-" * (width - filled)
    pct = int(round(progress * 100))
    return f"[{bar}] {pct:3d}%"


def run_bar(opt: Options) -> int:
    """运行进度条演示。"""

    start = time.time()
    while True:
        t = time.time() - start
        p = min(1.0, t / opt.seconds)
        line = render_bar(p, opt.width)
        if opt.log:
            print(f"task=demo progress={int(p*100)}%")
        else:
            sys.stdout.write("\r" + line)
            sys.stdout.flush()
        if p >= 1.0:
            break
        time.sleep(0.05)
    if not opt.log:
        sys.stdout.write("\n")
    return 0


def run_spinner(opt: Options) -> int:
    """运行 spinner 演示。"""

    frames = ["|", "/", "-", "\\"]
    start = time.time()
    i = 0
    while True:
        t = time.time() - start
        if t >= opt.seconds:
            break
        frame = frames[i % len(frames)]
        if opt.log:
            print(f"task=demo status=running spinner={frame}")
        else:
            sys.stdout.write("\r" + f"loading {frame}")
            sys.stdout.flush()
        i += 1
        time.sleep(0.08)
    if not opt.log:
        sys.stdout.write("\n")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """程序入口。"""

    opt = parse_args(argv)
    if opt.mode == "spinner":
        return run_spinner(opt)
    return run_bar(opt)


if __name__ == "__main__":
    raise SystemExit(main())
