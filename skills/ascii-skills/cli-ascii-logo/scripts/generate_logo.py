#!/usr/bin/env python3
"""
Generate a Spec-Kit-like ASCII logo/banner for CLI tools.

This script renders a small block font, optionally wraps it in a box frame,
and optionally applies a 24-bit ANSI gradient for terminals that support it.
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


RGB = Tuple[int, int, int]


@dataclass(frozen=True)
class Palette:
    """Represents a gradient palette from start RGB to end RGB."""

    start: RGB
    end: RGB


def clamp_u8(value: int) -> int:
    """Clamp an integer to the [0, 255] range."""

    return max(0, min(255, int(value)))


def lerp(a: float, b: float, t: float) -> float:
    """Linearly interpolate between a and b by t (0..1)."""

    return a + (b - a) * t


def lerp_rgb(start: RGB, end: RGB, t: float) -> RGB:
    """Linearly interpolate between two RGB colors by t (0..1)."""

    r = clamp_u8(round(lerp(start[0], end[0], t)))
    g = clamp_u8(round(lerp(start[1], end[1], t)))
    b = clamp_u8(round(lerp(start[2], end[2], t)))
    return (r, g, b)


def ansi_fg(rgb: RGB) -> str:
    """Return an ANSI escape sequence for 24-bit foreground color."""

    r, g, b = rgb
    return f"\x1b[38;2;{r};{g};{b}m"


def ansi_reset() -> str:
    """Return an ANSI reset escape sequence."""

    return "\x1b[0m"


def default_palettes() -> Dict[str, Palette]:
    """Return built-in palette presets."""

    return {
        "spec-kit": Palette((0, 255, 204), (153, 102, 255)),
        "cyan-purple": Palette((0, 230, 255), (170, 0, 255)),
        "cyan-blue": Palette((0, 255, 204), (0, 120, 255)),
        "orange-pink": Palette((255, 153, 51), (255, 51, 153)),
        "green-cyan": Palette((80, 255, 120), (0, 255, 255)),
        "mono": Palette((255, 255, 255), (255, 255, 255)),
    }


def supports_color(force: bool, no_color: bool) -> bool:
    """Decide whether ANSI coloring should be enabled."""

    if force:
        return True
    if no_color:
        return False
    if os.environ.get("NO_COLOR"):
        return False
    return sys.stdout.isatty()


def block_font() -> Dict[str, List[str]]:
    """Return a 5x7 block font mapping for A-Z, 0-9, dash, and space."""

    return {
        "A": [
            " ███ ",
            "█   █",
            "█   █",
            "█████",
            "█   █",
            "█   █",
            "█   █",
        ],
        "B": [
            "████ ",
            "█   █",
            "█   █",
            "████ ",
            "█   █",
            "█   █",
            "████ ",
        ],
        "C": [
            " ████",
            "█    ",
            "█    ",
            "█    ",
            "█    ",
            "█    ",
            " ████",
        ],
        "D": [
            "████ ",
            "█   █",
            "█   █",
            "█   █",
            "█   █",
            "█   █",
            "████ ",
        ],
        "E": [
            "█████",
            "█    ",
            "█    ",
            "████ ",
            "█    ",
            "█    ",
            "█████",
        ],
        "F": [
            "█████",
            "█    ",
            "█    ",
            "████ ",
            "█    ",
            "█    ",
            "█    ",
        ],
        "G": [
            " ████",
            "█    ",
            "█    ",
            "█ ███",
            "█   █",
            "█   █",
            " ████",
        ],
        "H": [
            "█   █",
            "█   █",
            "█   █",
            "█████",
            "█   █",
            "█   █",
            "█   █",
        ],
        "I": [
            "█████",
            "  █  ",
            "  █  ",
            "  █  ",
            "  █  ",
            "  █  ",
            "█████",
        ],
        "J": [
            "█████",
            "   █ ",
            "   █ ",
            "   █ ",
            "   █ ",
            "█  █ ",
            " ██  ",
        ],
        "K": [
            "█   █",
            "█  █ ",
            "█ █  ",
            "██   ",
            "█ █  ",
            "█  █ ",
            "█   █",
        ],
        "L": [
            "█    ",
            "█    ",
            "█    ",
            "█    ",
            "█    ",
            "█    ",
            "█████",
        ],
        "M": [
            "█   █",
            "██ ██",
            "█ █ █",
            "█   █",
            "█   █",
            "█   █",
            "█   █",
        ],
        "N": [
            "█   █",
            "██  █",
            "█ █ █",
            "█  ██",
            "█   █",
            "█   █",
            "█   █",
        ],
        "O": [
            " ███ ",
            "█   █",
            "█   █",
            "█   █",
            "█   █",
            "█   █",
            " ███ ",
        ],
        "P": [
            "████ ",
            "█   █",
            "█   █",
            "████ ",
            "█    ",
            "█    ",
            "█    ",
        ],
        "Q": [
            " ███ ",
            "█   █",
            "█   █",
            "█   █",
            "█ █ █",
            "█  █ ",
            " ██ █",
        ],
        "R": [
            "████ ",
            "█   █",
            "█   █",
            "████ ",
            "█ █  ",
            "█  █ ",
            "█   █",
        ],
        "S": [
            " ████",
            "█    ",
            "█    ",
            " ███ ",
            "    █",
            "    █",
            "████ ",
        ],
        "T": [
            "█████",
            "  █  ",
            "  █  ",
            "  █  ",
            "  █  ",
            "  █  ",
            "  █  ",
        ],
        "U": [
            "█   █",
            "█   █",
            "█   █",
            "█   █",
            "█   █",
            "█   █",
            " ███ ",
        ],
        "V": [
            "█   █",
            "█   █",
            "█   █",
            "█   █",
            "█   █",
            " █ █ ",
            "  █  ",
        ],
        "W": [
            "█   █",
            "█   █",
            "█   █",
            "█   █",
            "█ █ █",
            "██ ██",
            "█   █",
        ],
        "X": [
            "█   █",
            "█   █",
            " █ █ ",
            "  █  ",
            " █ █ ",
            "█   █",
            "█   █",
        ],
        "Y": [
            "█   █",
            "█   █",
            " █ █ ",
            "  █  ",
            "  █  ",
            "  █  ",
            "  █  ",
        ],
        "Z": [
            "█████",
            "    █",
            "   █ ",
            "  █  ",
            " █   ",
            "█    ",
            "█████",
        ],
        "0": [
            " ███ ",
            "█   █",
            "█  ██",
            "█ █ █",
            "██  █",
            "█   █",
            " ███ ",
        ],
        "1": [
            "  █  ",
            " ██  ",
            "  █  ",
            "  █  ",
            "  █  ",
            "  █  ",
            " ███ ",
        ],
        "2": [
            " ███ ",
            "█   █",
            "    █",
            "   █ ",
            "  █  ",
            " █   ",
            "█████",
        ],
        "3": [
            "████ ",
            "    █",
            "    █",
            " ███ ",
            "    █",
            "    █",
            "████ ",
        ],
        "4": [
            "█   █",
            "█   █",
            "█   █",
            "█████",
            "    █",
            "    █",
            "    █",
        ],
        "5": [
            "█████",
            "█    ",
            "█    ",
            "████ ",
            "    █",
            "    █",
            "████ ",
        ],
        "6": [
            " ███ ",
            "█    ",
            "█    ",
            "████ ",
            "█   █",
            "█   █",
            " ███ ",
        ],
        "7": [
            "█████",
            "    █",
            "   █ ",
            "  █  ",
            " █   ",
            " █   ",
            " █   ",
        ],
        "8": [
            " ███ ",
            "█   █",
            "█   █",
            " ███ ",
            "█   █",
            "█   █",
            " ███ ",
        ],
        "9": [
            " ███ ",
            "█   █",
            "█   █",
            " ████",
            "    █",
            "    █",
            " ███ ",
        ],
        "-": [
            "     ",
            "     ",
            "     ",
            "█████",
            "     ",
            "     ",
            "     ",
        ],
        " ": [
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
        ],
        "?": [
            "████ ",
            "    █",
            "   █ ",
            "  █  ",
            "  █  ",
            "     ",
            "  █  ",
        ],
    }


def normalize_text(text: str) -> str:
    """Normalize text for the 10、Company Manger font renderer."""

    return (text or "").upper()


def render_block_text(text: str, font: Dict[str, List[str]]) -> List[str]:
    """Render text using the built-in 5x7 block font."""

    normalized = normalize_text(text)
    glyphs = [font.get(ch, font["?"]) for ch in normalized]
    height = len(font["A"])
    lines: List[str] = []
    for row in range(height):
        parts = [g[row] for g in glyphs]
        lines.append(" ".join(parts).rstrip())
    return trim_trailing_blank_lines(lines)


def trim_trailing_blank_lines(lines: List[str]) -> List[str]:
    """Trim empty lines at the end of a multi-line block."""

    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def pad_to_width(line: str, width: int) -> str:
    """Right-pad a line with spaces to the requested width."""

    if len(line) >= width:
        return line[:width]
    return line + (" " * (width - len(line)))


def box_frame(lines: List[str], width: int) -> List[str]:
    """Wrap lines in a box frame using box-drawing characters."""

    inner_width = max(1, width)
    top = "╔" + ("═" * inner_width) + "╗"
    bottom = "╚" + ("═" * inner_width) + "╝"
    framed = [top]
    for line in lines:
        framed.append("║" + pad_to_width(line, inner_width) + "║")
    framed.append(bottom)
    return framed


def center_line(line: str, width: int) -> str:
    """Center a line inside a fixed width with space padding."""

    if width <= 0:
        return line
    text = line.rstrip()
    if len(text) >= width:
        return text[:width]
    left = (width - len(text)) // 2
    right = width - len(text) - left
    return (" " * left) + text + (" " * right)


def apply_gradient(line: str, palette: Palette) -> str:
    """Apply an ANSI foreground gradient to a single line."""

    length = len(line)
    if length == 0:
        return line
    colored: List[str] = []
    for i, ch in enumerate(line):
        t = 0.0 if length == 1 else (i / (length - 1))
        rgb = lerp_rgb(palette.start, palette.end, t)
        if ch == " ":
            colored.append(ch)
        else:
            colored.append(ansi_fg(rgb) + ch)
    return "".join(colored) + ansi_reset()


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    """Parse CLI arguments."""

    parser = argparse.ArgumentParser(prog="generate_logo.py")
    parser.add_argument("--text", required=True, help="Logo text, e.g. auto-cli")
    parser.add_argument("--subtitle", default="", help="Subtitle line under the logo")
    parser.add_argument("--width", type=int, default=46, help="Inner width of the frame")
    parser.add_argument("--palette", default="spec-kit", help="Palette preset name")
    parser.add_argument("--frame", choices=["box", "none"], default="box", help="Frame style")
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI colors")
    parser.add_argument("--force-color", action="store_true", help="Force ANSI colors even when not TTY")
    return parser.parse_args(list(argv))


def build_banner_lines(text: str, subtitle: str, width: int) -> Tuple[List[str], int]:
    """Build the uncolored inner lines for the banner and return (lines, inner_width)."""

    font = block_font()
    logo_lines = render_block_text(text, font)
    max_inner = max((len(l) for l in logo_lines), default=0)
    inner_width = max(width, max_inner)

    centered_logo = [center_line(l, inner_width) for l in logo_lines]
    lines: List[str] = list(centered_logo)
    if subtitle.strip():
        lines.append(center_line(subtitle.strip(), inner_width))
    return lines, inner_width


def main(argv: Iterable[str]) -> int:
    """Program entry point."""

    args = parse_args(argv)
    palettes = default_palettes()
    palette = palettes.get(args.palette, palettes["spec-kit"])
    use_color = supports_color(force=args.force_color, no_color=args.no_color)

    inner_lines, inner_width = build_banner_lines(args.text, args.subtitle, args.width)

    if args.frame == "box":
        output_lines = box_frame(inner_lines, inner_width)
        if use_color:
            output_lines = [apply_gradient(line, palette) for line in output_lines]
    else:
        output_lines = inner_lines
        if use_color:
            output_lines = [apply_gradient(line, palette) for line in output_lines]

    sys.stdout.write("\n".join(output_lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
