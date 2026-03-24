#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple


@dataclass(frozen=True)
class Spec:
    """boxflow 图规格（简化版）。"""

    nodes: List[str]
    edges: List[Tuple[str, str]]
    box_width: int


def _box(label: str, width: int) -> List[str]:
    """生成固定宽度的 ASCII 盒子。"""

    inner = max(1, width - 2)
    text = (label or "")[:inner].center(inner)
    top = "+" + "-" * inner + "+"
    mid = "|" + text + "|"
    return [top, mid, top]


def _parse(stdin_text: str) -> Spec:
    """解析 stdin JSON 到 Spec。"""

    data = json.loads(stdin_text)
    nodes = [str(n) for n in data.get("nodes", [])]
    edges = [(str(a), str(b)) for a, b in data.get("edges", [])]
    box_width = int(data.get("boxWidth", 14))
    return Spec(nodes=nodes, edges=edges, box_width=max(10, box_width))


def _children_map(edges: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    """构建 from -> children 映射。"""

    m: Dict[str, List[str]] = {}
    for a, b in edges:
        m.setdefault(a, []).append(b)
    return m


def render_tb(spec: Spec) -> str:
    """渲染 TB 方向（线性 + 单点二分支）。"""

    if not spec.nodes:
        return ""
    children = _children_map(spec.edges)
    w = spec.box_width

    # 选择一个起点：优先用 nodes[0]
    start = spec.nodes[0]
    lines: List[str] = []

    def add_box(label: str) -> None:
        for l in _box(label, w):
            lines.append(l)

    cur = start
    visited: set[str] = set()
    while cur and cur not in visited:
        visited.add(cur)
        add_box(cur)
        kids = children.get(cur, [])
        if not kids:
            break
        if len(kids) == 1:
            lines.append(" " * (w // 2) + "|")
            lines.append(" " * (w // 2) + "v")
            cur = kids[0]
            continue

        # 仅支持二分支展示
        left, right = kids[0], kids[1]
        lines.append(" " * (w // 2 - 1) + "|     |")
        lines.append(" " * (w // 2 - 1) + "v     v")

        left_box = _box(left, w)
        right_box = _box(right, w)
        for i in range(3):
            lines.append(left_box[i] + "  " + right_box[i])
        break

    return "\n".join(lines).rstrip()


def main(argv: Sequence[str] | None = None) -> int:
    """程序入口：从 stdin 读取 JSON，输出 TB boxflow。"""

    raw = sys.stdin.read().strip()
    if not raw:
        print("Error: empty stdin. Provide JSON {nodes:[], edges:[[]]}.", file=sys.stderr)
        return 1
    spec = _parse(raw)
    print(render_tb(spec))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
