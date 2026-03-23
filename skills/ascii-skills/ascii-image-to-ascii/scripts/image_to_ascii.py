#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass
from typing import Iterable, Sequence


try:
    from PIL import Image  # type: ignore
except Exception:  # pragma: no cover
    Image = None  # type: ignore


@dataclass(frozen=True)
class Options:
    """图片转 ASCII 的参数。"""

    image_path: str
    width: int
    charset: str
    mode: str
    invert: bool
    ansi256: bool


def parse_args(argv: Sequence[str] | None = None) -> Options:
    """解析命令行参数。"""

    p = argparse.ArgumentParser(description="Convert image to ASCII art (readable/detail). Requires Pillow.")
    p.add_argument("--image", required=True, help="Image path")
    p.add_argument("--width", type=int, default=100, help="Target width in characters")
    p.add_argument("--charset", default=" .:-=+*#%@", help="ASCII charset from light to dark")
    p.add_argument("--mode", choices=["readable", "detail"], default="readable", help="Output mode")
    p.add_argument("--invert", action="store_true", help="Invert brightness mapping")
    p.add_argument("--ansi256", action="store_true", help="Add ANSI 256 colors (best-effort)")
    ns = p.parse_args(argv)
    return Options(
        image_path=ns.image,
        width=max(10, ns.width),
        charset=ns.charset,
        mode=ns.mode,
        invert=bool(ns.invert),
        ansi256=bool(ns.ansi256),
    )


def _ensure_pillow() -> None:
    """确保 Pillow 可用。"""

    if Image is None:
        raise RuntimeError("Pillow 未安装：请先执行 `pip install pillow`")


def _resize_for_terminal(img: "Image.Image", target_width: int) -> "Image.Image":
    """按终端字符比例缩放图片（字符通常比宽更“高”）。"""

    w, h = img.size
    if w <= 0 or h <= 0:
        return img
    aspect = h / w
    target_height = max(1, int(math.ceil(target_width * aspect * 0.55)))
    return img.resize((target_width, target_height))


def _normalize_charset(charset: str, mode: str) -> str:
    """根据模式对字符集做降级或增强。"""

    chars = [c for c in charset if 0x20 <= ord(c) <= 0x7E]
    if not chars:
        chars = list(" .:-=+*#%@")
    if mode == "readable":
        # 稀疏层级：减少噪点
        sparse = []
        for c in chars:
            if c in [" ", ".", ":", "-", "=", "+", "*", "#", "@"]:
                sparse.append(c)
        return "".join(sparse) if len(sparse) >= 6 else " .:-=+*#%@"
    return "".join(chars)


def _to_gray(img: "Image.Image") -> "Image.Image":
    """转换为灰度。"""

    return img.convert("L")


def _pixel_to_char(value: int, charset: str, invert: bool) -> str:
    """将 0-255 灰度映射到字符。"""

    v = 255 - value if invert else value
    idx = int((v / 255) * (len(charset) - 1))
    return charset[idx]


def _ansi256_fg(gray: int) -> str:
    """将灰度映射到 ANSI 256 色（灰阶区间）。"""

    # 232-255 是灰阶
    idx = 232 + int((gray / 255) * 23)
    return f"\x1b[38;5;{idx}m"


def image_to_ascii_lines(img: "Image.Image", charset: str, invert: bool, ansi256: bool) -> Iterable[str]:
    """把灰度图转换为 ASCII 行。"""

    pixels = img.load()
    w, h = img.size
    reset = "\x1b[0m"
    for y in range(h):
        line_chars = []
        for x in range(w):
            gray = int(pixels[x, y])
            ch = _pixel_to_char(gray, charset, invert)
            if ansi256 and ch != " ":
                line_chars.append(_ansi256_fg(gray) + ch + reset)
            else:
                line_chars.append(ch)
        yield "".join(line_chars).rstrip()


def main(argv: Sequence[str] | None = None) -> int:
    """程序入口。"""

    try:
        _ensure_pillow()
        opt = parse_args(argv)
        charset = _normalize_charset(opt.charset, opt.mode)

        img = Image.open(opt.image_path)  # type: ignore[misc]
        img = _resize_for_terminal(img, opt.width)
        img = _to_gray(img)

        for line in image_to_ascii_lines(img, charset, opt.invert, opt.ansi256):
            print(line)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
